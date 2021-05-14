raibow_colors = {'red', 'orenge', 'yellow', 'green', 'blue', 'indigo', 'violet'}
print(raibow_colors)
print(type(raibow_colors))

empty_set = set()
print(empty_set)
print(type(empty_set))

number_list = [1, 2, 43]
text_tuple = ('hi', 'age', 'son')
set_from_list = set(number_list)
set_from_tuple = set(text_tuple)

set_from_list.add(77)
set_from_tuple.add('hello')
set_from_list.add(77)
set_from_tuple.add('hello')
print(set_from_tuple)
print(set_from_list)

set_from_list.pop()
set_from_list.remove(43)
print(set_from_list)
set_from_list.discard(43)
#set_from_list.remove(43)