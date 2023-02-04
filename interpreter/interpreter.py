exp = input("Expression: ")
x, y, z = exp.split()
divide = float(x)/float(z)
multiply = float(x)*float(z)
add = float(x)+float(z)
minus = float(x)-float(z)
if y == "*":
    print(multiply)
elif y == "/":
    print(divide)
elif y == "+":
    print(add)
elif y == "-":
    print(minus)
else:
    exp = input("Expression: ")