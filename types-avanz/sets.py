# set is grouped
first = {1, 1, 2, 2, 3, 3, 4, 5}
print(first)
first.add(6)
print(first)
first.remove(1)
print(first)

second = [3, 4, 5]
second = set(second)
print(first | second)
print(first & second)
print(first - second)
print(first ^ second)
