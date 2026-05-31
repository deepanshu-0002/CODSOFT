import random
import string

print("===== STRONG PASSWORD GENERATOR =====")

length = int(input("Enter Password Length: "))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

all_characters = lower + upper + digits + symbols

password = ''.join(random.choice(all_characters) for _ in range(length))

print("\nGenerated Password:", password)