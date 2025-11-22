# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

try:
 temperature = float(input("Enter the temperature to convert:"))

except ValueError:
    print("Invalid temperature. Please enter a numeric value.")
    exit()

def convert_to_celsius(fahrenheit):
 return (fahrenheit-32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
 return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

if unit == "C":
    converted = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is equal to {converted:.2f}°F")
elif unit == "F":
    converted = convert_to_celsius(temperature)
    print(f"{temperature}°F is equal to {converted:.2f}°C")
else:
    print("Invalid unit. Please enter C for Celsius or F for Fahrenheit.")


