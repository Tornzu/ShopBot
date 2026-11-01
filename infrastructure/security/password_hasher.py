from argon2 import PasswordHasher

hasher = PasswordHasher()

def hash_password(password):
    return hasher.hash(password)

def verify_password(password, hashed_password):
    try:
        return hasher.verify(hashed_password, password)
    except:
        return False