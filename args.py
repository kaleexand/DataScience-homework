# def ten_pecent_of_product(x, y, z):
#     return (x * y) * 0.1
#
# print(ten_pecent_of_product(10, 20, 1))
# def ten_pecent_of_product_with_argc(*argc):
#    product = 1;
#    for numb in argc:
#        product = product * numb
#    return product * 0.1
#
# print(ten_pecent_of_product_with_argc(10, 20, 2, 1, 200))

# def func_with_kwargs(**kwargs):
#     print(kwargs)
#
# func_with_kwargs(first = 1, second = 2, third = 3)

# def hello_with_kwargs(**kwargs):
#     if 'name' in kwargs:
#         print('hello {}'.format(kwargs['name']))
#     else:
#         print('hello')
#
#
# hello_with_kwargs(gender = 'male', age = 24, name = 'Jack')
# hello_with_kwargs(gender = 'male', age = 24)

# def hello_with_greeting_and_kwargs(greeting, **kwargs):
#     if 'name' in kwargs:
#         print('{} {}'.format(greeting, kwargs['name']))
#     else:
#         print('{}'.format(greeting))
#
# hello_with_greeting_and_kwargs('Hi', gender = 'male', age = 24, name = 'Jack')
# hello_with_greeting_and_kwargs('Hi', gender = 'male', age = 24)

def func_w(*args, **kwargs):
    print('I would like {} {}'.format(args[0], kwargs['drink']))

func_w('one', 'two', drink = 'coffee')