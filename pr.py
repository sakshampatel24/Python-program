import secrets
import string

def create_pw(pw_length=13):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    alphabet = letters + digits + special_chars
    pw_strong = False
    
    while not pw_strong:
        pwd = ''.join(secrets.choice(alphabet) for _ in range(pw_length))
        if any(char in special_chars for char in pwd) and sum(char in digits for char in pwd) >= 2:
            pw_strong = True
    
    return pwd

def generate_passwords(num_passwords=5, pw_length=13):
    passwords = [create_pw(pw_length) for _ in range(num_passwords)]
    return passwords

if __name__ == '__main__':
    num_passwords = 5
    pw_length = 15
    
    passwords = generate_passwords(num_passwords, pw_length)
    
    print(f"Generated {num_passwords} strong passwords:")
    for i, password in enumerate(passwords, start=1):
        print(f"Password {i}: {password}")
