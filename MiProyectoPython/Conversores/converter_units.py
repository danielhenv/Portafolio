# Simple converter from Celsius to Fahrenheit

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

temp_c = float(input("Enter temperature in Celsius: "))
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C is {temp_f}°F")