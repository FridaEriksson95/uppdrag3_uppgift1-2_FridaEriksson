#conversion from Fahrenheit to Celsius
def fahr_to_cel(fahr):
    celsius = (fahr - 32) * 5 / 9
    return round(celsius)

#Users input on Fahrenheit
fahr_input = int(input("Skriv in Fahrenheit: "))

#The convertet answer from Fahrenheit to Celsius
celsius_result = fahr_to_cel(fahr_input)
print("Temperatur i Celsius:", celsius_result, ("grader."))

#Exit
input("Tryck Enter för att avsluta..")