temperature = float(input("Temperature: "))
unit = input("Unit (C/F): ").strip().upper()

if unit == "C":
    print("Fahrenheit:", temperature * 9 / 5 + 32)
elif unit == "F":
    print("Celsius:", (temperature - 32) * 5 / 9)
else:
    print("Please enter C or F.")
