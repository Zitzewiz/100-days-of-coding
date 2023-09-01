#1. Create a greeting for your program.
print("Welcome to band name generator.")
#2. Ask the user for the city that they grew up in.
city = input("Which city were you born in? \n")
#3. Ask the user for the name of a pet.
pet = input("What name is your pet? \n")
#4. Combine the name of their city and pet and show them their band name.
band_name = city + " " + pet
#5. Make sure the input cursor shows on a new line:
print(f'Maybe name your band "The {band_name}s"?')
# Solution: https://replit.com/@appbrewery/band-name-generator-end