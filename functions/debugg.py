def large(text):
    result = 0
    for _ in text:
        result += 1
    return result


print("--------------------------------")
res = large('Hello, world')
print(res)
