def degree(a, b):
    if a.lower() == "cel":
        fahrenheit = (b - 32) * (5 / 9)
        fahrenheit = float('{:.2f}'.format(fahrenheit))
        return f'tempercha in Fahrenheit = {fahrenheit}'

    elif a.lower() == "far":
        celsius = (b - 32) / 2 + (1 / 10)
        celsius = float('{:.2f}'.format(celsius))
        return f'tempercha in celsius = {celsius}'

    else:
        return f'please write correct type'


print(degree('far', 243))