import random
import string

def generate_password(length, use_letters, use_numbers, use_specials):
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_specials:
        characters += string.punctuation

    if not characters:
        return "Error! Please select at least one character type."

    password = "".join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("=" * 45)
    print("      Oasis Infobyte - Python Task 3     ")
    print("        Secure Password Generator        ")
    print("=" * 45)

    while True:
        try:
            length = int(input("Enter desired password length (Min 6): "))
            if length < 6:
                print("Password should be at least 6 characters long.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")

    print("\nConfigure Password Options:")
    use_letters = input("Include Letters? (y/n): ").strip().lower() == 'y'
    use_numbers = input("Include Numbers? (y/n): ").strip().lower() == 'y'
    use_specials = input("Include Special Characters? (y/n): ").strip().lower() == 'y'

    password = generate_password(length, use_letters, use_numbers, use_specials)
    
    print("\n" + "-" * 45)
    print(f"Generated Password: {password}")
    print("-" * 45)

if __name__ == "__main__":
    main()