"""
Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
"""
import math


def filter_num():
    numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
    nums = [i for i in numbers if i <= 0]
    return nums


print(filter_num())

"""
Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

output
[1, 2, 3, 4, 5, 6, 7, 8, 9]
"""


def flatten_list():
    list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
    flist = [num for row in list_of_lists for number in row for num in number]
    return flist


print(flatten_list())

"""
Using list comprehension create the following list of tuples:

[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]
"""


def list_of_tuples():
    tl = [(i, i ** 0, i ** 1, i ** 2, i ** 3, i ** 4, i ** 5) for i in range(11)]
    return tl


print(list_of_tuples())

"""
Flatten the following list to a new list:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output:
[['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
"""


def flatten_countries():
    countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
    flattened_countries = [[country_name.upper(), country_name[:3].upper(), capital.upper()] for
                           [(country_name, capital)] in
                           countries]
    return flattened_countries


print(flatten_countries())
"""
Change the following list to a list of dictionaries:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output:
[{'country': 'FINLAND', 'city': 'HELSINKI'},
{'country': 'SWEDEN', 'city': 'STOCKHOLM'},
{'country': 'NORWAY', 'city': 'OSLO'}]
"""


def change_to_dic():
    countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
    dic = [{'country': country_name.upper(), 'city': city_name.upper()} for [(country_name, city_name)] in countries]
    return dic


print(change_to_dic())

"""
Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

output
['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
"""


def concatenated_strings():
    names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
    cs = [a + ' ' + b for [(a, b)] in names]
    return cs


print(concatenated_strings())
"""
Write a lambda function which can solve a slope or y-intercept of linear functions.
"""

res = lambda angle: math.tan(angle)
print(res(60))
