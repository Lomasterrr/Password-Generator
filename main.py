import random 
from math import sqrt
import string
import secrets
import logo
from colorama import Fore, Back, Style

logo.logo()
print("--------------------------")
print(Fore.GREEN)

Length = int(input('  Password length: '))
def generate_pass():
    letters_and_digits = string.ascii_letters + string.digits
    crypt_rand_string = ''.join(secrets.choice(
    letters_and_digits) for i in range(Length))
    print("  Result: ", crypt_rand_string)
    print(Fore.RED)
    print("--------------------------")

generate_pass()