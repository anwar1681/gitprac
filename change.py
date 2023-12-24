while True:

    temp = input('enter temprature f or c, else to exit: ')
    if temp == 'f':
        F = int(input('enter temperature in farenheit: '))
        c = round((F-32)*5/9,2)
        print(f'The centi equivalent of {F} F is: {c} C')
    elif temp == 'c':
        C = int(input('enter temperature in centigrade: '))
        f = round(C*9/5 + 32,2)
        print(f'The farenheit equivalent of {C} C is: {f} F')
    else:
        print('you entered temp other than f or c,\ntherefore exiting this snippet')
        break
    