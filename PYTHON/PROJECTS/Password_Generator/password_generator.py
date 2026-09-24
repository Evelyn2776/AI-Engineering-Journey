import secrets
import string


class PasswordGenerator:

    def __init__(
        self, 
        length: int, 
        use_uppercase: bool, 
        use_lowercase: bool, 
        use_numbers: bool, 
        use_symbols: bool
    ):
        
        self.length = length
        self.use_uppercase = use_uppercase
        self.use_lowercase = use_lowercase
        self.use_numbers = use_numbers
        self.use_symbols = use_symbols

    def generate(self) -> str:
        # 1. Build the pool of allowed characters based on settings
        character_pool = ""
        required_characters = []

        if self.use_uppercase:
            character_pool += string.ascii_uppercase
            # Guarantee at least one character from this set is ready
            required_characters.append(secrets.choice(string.ascii_uppercase))
            
        if self.use_lowercase:
            character_pool += string.ascii_lowercase
            required_characters.append(secrets.choice(string.ascii_lowercase))
            
        if self.use_numbers:
            character_pool += string.digits
            required_characters.append(secrets.choice(string.digits))
            
        if self.use_symbols:
            character_pool += string.punctuation
            required_characters.append(secrets.choice(string.punctuation))

        # 2. Defensive check: Stop if no character pools were selected
        if not character_pool:
            raise ValueError("You must select at least one character type (uppercase, lowercase, numbers, or symbols).")

        # 3. Handle edge case: Ensure the requested length is long enough for the selected pools
        if self.length < len(required_characters):
            raise ValueError(f"Password length must be at least {len(required_characters)} to include all selected character types.")

        # 4. Fill the remaining slots randomly from the total pool
        remaining_length = self.length - len(required_characters)
        random_characters = [secrets.choice(character_pool) for _ in range(remaining_length)]

        # 5. Combine the guaranteed characters and the random ones
        password_list = required_characters + random_characters
        
        # 6. Shuffle them securely so the guaranteed characters aren't always at the front
        secrets.SystemRandom().shuffle(password_list)

        # 7. Convert the list back into a single string
        return "".join(password_list)