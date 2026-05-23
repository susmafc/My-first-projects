# Python weight converter
while True:
    while True:
        try:
            weight = float(input("Enter your weight: "))
            break
        except ValueError:
            print("Please enter a number.")
    unit = input("Kilograms or Pounds? (K/P): ").upper()
    if unit == "K":
        weight = weight * 2.205
        unit = "Lbs"
        print(f"Your weight is {round(weight, 2)} {unit}.")
    elif unit == "P":
        weight = weight / 2.205
        unit = "Kgs."
        print(f"Your weight is {round(weight, 2)} {unit}.")
    else:
        print(f"{unit} is not a valid unit.")
    again = input("Would you like to select another weight? (yes/no): ")
    if again.lower() == "no":
        break
