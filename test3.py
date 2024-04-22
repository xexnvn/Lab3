#
# Eva
# Calculator
# 

# Define function to calculate two numbers
def cal(x1, x2, op): 
    if op == "+":
       sum = int(x1) + int(x2)
    elif op == "-":
       sum = int(x1) - int(x2)
    elif op == "*":
       sum = int(x1) * int(x2)
    elif op == "/":
       sum = int(x1) / int(x2)

# 1. Input
x1 = input("Type x1: ")
x2 = input("Type x2: ")
op = input("Type operator: ")

# 2. Process
sum = cal(x1, x2, op)

# 3. Print result
print(f"Sum: {sum}")