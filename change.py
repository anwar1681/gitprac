def changetemp():
    temp = input('enter temprature  f or c: ')
    if temp == f:
        F = int(input('enter temperature if farenheit: '))
        c = (F-32)*5/9
        print(f'The centi equivalent of {F} F is: {c} C')
    elif temp == c:
        C = int(input('temperature if centigrade: '))
        f = C*9/5 + 32
        print(f'The farenheit equivalent of {C} C is: {f} F')
    else:
        print('enter temp f or c')

changetemp()
    