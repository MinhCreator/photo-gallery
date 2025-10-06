import bcrypt
import string
import secrets

def generate_random_string(length=int):
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for _ in range(length))

def generate_password_hash(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

def secret_key_gen():
    password = generate_random_string(16)
    salt_pass = generate_password_hash(password)
    return salt_pass



