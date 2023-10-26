welcome_msg= '''***Welcome to Temperature Converter***'''
options = '''>>>Convert - 
1.Degree Celsius to Degree Fahrenheit
2.Degree Fahrenheit to Degree Celsius
3.Degree Celsius to Kelvin
4.Kelvin to Degree Celsius
5.Degree Fahrenheit to Kelvin
6.Kelvin to Degree Fahrenheit
7.Quit'''
print(welcome_msg)
while True:
    print(options)
    x = input("Enter the options above to convert temperature - ")
    y = input("Enter Temperature to convert - ")
    print(' ')
    if x == '1':
        result = (float(y) *( 9/5)) + 32
        print(f"Temperature of {y}°C is equal to {result}°F")
    elif x == '2':
        result = (float(y)- 32) * (5/9)
        print(f"Temperature of {y}°F is equal to {result}°C")
    elif x == '3':
        result = float(y) + 273.15
        print(f"Temperature of {y}°C is equal to {result}K")
    elif x == '4':
        result=float(y) - 273.15 
        print(f"Temperature of {y}K is equal to {result}°C")
    elif x == '5':
        result = (float(y)- 32) * (5/9) + 273.15
        print(f"Temperature of {y}°F is equal to {result}K")
    elif x == '6':
        result = (float(y) - 273.15) * (9/5) + 32
        print(f"Temperature of {y}K is equal to {result}°F")
    elif x == '7':
        print("Thank you for using our converter, Have a nice day!")
    print('*****************************************************************************************************************************************')