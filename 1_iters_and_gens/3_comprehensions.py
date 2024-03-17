# generator expression
lst = (i * 10 for i in range(1, 3))

for item in lst:
    print(item)


# list comprehension - списковые включения
new_list = [x if x in 'aeiou' else '*' for x in 'apple']

for item in new_list:
    print(item)

a = ''
for letter in new_list:
    a += letter if letter in 'aeiou' else ''

print(a)

# set comprehension
input_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]

set_ = {v for v in input_list if v % 2 == 0}

print(set_)

squares_dict = {x: x ** 2 for x in range(1, 6)}
print(squares_dict)
