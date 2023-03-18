users = users = [['user', 3], ['user', 1], ['user', 2]]
# users.sort(key=lambda x: x[1])
# print(users)

# names = []
# for name in users:
#     names.append(name[0])
# print(names)

# map
# names = [user[0] for user in users]
# filter
# names = [user for user in users if user[1] > 2]

# names = [user[0] for user in users if user[1] > 2]

# names = list(map(lambda user: user[0], users))
names = list(filter(lambda user: user[1] > 2, users))

print(names)
