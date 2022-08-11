class Person:
  def __init__(self,firstName,lastName,age,weight,height):
    self.firstName = firstName
    self.lastName = lastName
    self.age = age
    self.weight = weight
    self.height = height

person1 = Person("Aysegul","Yilmaz",21,57,161)
print(person1.firstName)
print(person1.lastName)
print(person1.age)
print(person1.weight)
print(person1.height)

class Worker:
  def __init__(self,salary):
    self.salary = salary

class Customer:
  def __init__(self,creditCardNo):
    self.creditCardNo= creditCardNo

ahmet = Worker(1541)
mehmet = Customer(123456789)

print(ahmet.salary)
print(mehmet.creditCardNo)
