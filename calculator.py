# calculator.py

from exceptions import DivisionError
from colorama import Fore

class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = a + b
        self._save(a, "+", b, result)
        return result

    def subtract(self, a, b):
        result = a - b
        self._save(a, "-", b, result)
        return result

    def multiply(self, a, b):
        result = a * b
        self._save(a, "*", b, result)
        return result

    def divide(self, a, b):
        if b == 0:
            raise DivisionError("0'a bölme hatası!")
        result = a / b
        self._save(a, "/", b, result)
        return result

    def _save(self, a, operator, b, result):
        record = f"{a} {operator} {b} = {result}"
        self.history.append(record)

    def show_history(self):
        if not self.history:
            print(Fore.YELLOW + "Henüz bir işlem yapılmadı." + Fore.RESET)
        else:
            print(Fore.CYAN + "\n--- İşlem Geçmişi ---" + Fore.RESET)
            for i, record in enumerate(self.history, start=1):
                print(f"{i}. {record}")

    def undo_last(self):
        if self.history:
            last = self.history.pop()
            print(Fore.YELLOW + f"↩️ Son işlem geri alındı: {last}" + Fore.RESET)
        else:
            print(Fore.RED + "Geri alınacak işlem yok!" + Fore.RESET)
