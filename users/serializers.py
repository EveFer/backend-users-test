#django
from datetime import timedelta
from django.core.validators import RegexValidator
from django.utils import timezone
from django.conf import settings
from django.shortcuts import get_object_or_404
#rest framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
#utilities
import jwt
import bcrypt
#models
from users.models import User

from utils import tools

class UserModelSerializer(serializers.ModelSerializer):
    """Instructor model serializer"""
    password = serializers.CharField(
        write_only=True,
        required=True,
        allow_null=True,
        validators=[
            RegexValidator(
                regex='^[A-Za-z0-9@#$_-]{8,16}$',
                message='Password doesnt comply',
            ),
        ],
        min_length=8,
    )
    password_confirmation = serializers.CharField(
        write_only=True,
        required=True,
        allow_null=True,
        validators=[
            RegexValidator(
                regex='^[A-Za-z0-9@#$_-]{8,16}$',
                message='Password doesnt comply',
            ),
        ],
        min_length=8,
    )
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    # def validate(self, data):
    #     """Varify password match"""
    #     passwd = data['password']
    #     passwd_conf = data['password_confirmation']
    #     if passwd != passwd_conf:
    #         raise serializers.ValidationError("Passwords don´t match.")
    #     return data

    def create(self, validated_data):
        passwd = data['password']
        passwd_conf = validated_data.pop('password_confirmation')
        if passwd != passwd_conf:
            raise serializers.ValidationError("Passwords don´t match.")

        if 'email' in validated_data and 'password' in validated_data:
            validated_data['password'] = tools.get_encryp_password(validated_data.get('password'))

            user = User.objects.create(**validated_data)
            user.save()
            return user
        else:
            error = {
                'message': 'You have to provide email and password'
            }
            raise serializers.ValidationError(error)

    def update(self, instance, validated_data):
        for i in validated_data:
            setattr(instance, i, validated_data[i])
        print()
        if validated_data.get('password'):
            instance.password = tools.get_encryp_password(validated_data.get('password'))

        instance.save()
        return instance


    class Meta:
        model = User
        exclude = ['created', 'modified']

class UserResponseModelSerializer(serializers.ModelSerializer):
    """Instructor Response model serializer"""

    class Meta:
        model = User
        exclude = ['created', 'modified']
        

class UserLoginSerializer(serializers.Serializer):
    """Instructor Login serializer"""
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8)

    def validate(self, data):
        """Check credentials"""
        email = data['email']
        password = data['password']

        user = get_object_or_404(User, email=email)
        password = bytes(password, 'utf8')
        is_valid = False if not user.password else bcrypt.checkpw(
            password,
            bytes(user.password, 'utf8'))
        if not is_valid:
            raise serializers.ValidationError('Invalid credentials')
        return data

    def create(self, validated_data):
        """Generate new access Token"""
        user = User.objects.get(email=validated_data['email'])
        instructor = {
            'id': user.id,
            'email': user.email,
            'name': user.full_name
        }
        exp_date = timezone.now()+timedelta(hours=24)
        payload = {
            'user': instructor,
            'exp': int(exp_date.timestamp())
        }

        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
        return token.decode()