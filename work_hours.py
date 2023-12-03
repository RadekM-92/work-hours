import sys


while True:
    print()
    print("--- Rejestrator czasu pracy ---")
    print("[0] - Wyjscie")
    print("[1] - Rozpoczecie pracy")
    print("[2] - Zakonczenie pracy")

    user_cmd = int(input("Twoj wybor: "))

    if user_cmd == 0:
        exit(0)

    if user_cmd == 1:
        print("Praca rozpoczeta")

    if user_cmd == 2:
        print('Praca zakonczona')