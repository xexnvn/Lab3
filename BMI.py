# Eva
# BMI Calculator
# Calculate BMI

print("BMI Calculator")

while True:
    # 1. Input
    x1 = float(input("Enter your weight in kilograms: "))
    x2 = float(input("Enter your height in meters   : "))

    # 2. Process
    BMI = x1/(x2**2)
    
    # 3. Output
    print(f"Your BMI is: {BMI}")

    res = input("Continue? (yes/no): ")
    if res == "no":
        break;