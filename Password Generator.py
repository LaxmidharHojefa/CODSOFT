import random
import string

def generate_password(length):
    """Generate a random password with the specified length."""
    
    # Character set: uppercase, lowercase, digits, and special characters
    char_set = string.ascii_letters + string.digits + string.punctuation
    
    # Ensure the password has at least one uppercase, one lowercase, one digit, and one special character
    if length < 4:
        return "Password length should be at least 4 characters for complexity."
    
    # Guarantee each type of character appears at least once
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),         
        random.choice(string.punctuation)     
    ]
    
    # Fill the remaining characters randomly from the full character set
    password += random.choices(char_set, k=length - 4)
    
    # Shuffle the password list to randomize the order
    random.shuffle(password)
    
    # Convert the list to a string
    return ''.join(password)

def password_generator():
    """Main function to prompt user input and generate a password."""
    
    print("Password Generator")
    while True:
        try:
            length = int(input("Enter the desired password length (minimum 4): "))
            if length < 4:
                print("Please enter a valid length of at least 4.")
            else:
                break
        except ValueError:
            print("Invalid input! Please enter a number.")
    
    password = generate_password(length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    password_generator()
