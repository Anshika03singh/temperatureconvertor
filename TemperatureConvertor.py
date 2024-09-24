def convert_temperature():
    print("Temperature Converter")
    print("1: Celsius to Fahrenheit")
    print("2: Fahrenheit to Celsius")
    print("3: Celsius to Kelvin")
    print("4: Kelvin to Celsius")
    print("5: Fahrenheit to Kelvin")
    print("6: Kelvin to Fahrenheit")
    
    choice = input("Choose an option (1-6): ")

    if choice in ['1', '2', '3', '4', '5', '6']:
        temp = float(input("Enter the temperature: "))

        if choice == '1':
            # Celsius to Fahrenheit
            converted = (temp * 9/5) + 32
            print(f"{temp} °C is {converted} °F")

        elif choice == '2':
            # Fahrenheit to Celsius
            converted = (temp - 32) * 5/9
            print(f"{temp} °F is {converted} °C")

        elif choice == '3':
            # Celsius to Kelvin
            converted = temp + 273.15
            print(f"{temp} °C is {converted} K")

        elif choice == '4':
            # Kelvin to Celsius
            converted = temp - 273.15
            print(f"{temp} K is {converted} °C")

        elif choice == '5':
            # Fahrenheit to Kelvin
            converted = (temp - 32) * 5/9 + 273.15
            print(f"{temp} °F is {converted} K")

        elif choice == '6':
            # Kelvin to Fahrenheit
            converted = (temp - 273.15) * 9/5 + 32
            print(f"{temp} K is {converted} °F")

    else:
        print("Invalid choice! Please select a valid option.")

# Run the converter
convert_temperature()
