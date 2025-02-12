print("Welcome to the tip calculator")

# Generate user input
bill = float(input("What was the total bill? "))

tip =  int(input("How much tip will you like to give? 10, 12, 0r 15? "))

number_people = int(input("How many people to split the bill? "))

# Calulate the total bill 
total = bill * (1+tip/100)

amount_per_person = round(total/number_people, 2)

# print out total bill to be paid by each person

print(f"Each person should pay: ${amount_per_person}")
