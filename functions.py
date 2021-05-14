# my_list = [1, 2, 3]
#
# my_list.append(4)
# print(my_list)
# my_list.clear()
# print(my_list)

# def print_greeting():
#     '''
#     Print 'Hello' text
#     :return: None
#     '''
#     print('Hello')
# # call the function
# print_greeting()
#
# #receive the description of the function
# help(print_greeting)

# def print_greeting_with_name(name = 'Jack'):
#     '''
#     :param name
#     :return: None
#     '''
#     print("hello " + name + "!")
#
# name = 'Juliya'
# print_greeting_with_name(name)
# help(print_greeting_with_name)
# print_greeting_with_name('Jane')

# def sum_of_two_numbers(a = 0, b = 0):
#     return a + b
# x = sum_of_two_numbers(45, 7)
# print(x)

# def is_hello_in_text(text):
#     if 'hello' in text.lower():
#         return True
#     else:
#         return False
#
# def is_hello_in_text(text):
#     return 'hello' in text.lower()
#
# print(is_hello_in_text('Hello everyone'))

# def is_string_in_text(string, text):
#     return string in text
#
# print(is_string_in_text('he', 'The apple'))
# print(is_string_in_text('hey', 'The apple'))

def greeting_depends_on_gender(name, gender):
    if gender == 'male' :
        print('Hello ' + name + '! You look great!')
        return gender
    elif gender == 'female':
        print('Hello ' + name + '! You are so nice!')
        return gender
    else:
        print('Hello ' + name + '! I\'ve never seen the creature like you!')
        return gender


returned_value = greeting_depends_on_gender('Jack', 'male')
returned_value = greeting_depends_on_gender('Jane', 'female')
returned_value = greeting_depends_on_gender('Ja', 'smale')