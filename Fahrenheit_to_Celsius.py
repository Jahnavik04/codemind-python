def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
fahrenheit = float(input())
celsius = fahrenheit_to_celsius(fahrenheit)
print("{:.2f}".format(celsius))