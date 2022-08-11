x = 10
y = 9
z = 12

if x > y > z:
  print("Max number:",x)
  print("Min number:",z)
elif x > z > y:
  print("Max number:",x)
  print("Min number:",y)
elif y > x > z:
  print("Max number:",y)
  print("Min number:",z)
elif y > z > x:
  print("Max number:",y)
  print("Min number:",x)
elif z > y > x:
  print("Max number:",z)
  print("Min number:",x)
else:
  print("Max number:",z)
  print("Min number:",y)
