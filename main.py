# Kenet Ortiz

# Main of the program, controls the loop of the program
def main():
    program_state = True
    while program_state:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        option = input('\nPlease enter an option: ')
        do_options(option)


# do_options method, deals with the option picked by the user
def do_options(option):
    if option == '1':
        global new_password
        new_password = encode()
    elif option == '2':
        pass
    elif option == '3':
        quit()
    else:
        print('Please enter a valid option')


# encode option, encodes the 8 digits password typed by the user, returns the encoded password
def encode():
    password = input('Please enter your password to encode: ')
    new_password = ''
    try:
        if len(password) == 8:
            for current in password:
                aux = int(current) + 3
                if len(str(aux)) == 2:
                    aux1 = str(aux)
                    new_password = new_password + aux1[1:]
                else:
                    new_password = new_password + str(aux)
            print('Your password has been encoded and stored!\n')
        else:
            print('The password should be 8 digits long')
    except ValueError:
        print('The password can only contain numbers')
    return new_password





if __name__ == '__main__':
    main()

