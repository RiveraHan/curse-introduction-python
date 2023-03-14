"""Methods string"""

animal = ' happy maCAco '
print(animal.upper())
print(animal.lower())
print(animal.strip().capitalize())
print(animal.title())
print(animal.lstrip())
print(animal.rstrip())
print(animal.find('happy'))
print(animal.find('feliz'))
print('happy' in animal)
print('happy' not in animal)
print(animal.replace('maCAco', 'monkey'))
