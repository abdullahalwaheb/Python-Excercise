# ------ completed/submitted ------

#---------------------------What day is it-----------------------------
day = int(input("day (0-2)? "))
if day == 0:
  print("It is Sunday")
elif day == 1:
  print("It is Monday")
else:
  print("It is Funday")


#----------------------Temperature calculator-------------------------
temp = float(input("What is today's temperature? "))
celsius = (temp - 30) / 2
print("Today's temperature is ", temp," F and ", celsius," in celsius")


#---------------------------Tip Calculator----------------------------
bill = 0
tip = 0.0
total = 0
rate = ""

def calcTotal():
  while True:
    try:
      bill = float(input("What is your total?\n$"))
      rate = input("How would you rate us? Good,Fair or Crap?\n")
      if (rate == "good" or rate == "Good"):
        tip = 0.20
      elif (rate == "fair" or rate == "Fair"):
        tip = 0.10
      elif (rate == "crap" or rate == "Crap"):
        tip = 0.05
      else:
        print("invalid value")

      total = bill + bill * tip
      print("Your total is: $",total)

    except ValueError:
      print("Your bill has to be a number")
    else:
      return bill
      break

calcTotal()


#--------------------------Loop Practice------------------------------
i = 0
while i < 15:
  i += 1
  print(i)

#--------------------------How many coins?------------------------------
coins = 0

answer = input("Do want some coins? ")
while (answer == "yes" or answer == "Yes"):
  coins += 1
  answer = input("You have %s coin, want another one? " % coins)
  if (answer == "no" or answer == "No"):
    print("see ya")
    break

