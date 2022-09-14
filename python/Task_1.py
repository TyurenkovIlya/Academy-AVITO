def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


def step2_umbrella():
    print(
        'Отлично! '
        'Можно погулять в парке и попрыгать по лужам.'
    )


def step2_no_umbrella():
    print(
        'Ничего страшного! '
        'У утки непромокаемые перья'
    )


if __name__ == '__main__':
    step1()
