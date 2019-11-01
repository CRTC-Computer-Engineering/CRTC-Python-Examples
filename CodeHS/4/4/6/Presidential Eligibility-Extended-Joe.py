"""
This program made by Joe
"""
userage = bool(int(input("Age: ")) >= 35)
user_birthplace = bool(input("Born in the US? (Yes/No): ") == "Yes")
user_residency = bool(int(input("Years of Residency: ")) >= 14)

if (userage and user_birthplace) and user_residency:
    print("You are eligible to run for president.")
else:
    print("You are not eligible to run for president.")
    
if userage != True:
    print("You are too young. You must be at least 35 years old.")
if user_birthplace != True:
    print("You must be born in the U.S. to run for president.")
print(user_residency)
if user_residency != True:
    print("You have not been a resident for long enough.")