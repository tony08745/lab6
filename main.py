# Anthony Taylor

# Main of the program, controls the loop of the program
new_password = ''


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
    global new_password
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


def decode():
    global new_password
    password_decode_list = []
    # convert to int and subtract 3 from every element of string
    for i in new_password:
        if int(i) - 3 < 0:
            e = int(i) + 10 - 3
        else:
            e = int(i) - 3
        password_decode_list.append(e)
    # join list of integers into string
    password_decode = ''.join(str(n) for n in password_decode_list)
    print(f"The encoded password is {new_password}, and the original password is {password_decode}\n")


if __name__ == '__main__':
    main()
