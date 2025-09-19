import math
def calculate_equation():
    try:
        description = input('значение x:')
        x = float(description)
        e = math.e

        y= math.acos(1-x**2)+math.asin(1-x**2)/math.sin(1-2*x**2)
        return f'answer is: {round(y , 5)}'

    except ValueError:
        return "Error, please enter "

print(calculate_equation())
