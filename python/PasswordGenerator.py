import random
import string

def generate_password(length=12):
    # Define possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password by selecting random characters
    password = ''.join(random.choice(characters) for i in range(length))
    return password

if __name__ == "__main__":
    # Get the desired password length from the user
    length = int(input("Enter the password length: "))
    password = generate_password(length)
    print("Generated password:", password)
