dict = {'name': 'harsh', 'age': 23, 'color': 'blue'}

print(dict.values())

print(dict.keys())

print(dict.items())

dict.pop('color')
print(dict)

dict.update({'age': 24})

dict.update({'color': 'red'})
print(dict)

dict.setdefault('color', 'voilet')
dict.setdefault('vehicle', 'car')
print(dict)

print(dict.clear())
