print("Welcome to the Tip Calculator!")

bill = float(input("What was the total bill? $ "))
tip = int(input("How much tip would you like to give? 10%, 12% or 15%? "))
people = int(input("How many people to split the bill? "))

tip_total = bill * (tip / 100)

bill_with_tip = bill + tip_total

per_person = round(bill_with_tip / people, 2)
print(f"Each person should pay $ {per_person}.")



# multiply the number with the percentage number divided by 100