import random
import string

print("=" * 50)
print("        RANDOM PASSWORD GENERATOR")
print("=" * 50)

def generate_password(length, use_special):
    
    # Base characters
    letters = string.ascii_letters
    digits = string.digits
    characters = letters + digits
    if use_special:
        characters += string.punctuation

    password = ""

    for i in range(length):
        random_character = random.choice(characters)
        password += random_character

    return password

while True:

    try:
        password_length = int(input("\nEnter desired password length: "))

        if password_length <= 0:
            print("Password length must be greater than 0.")
            continue

        break

    except ValueError:
        print("Please enter a valid number.")

choice = input(
    "Do you want to include special characters? (yes/no): "
).lower()

if choice == "yes":
    special_characters = True
else:
    special_characters = False

while True:

    try:
        total_passwords = int(
            input("How many passwords do you want to generate? ")
        )

        if total_passwords <= 0:
            print("Please enter a number greater than 0.")
            continue

        break

    except ValueError:
        print("Invalid input. Enter a number.")


print("\n" + "=" * 50)
print("GENERATED PASSWORDS")
print("=" * 50)

for count in range(1, total_passwords + 1):

    password = generate_password(
        password_length,
        special_characters
    )
    print(f"Password {count}: {password}")
print("\n" + "=" * 50)
print("Password generation completed successfully!")
print("=" * 50)
