def show_progress(how_many, character='*'):
    for i in range(how_many):
        print(character, end='')
    print()


show_progress(10)
show_progress(15)
show_progress(30)
show_progress(10, '-')
show_progress(15, '+')
