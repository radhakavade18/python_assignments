# Celcious to fahrenheit converter
# Accept temperature in celcious and convert it into Fahrenhiet using the formula:
# F = (C * 9/5) + 32
# Input - 25
# Output - 77.0

def TemperatureConverter(value):
    F = (value * (9/5)) + 32
    print("Temperature in Faherenheit is", F)

def main():
    print("Enter temperature into celcious")
    no = int(input())

    TemperatureConverter(no)

if __name__ == "__main__":
    main()