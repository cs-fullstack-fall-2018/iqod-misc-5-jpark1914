answer = input("Do you want to quit yes or no? \n").lower();
really = 'really'
while answer != 'yes' or answer != 'y' or answer != 'no' or answer != 'n':
    if answer == 'yes' or answer == 'y':
        print('Alright, good bye!')
        break
    elif answer == 'no' or answer == 'n':
        answer = input('Are you sure? Yes or No \n')
        if answer == 'yes' or answer == 'y':
            print('Alright, goodbye!')
            break
        elif answer == 'no' or answer == 'n':
            while answer == 'no' or answer == 'n':
                print('Are you %s sure' %really)
                really += ' really'
                answer = input("Yes or No \n")
                if answer == 'yes' or answer == 'y':
                    print('Alright, goodbye!')
                    break
    else:
        print('Not a valid answer.')
        answer = input('Input "yes / y" or "no / n" \n')
        if answer == 'yes' or answer == 'y':
            print('Alright, goodbye!')
            break
        elif answer == 'no' or answer == 'n':
            while answer == 'no' or answer == 'n':
                print('Are you %s sure' %really)
                really += ' really'
                answer = input("Yes or No \n")
                if answer == 'yes' or answer == 'y':
                    print('Alright, goodbye!')