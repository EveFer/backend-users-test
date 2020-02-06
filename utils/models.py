"""Django models utilities"""

#django
from django.db import models

class CommonFields(models.Model):
    """
        Clase en donde se heredarán los demas modelos
        para que se pueda incluir los campos:
        +created(Datetime)
        +modified(Datetime)
    """

    created = models.DateTimeField('Created At', auto_now_add=True)
    modified = models.DateTimeField('Modified At', auto_now=True)

    class Meta:
        """Clase en la cual se configurará de forma que la clase se pueda heredar"""
        abstract = True