import sys
import datetime

work_is_busy = False

work_hours_list = []
work_start_date = ''
work_start_time = ''
work_stop_date = ''
work_stop_time = ''

def show_main_menu():
    print()
    print("--- Rejestrator czasu pracy ---")
    print("[0] - Wyjscie")
    print("[1] - Rozpoczecie pracy")
    print("[2] - Zakonczenie pracy")
    print()

def user_cmd_not_ok(cmd):
    if cmd < 0 or cmd > 2:
        return True
    else:
        return False

def user_cmd_work_start():
    global work_is_busy
    global work_start_date
    global work_start_time

    if work_is_busy == True:
        print("Trwa praca!")
    else:
        ct = datetime.datetime.now()
        work_start_date = str(ct.date())
        work_start_time = "".join(str(ct.hour) + ":" + str(ct.minute))
        work_is_busy = True
        print("Praca rozpoczeta")

def user_cmd_work_stop():
    global work_is_busy
    global work_stop_date
    global work_stop_time

    ct = datetime.datetime.now()
    work_stop_date = str(ct.date())
    work_stop_time = "".join(str(ct.hour) + ":" + str(ct.minute))

    work_is_busy = False
    print('Praca zakonczona')

def create_new_file():
    file = open("Work_Hours_Log.txt", "w+")
    
    file.write("Start_Date:" + '\t' "Stop_date:" + '\t' + "Start_Time:" + '\t' + "Stop_Time:" + '\n')
    file.close()

def load_file():
    try:
        file = open("Work_Hours_Log.txt")

        for line in file.readlines():
            if line == 0:
                continue
            else:
                work_hours_list.append(line.strip())
            
        file.close()
    except FileNotFoundError:
        create_new_file()

load_file()

while True:
    show_main_menu()

    user_cmd = int(input("Twoj wybor: "))
    if user_cmd_not_ok(user_cmd):
        print("Nieprawdilowy wybor!")
    else:
        if user_cmd == 0:
            exit(0)

        if user_cmd == 1:
            user_cmd_work_start()

        if user_cmd == 2:
            user_cmd_work_stop()

