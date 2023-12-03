import sys

work_is_busy = False

def user_cmd_not_ok(cmd):
    if cmd < 0 or cmd > 2:
        return True
    else:
        return False

def user_cmd_work_start():
    global work_is_busy

    if work_is_busy == True:
        print("Trwa praca!")
    else:
        work_is_busy = True
        print("Praca rozpoczeta")

while True:
    print()
    print("--- Rejestrator czasu pracy ---")
    print("[0] - Wyjscie")
    print("[1] - Rozpoczecie pracy")
    print("[2] - Zakonczenie pracy")

    user_cmd = int(input("Twoj wybor: "))
    if user_cmd_not_ok(user_cmd):
        print("Nieprawdilowy wybor!")
    else:
        if user_cmd == 0:
            exit(0)

        if user_cmd == 1:
            user_cmd_work_start()

        if user_cmd == 2:
            work_is_busy = False
            print('Praca zakonczona')