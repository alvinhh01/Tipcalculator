# What is the total bill?
total_bill = float(input("What is the total bill?"))

# What is the tip percentage?
tip_percentage = float(input("What is the tip percentage?"))

# How many people are splitting the bill?
splitting_bill = int(input("How many people are splitting the bill?"))

# Calculate total bill plus tips
total_bill_plus_tips = total_bill + (total_bill * tip_percentage / 100)

# Display the total bill plus tips
print(f"Your total bill plus tips is {total_bill_plus_tips:.2f}")

# Calculate bill per person
bill_per_person = total_bill_plus_tips / splitting_bill

# Display the bill per person
print(f"The bill per person is {bill_per_person:.2f}")
