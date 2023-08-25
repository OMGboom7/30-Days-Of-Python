# Declare a function add_two_numbers. It takes two parameters and it returns a sum.
import math


def add_two_numbers(num1, num2):
    total = num1 + num2
    return total


print(add_two_numbers(1, 55))


# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(radius):
    area = math.pi * radius * radius
    return area


print(area_of_circle(10))


# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments.
# Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*args):
    total = 0
    for i in args:
        if type(i) == int or type(i) == float:
            total += i
        else:
            return 'not numbers'
    return total


print(add_all_nums(1, 55, 66))


# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32.
# Write a function which converts °C to °F, convert_celsius_to_fahrenheit.
def convert_celsius_to_fahrenheit(celsius):
    if type(celsius)!=int and type(celsius)!=float:
        return 'not a number'
    else:
        fahrenheit = (celsius * 9 / 5) + 32
        return fahrenheit


print(convert_celsius_to_fahrenheit(10))
# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
# Write a function called calculate_slope which return the slope of a linear equation
# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
