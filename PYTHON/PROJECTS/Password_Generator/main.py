from password_generator import PasswordGenerator


def get_bool_choice(prompt: str) -> bool:
    choice = input(f"{prompt} (y/n): ").strip().lower()
    return choice in ["y", "yes"]


def main():
    print("=== Password Generator ===")

    
    try:
        length = int(input("Enter length of password: "))
        
    
        print("\n--- Configure Character Pools ---")
        use_uppercase = get_bool_choice("Include uppercase letters (A-Z)?")
        use_lowercase = get_bool_choice("Include lowercase letters (a-z)?")
        use_numbers = get_bool_choice("Include numbers (0-9)?")
        use_symbols = get_bool_choice("Include special characters (!@#$)?")

        
        generator = PasswordGenerator(
            length=length,
            use_uppercase=use_uppercase,
            use_lowercase=use_lowercase,
            use_numbers=use_numbers,
            use_symbols=use_symbols
        )

        
        secure_password = generator.generate()

        
        print("\n========================================")
        print(f"🔒 Your Secure Password: {secure_password}")
        print("========================================")

    except ValueError as e:
        # Gracefully handle non-integer lengths or failed validation logic errors from the generator
        print(f"\n❌ Error: {e}")


if __name__ == "__main__":
    main()