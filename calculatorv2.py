a = float(input("Enter First Number => "))
op = str(input("Enter Operation (+, -, *, /, %) => "))
b = float(input("Enter Second Number => "))

if op == "+":
    sum = a + b
    total = str(f"The sum of {a} + {b} is {sum}")
elif op == "-":
    diff = a - b
    total = str(f"The difference of {a} - {b} is {diff}")
elif op == "*":
    mul = a * b
    total = str(f"The multiplication of {a} * {b} is {mul}")
elif op == "/":
    div = a / b
    total = str(f"The division of {a} / {b} is {div}")
elif op == "%":
    mod = a % b
    total = str(f"The module of {a} % {b} is {mod}")
else:
    total = str("Please Enter an Valid Operation.......")

print (total)