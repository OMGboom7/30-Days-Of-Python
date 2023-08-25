import string
from random import randint


# Writ a function which generates a six digit/character random_user_id.
def random_user_id():
    character = string.ascii_letters + string.digits
    random_id = ''
    for i in range(6):
        random_id += character[randint(0, len(character) - 1)]
    return random_id


print('random_user_id: ' + random_user_id())


# Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters, but it takes
# two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs
# which are supposed to be generated.
def user_id_gen_by_user(number_of_characters, number_of_ids):
    character = string.ascii_letters + string.digits
    random_ids=[]
    for num in range(number_of_ids):
        random_id=''
        for i in range(number_of_characters):
            random_id += character[randint(0, len(character) - 1)]
        random_ids.append(random_id)
    return random_ids

print(user_id_gen_by_user(10, 5))
