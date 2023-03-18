numbers = (1, 2, 3) + (4, 5, 6)
print(numbers)

point = tuple([1, 2])
print(point)

less_number = numbers[:2]
print(less_number)

first, second, *other = numbers
print(first, second, other)
for n in numbers:
    print(n)

# numbers[0] = 6 not

number_list = list(numbers)
number_list[0] = 'changed'
print(number_list)
