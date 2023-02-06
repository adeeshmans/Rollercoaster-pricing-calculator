print("Welcome to the rollercoaster!")
# Getting the input
height = int(input("What is your height in cm? "))
bill = 0

#Logic
if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
    
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  elif age >=45 and age <=55:
    print("Have a free ride on us!")
  else:
    bill = 12
    print("Adult tickets are $12.")
  
    # Get input if user wants to add a photo to the ticket and add $3v regardless of age.
 wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3
  print(f"Your final bill is ${bill}")

else:
  print("Sorry, you have to grow taller before you can ride.")
