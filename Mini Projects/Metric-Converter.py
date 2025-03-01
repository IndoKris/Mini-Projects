print('''
======================================================================================
                             WELCOME TO METRIC & CURRENCY CONVERTER
======================================================================================
''')

choice = 1
while choice == 1:
    opt = int(input('''-------------------------------------------------
| Opt |      From       |       |      To       |
-------------------------------------------------
|  1  |  Centimeter(cm) | --->  | Meter(m)      |
|  2  |  Meter(m)       | --->  | Kilometer(km) |
|  3  |  Meter(m)       | --->  | Feet(ft)      |
|  4  |  Gram(g)        | --->  | Kilogram(kg)  |
|  5  |  Kilogram(kg)   | --->  | Ton(t)        |
|  6  |  Kilogram(kg)   | --->  | Pound(lb)     |
|  7  |  Rupee(INR)     | --->  | Dollar(USD)   |
|  8  |  Dollar(USD)    | --->  | Rupee(INR)    |
-------------------------------------------------

Enter your option: '''))
    if opt == 1:
        unit = float(input('Enter value in Centimeters (cm): '))
        print(f'{unit} cm = {unit / 100} meters')

    elif opt == 2:
        unit = float(input('Enter value in Meters (m): '))
        print(f'{unit} m = {unit / 1000} kilometers')

    elif opt == 3:
        unit = float(input('Enter value in Meters (m): '))
        print(f'{unit} m = {unit * 3.28084} feet')

    elif opt == 4:
        unit = float(input('Enter value in Grams (g): '))
        print(f'{unit} g = {unit / 1000} kilograms')

    elif opt == 5:
        unit = float(input('Enter value in Kilograms (kg): '))
        print(f'{unit} kg = {unit / 1000} tons')

    elif opt == 6:
        unit = float(input('Enter value in Kilograms (kg): '))
        print(f'{unit} kg = {unit * 2.20462} pounds')

    elif opt == 7:
        print("NOTE: 1 USD = 87.5425 INR")
        unit = float(input('Enter amount in Rupees (INR): '))
        print(f'{unit} INR = {unit / 87.5425} USD')

    elif opt == 8:
        print("NOTE: 1 USD = 87.5425 INR")
        unit = float(input('Enter amount in Dollars (USD): '))
        print(f'{unit} USD = {unit * 87.5425} INR')

    else:
        print("Invalid option. Please select a valid conversion.")
        continue

    choice = int(input('Enter 1 to continue or 0 to exit: '))
