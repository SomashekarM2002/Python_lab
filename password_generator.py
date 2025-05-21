import random
import string

def generate_password(length):
    if length < 4:
        return "Password should be at least 4 characters long."

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter desired password length: "))
        password = generate_password(length)
        print("Generated Password:", password)
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
