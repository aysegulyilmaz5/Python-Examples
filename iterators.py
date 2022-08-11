cities = ["Ankara","Istanbul","Izmır"]

iterator = iter(cities)

print(next(iterator))
print(next(iterator))
print(next(iterator))

#instead of
for city in cities:
  print(city)
