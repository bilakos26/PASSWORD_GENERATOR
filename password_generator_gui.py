from random import randint
import random
import PySimpleGUI as sg

# Theme
sg.theme("darkblue1")

layout = [
    [sg.Frame("Password length: ", [[sg.Input(key = '-PASS_LENGTH-', font = ("Arial", 12), text_color='Black')]], size = (150, 40))],
    [sg.Checkbox("Letters", key = '-LETTERS-')],
    [sg.Checkbox("Symbols", key = '-SYMBOLS-')],
    [sg.Button("Create", key = '-CREATE-', button_color=("green", "black"), font= ("Arial", 20))],
    [sg.Multiline("", key = "-DESCRIPTION-", size = (100, 5), font = ("Arial", 12), text_color='Black', no_scrollbar=True, disabled=True)]
]

def main(pl, values):
    alphabet_list = alphabet()
    symbols_list = symbols()
    proceed, ch2_proceed, ch3_proceed = check(values)
    generation(alphabet_list, symbols_list, proceed, ch2_proceed, ch3_proceed, pl)


def generation(alphabet_list, symbols_list, proceed, ch2_proceed, ch3_proceed, pl):
    password = ''
    for i in range(pl):
        #Checking the choices that are True
        if proceed == 0:
            random_selection = 1
        elif proceed == 1 and ch2_proceed:
            random_selection = randint(1, 2)
        else:
            if ch2_proceed:
                random_selection = randint(1, 3)
            else:
                random_selection = random.choice([1, 3])
        #Creating the password by the random_selection values
        if random_selection == 1:
            password = password + str(randint(0, 9))
        elif random_selection == 2 and ch2_proceed == True:
            lower_lt = randint(0, 1)
            if lower_lt == 1:
                alph_index = randint(0, len(alphabet_list)-1)
                password = password + alphabet_list[alph_index].lower()
            else:
                alph_index = randint(0, len(alphabet_list)-1)
                password = password + alphabet_list[alph_index]
        elif random_selection == 3 and ch3_proceed == True:
            symp_index = randint(0, len(symbols_list)-1)
            password = password + symbols_list[symp_index]
    lower_letters = 0
    upper_letters = 0
    cont_loop = False
    for i in password:
        try:
            if type(int(password)) != int:
                if i.islower():
                    lower_letters += 1
                if i.isupper():
                    upper_letters += 1
        except Exception:
            if i.islower():
                lower_letters += 1
            if i.isupper():
                upper_letters += 1
    try:
        if type(int(password)) != int:
            if ch2_proceed:
                if lower_letters == 0 or upper_letters == 0:
                    password = ''
                    lower_letters = 0
                    upper_letters = 0
                    cont_loop = True
            else:
                cont_loop = False 
    except Exception:
        cont_loop = False

    #If the "For" loop give cont_loop = True the script will continue with the "while" loop
    while cont_loop:
        for i in range(pl):
            #Checking the choices that are True
            if proceed == 0:
                random_selection = 1
            elif proceed == 1 and ch2_proceed:
                random_selection = randint(1, 2)
            else:
                if ch2_proceed:
                    random_selection = randint(1, 3)
                else:
                    random_selection = random.choice([1, 3])
            #Creating the password by the random_selection values
            if random_selection == 1:
                password = password + str(randint(0, 9))
            elif random_selection == 2 and ch2_proceed == True:
                lower_lt = randint(0, 1)
                if lower_lt == 1:
                    alph_index = randint(0, len(alphabet_list)-1)
                    password = password + alphabet_list[alph_index].lower()
                else:
                    alph_index = randint(0, len(alphabet_list)-1)
                    password = password + alphabet_list[alph_index]
            elif random_selection == 3 and ch3_proceed == True:
                symp_index = randint(0, len(symbols_list)-1)
                password = password + symbols_list[symp_index]
        for i in password:
            try:
                if type(int(password)) != int:
                    if i.islower():
                        lower_letters += 1
                    if i.isupper():
                        upper_letters += 1
            except Exception:
                if i.islower():
                    lower_letters += 1
                if i.isupper():
                    upper_letters += 1
        try:
            if type(int(password)) != int:
                if ch2_proceed:
                    if lower_letters == 0 or upper_letters == 0:
                        password = ''
                        lower_letters = 0
                        upper_letters = 0
                        cont_loop = True
                else:
                    cont_loop = False 
        except Exception:
            cont_loop = False 

    window['-DESCRIPTION-'].update(password)


def check(values):
    ch2_proceed = False
    ch3_proceed = False
    proceed = 0
    if values["-LETTERS-"]:
        ch2_proceed = True
        proceed += 1
    if values["-SYMBOLS-"]:
        ch3_proceed = True
        proceed += 1
    return proceed, ch2_proceed, ch3_proceed


def alphabet():
    alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                     'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                     'U', 'V', 'W', 'X', 'Y', 'Z']
    return alphabet_list

def symbols():
    symp = ['!', '@', '#', '$', '%', '*', '^', '&', '/']
    return symp

if __name__ == "__main__":
    window = sg.Window("Password Generator", layout, size = (500, 450))

    while True:
        event, values = window.read()
        
        if event == sg.WIN_CLOSED:
            break
        
        if event == "-CREATE-":
            try:
                pl = int(values["-PASS_LENGTH-"])
                main(pl, values)
            except Exception:
                sg.Popup("Error", 'The "Password length" must be an interger not a string or empty.')

    window.close()