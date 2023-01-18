# generator function
def squares(start, stop):
    for i in range(start, stop):
        # yield keyword is used!
        yield i * i


generator = squares(1, 10)

print(next(generator))
print(next(generator))
# print(next(generator))

# generator expression
lst = (i * 10 for i in range(1, 3))

for item in lst:
    print(item)

for item in lst:
    print(item + 1)

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
