# Python Temperature Converter

while True:
    while True:
            unit = input("Is the temperature in Celsius or Fahrenheit? (C/F): ").upper()
            if unit not in ["C", "F"]:
                print("Please enter either C or F")
                continue
            break
    while True:
        try:
            temp = float(input("Enter your temperature: "))
            if unit == "C":
                temp = round((9 * temp) / 5 + 32, 1) # Fahrenheit convert
                print(f"The temperature in Fahrenheit is: {temp}°F")
            elif unit == "F":
                temp = round((temp - 32) * 5 / 9 , 1) # Celsius convert
                print(f"The temperature in Celsius is: {temp}°C")
        except ValueError:
            print("Please enter a valid number")
            continue
        break
    again = input("Would you like to convert another temperature? (yes/no): ")
    if again.lower() == "no":
        break