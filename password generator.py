import random
import string


def generate_password(length, include_upper, include_lower, include_numbers, include_special):
    character_pool = ""

    if include_upper:
        character_pool += string.ascii_uppercase
    if include_lower:
        character_pool += string.ascii_lowercase
    if include_numbers:
        character_pool += string.digits
    if include_special:
        character_pool += string.punctuation

    if not character_pool:
        raise ValueError("At least one character type must be selected.")

    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password


def main():
    print("Welcome to the Random Password Generator!")

    # Get user input
    length = int(input("Enter desired password length (minimum 6): "))
    if length < 6:
        print("Password length should be at least 6 characters.")
        return

    include_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    include_special = input("Include special characters? (y/n): ").lower() == 'y'

    try:
        password = generate_password(length, include_upper, include_lower, include_numbers, include_special)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
