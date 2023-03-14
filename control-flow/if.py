age = 27

if age > 17:
    print('You can watch the movie only today')

elif age > 60:
    print('You can watch the movie always')
else:
    print('You can not watch the movie')

msg = 'Is old' if age > 17 else 'is young'
print(msg)

if 15 <= age <= 65:
    print('You can come in the pool')


for num in range(5):
    print(num, num * 'Hanzell Rivera')
    if num == 29:
        print('Hello', num)
        break
else:
    print('No ;(')

num = 1
while num < 100:
    print(num)
    num *= 2
