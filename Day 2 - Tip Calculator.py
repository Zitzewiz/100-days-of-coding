print("Welcome to the tip calculator.")
runagain = "Y"

while runagain == "Y":

  bill = float(input("How high was the total bill to split?\n"))
  tip = int(input("How much percent do you want to tip?\n"))/100
  persons = int(input("How many persons were involved?\n"))
  
  bill_pp = bill * (1+tip) / persons
  #bill_pp_rounded = round(bill_pp,2)
  bill_pp_rounded = "{:.2f}".format(bill_pp)
  print(f"Each person must pay {bill_pp_rounded}€.")

  runagain = input("Do you want to run again? Y/N \n")