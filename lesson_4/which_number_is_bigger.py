x = float(input('Input number x='))
y = float(input('Input another number y='))

if not x > y:
    if x == y:
        print(f'{x} and {y} are equal!')
    else:
        print(f'{x} is lesser than {y}')
else:
    print(f'{x} is greater than {y}')