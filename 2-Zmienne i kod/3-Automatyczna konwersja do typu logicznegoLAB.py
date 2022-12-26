def display_options(lista):
    for i in range(len(lista)):
        print(f'{i+1} - {lista[i]}')
    _choice = input('Select option above or press enter to exit\n')
    return _choice


if __name__ == '__main__':
    options = ['load data', 'export data', 'analyze & predict']
    choice = 'x'
    while choice:
        choice = display_options(options)
        if choice:
            try:
                choice_num = int(choice)
                if choice_num in (1, 2, 3):
                    print(choice, ' - ', options[choice_num - 1])
                    break
                else:
                    print('Dokonano złego wyboru\n')
            except:
                print('Wprowadź liczbę\n')
        else:
            print('Do widzenia...')
