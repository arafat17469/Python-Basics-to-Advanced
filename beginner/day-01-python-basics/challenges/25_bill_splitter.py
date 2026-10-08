bill = float(input("Bill amount: "))
people = int(input("Number of people: "))
tip = float(input("Tip percentage: "))
total = bill + bill * tip / 100
print(f"Each person pays: {total / people:.2f}")
