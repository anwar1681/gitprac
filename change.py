def changetemp():
    temp = input('enter temprature f or c: ')
    if temp == 'f':
        F = int(input('enter temperature if farenheit: '))
        c = round((F-32)*5/9,2)
        print(f'The centi equivalent of {F} F is: {c} C')
    elif temp == 'c':
        C = int(input('temperature if centigrade: '))
        f = round(C*9/5 + 32,2)
        print(f'The farenheit equivalent of {C} C is: {f} F')
    else:
        print('enter temp f or c')

changetemp()
    