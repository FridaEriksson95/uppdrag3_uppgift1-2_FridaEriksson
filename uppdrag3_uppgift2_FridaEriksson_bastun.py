#Clear screen
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
#Conversion from Fahrenheit to Celsius    
def fahr_to_cel(fahr):
    celsius = (fahr - 32) * 5 / 9
    return round(celsius)

#Opening
print("Welcome to Sweden! Let's get our sauna ready for you when you've arrived!\nWe can provide any degrees between 82 and 87 Celsius.\n")

#Users input on Fahrenheit    
while(True): 
    fahr_input = int(input("Put in how many Fahrenheit you wish to have: "))
    celsius_result = fahr_to_cel(fahr_input)
#If the temperature is less than 82 - too cold
    if celsius_result < 82:
        print("That's too cold!")
        input("Press Enter to try again..")
        clear_screen()
#If the temperature is more than 87 - to hot        
    elif celsius_result > 87:
        print("That's too hot!")
        input("Press Enter to try again..")
        clear_screen()
#If the temperature is between 82 and 87 - answer and exit       
    else:
        clear_screen()
        print("The temperature is now set for", celsius_result, "celsius and will be ready for you when you arrive!\n")
        input("Press Enter to exit..")
        break

#Andra försök
#def fahr_to_cel(fahr):
    #celsius = (fahr - 32) * 5 / 9
    #return round(celsius)  # Round to the nearest whole number

#while True:
    #fahr_input = int(input("Skriv in Fahrenheit (82-87): "))
    #if 82 <= fahr_input <= 87:
    #    break
    #else:
     #   print("Invalid input. Please enter a temperature between 82 and 87.")

#celsius_result = fahr_to_cel(fahr_input)
#print("Temperature in Celsius:", celsius_result)

#input("Press Enter to exit")

#    try:
#        celsius_result < 82:
#        print("That's too cold!n")
#        celsius_result > 87:
#        print("That's too hot!\n")
#        input("Put in how many Fahrenheit you wish to have: ")
#    except:
#        print("The temperature is now set for", celsius_result, ("celsius and will be ready for you when you arrive.\n"))
#        input("Press Enter to exit..")
#        break