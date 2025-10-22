# utils.py

from colorama import Fore, Style

def colored_print(text, color=Fore.WHITE):
    print(color + str(text) + Style.RESET_ALL)

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            colored_print("Lütfen geçerli bir sayı giriniz!", Fore.RED)
