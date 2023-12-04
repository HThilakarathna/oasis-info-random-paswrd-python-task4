import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        print("Error: Please enable at least one character type (letters, numbers, symbols).")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_user_input():
    try:
        length = int(input("Enter password length: "))
        use_letters = input("Include letters? (y/n): ").lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
        return length, use_letters, use_numbers, use_symbols
    except ValueError:
        print("Error: Please enter a valid numeric value for password length.")
        return None

def main():
    user_input = get_user_input()

    if user_input:
        length, use_letters, use_numbers, use_symbols = user_input
        password = generate_password(length, use_letters, use_numbers, use_symbols)

        if password:
            print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
