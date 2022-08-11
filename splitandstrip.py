message = "Hello World"

print(len(message))

newmessage = message[len(message)-1:len(message)]
print(newmessage)

print(message.replace("o","ö"))

information = "Aysegul Yilmaz 21 İstanbul"
print(information.split()) 

information2 = "    Aysegul Yilmaz 21 İstanbul".strip

name = input("What is your name?")
number1 = input("Number 1 = ?")
number2 = input("Number 2 = ?")
print(int(number1 )+ int(number2))