numbers = [1, 2, 3, 4, 5, 6, 7]

first, sequent, third, four, five, six, seven = numbers
first, *others = numbers
first, sequent, *others, ultimate = numbers

print(first, sequent, third)
print(first)
print(others)
print(first, sequent)
print(first, others)
