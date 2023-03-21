# programme for simple calculator
firstnumber = float(input("Enter firstnumbner:"))
secondnumber = float(input("enter second number:"))
myoperator = str(input("myoperator(+,-,*,/):"))
if myoperator=="+":
    print(firstnumber+secondnumber)
elif myoperator=="-":
    print(firstnumber-secondnumber)
elif myoperator=="*":
    print(firstnumber*secondnumber)
elif myoperator=="/":
    print(firstnumber/secondnumber)
else:
    print("invalid")

