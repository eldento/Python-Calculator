import time
from calculator import Calculator
from exceptions import DivisionError, InvalidOperationError
from utils import colored_print, get_number
from colorama import Fore, init

init(autoreset=True)
calc = Calculator()

# Kullanıcı adı girişini burda alıyoruz.
username = input("Kullanıcı adınızı giriniz: ").strip().capitalize()

# Hesap makinesi menümüzü ekrana getiriyoruz.
def show_menu():
    colored_print(f"""
===  Profesyonel Hesap Makinesi ===
Hoş geldin, {username}! 
1️⃣  Toplama
2️⃣  Çıkarma
3️⃣  Çarpma
4️⃣  Bölme
5️⃣  İşlem Geçmişini Gör
6️⃣  Son İşlemi Geri Al
q️⃣  Çıkış
""", Fore.CYAN)

while True:
    show_menu()
    choice = input("Bir işlem seçiniz: ").strip().lower()

    # Geçersiz girişleri atlıyoruz.
    if choice not in ["1", "2", "3", "4", "5", "6", "q", ""]:
        continue

    if choice == "":
        continue

    if choice == "q":
        colored_print(f" Program sonlandırıldı. Görüşürüz {username}!", Fore.GREEN)
        break

    try:
        if choice in ["1", "2", "3", "4"]:
            a = get_number("Birinci sayıyı giriniz: ")
            b = get_number("İkinci sayıyı giriniz: ")

            if choice == "1":
                result = calc.add(a, b)
            elif choice == "2":
                result = calc.subtract(a, b)
            elif choice == "3":
                result = calc.multiply(a, b)
            elif choice == "4":
                result = calc.divide(a, b)

            colored_print(f" Sonuç: {result}", Fore.GREEN)
            time.sleep(1.5)
            input("Devam etmek için Enter'a basın...")

        elif choice == "5":
            calc.show_history()
            input("Devam etmek için Enter'a basın...")

        elif choice == "6":
            calc.undo_last()
            input("Devam etmek için Enter'a basın...")

    except DivisionError as e:
        colored_print(f"Hata: {e}", Fore.RED)
        time.sleep(1.5)
    except InvalidOperationError as e:
        colored_print(f"Hata: {e}", Fore.RED)
        time.sleep(1.5)
    except Exception as e:
        colored_print(f"Beklenmeyen bir hata oluştu: {e}", Fore.RED)
        time.sleep(1.5)
