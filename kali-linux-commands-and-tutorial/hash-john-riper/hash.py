import hashlib

def generate_md5_hash(password):
    #covierte la contraseña a MD5 Hash
    md5_hash = hashlib.md5(password.encode()).hexdigest()
    return md5_hash

def main():
    user_id = input("escriba su usuario: ")
    password = input("escriba su contraseña: ")

    hashed_password = generate_md5_hash(password)

    print("\n detalles del login: ")
    print(f"User ID: {user_id}")
    print(f"MD5 hashed password: {hashed_password}")

if __name__ == "__main__":
    main()
