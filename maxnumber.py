number1 = int(input("Please  enter first number:"))
print(number1)

number2  = int(input("Please enter second number:"))
print(number2)

number3 = int(input("Please enter third number:"))
print(number3)

if number1>number2>number3:
  print(number1)

elif number1>number3>number2:
  print(number1)
  
elif number2>number1>number3:
  print(number2)

elif number2>number3>number1:
  print(number2)

elif number3>number1>number2:
  print(number3)
  
else:
  print(number3)