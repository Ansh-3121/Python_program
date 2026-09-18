#Ask the user for a temperature in Celsius (string input). Convert it to float,then calculate and print temperature in Fahrenheit
# Formula : FahrenheitTemp = (CelsiusTemp ∗ (9/5)) +32

celsius=input("Enter Temperature : ")
celsius=float(celsius)
FahrenheitTemp =(celsius*(9/5)) +32
print(FahrenheitTemp)
print(type(celsius))

