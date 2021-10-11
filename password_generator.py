from random import randint

def main():
    alphabet_list = alphabet()
    symbols_list = symbols()
    ch1, ch2, ch3 = choices()
    proceed, ch2_proceed, ch3_proceed = check(ch2, ch3)
    generation(alphabet_list, symbols_list, proceed, ch2_proceed, ch3_proceed, ch1)


def generation(alphabet_list, symbols_list, proceed, ch2_proceed, ch3_proceed, ch1):
    password = ''
    for i in range(ch1):
        #Checking the choices that are True
        if proceed == 0:
            random_selection = 1
        elif proceed == 1:
            random_selection = randint(1, 2)
        else:
            random_selection = randint(1, 3)
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
        for i in range(ch1):
            #Checking the choices that are True
            if proceed == 0:
                random_selection = 1
            elif proceed == 1:
                random_selection = randint(1, 2)
            else:
                random_selection = randint(1, 3)
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
                if lower_letters == 0 or upper_letters == 0:
                    password = ''
                    lower_letters = 0
                    upper_letters = 0
                    cont_loop = True
                else:
                    cont_loop = False 
        except Exception:
            cont_loop = False 

    print(password)


def check(ch2, ch3):
    ch2_proceed = False
    ch3_proceed = False
    proceed = 0
    if ch2 == 1:
        ch2_proceed = True
        proceed += 1
    if ch3 == 2:
        ch3_proceed = True
        proceed += 1
    return proceed, ch2_proceed, ch3_proceed


def choices():
    choice1 = int(input('How big do you want your password to be: '))
    print('')
    choice2 = int(input('Do you want your password to contain letter? If yes give --> 1 else give 0: '))
    print('')
    while choice2 > 1 or choice2 < 0:
        print('Wrong input. Please try again.')
        choice2 = int(input('Do you want your password to contain letter? If yes give --> 1 else give 0: '))
        print('')
    choice3 = int(input('Do you want your password to contain symbols? If yes give --> 2 else give 0: '))
    print('')
    while choice3 > 2 or choice2 < 0:
        print('Wrong input. Please try again.')
        choice2 = int(input('Do you want your password to contain symbols? If yes give --> 2 else give 0: '))
        print('')
    return choice1, choice2, choice3


def alphabet():
    alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                     'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                     'U', 'V', 'W', 'X', 'Y', 'Z']
    return alphabet_list

def symbols():
    symp = ['!', '@', '#', '$', '%', '*', '^', '&', '/']
    return symp

main()