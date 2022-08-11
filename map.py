numbers = [1,2,3,4,5]

numbersSquare = list(map(lambda x: x**2,numbers))

#for number in numbers:
#  numbersSquare.append(number*number)

print(numbersSquare)

numbers2 = [10,20,30,40]

numbersDivide = list(map(lambda x : x/2,numbers2))

numbersQuarter = list(map(lambda x: x/4,numbers2))

print(numbersDivide)
print(numbersQuarter)