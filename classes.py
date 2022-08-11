class Math:
  def sum(self,num1,num2):
    return num1 + num2

  def sub(self,num1,num2):
    return num1 - num2

  def mult(self,num1,num2):
    return num1*num2

  def div(self,num1,num2):
    return num1/num2

math = Math()
print("Sum =" + str(math.sum(5,6)))
print("Sub =" +str(math.sub(11,9)))
print("Div=" +str(math.div(9,3)))
print("Multiplication="+str(math.mult(7,3)))
