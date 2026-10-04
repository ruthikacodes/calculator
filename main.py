a=float(input("First number:   "))
operation=input("Operation(+, -, *, /):")
b=float(input("Second number:   "))

if operation=="+":
    result=a+b
elif operation=="-":
    result=a-b
elif operation=="*":
    result=a*b
elif operation=="/":
    if b==0:
        result="Error: Division by zero"
    else:
        result=a/b
else:
    result="Error: Invalid operation"

print("Result:", result)