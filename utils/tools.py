"""Tools module"""
import bcrypt

def get_encryp_password(password):
    """This function handle the encrypting a password"""
    if password:
        password = bcrypt.hashpw(bytes(password, 'utf8'), bcrypt.gensalt(14)).decode("utf-8")
    return password