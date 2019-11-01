"""
This program made by Joe S
"""

servings = -1 # Set the servings to a null value
shopping_list = ["mixed greens", "blueberries", "walnuts"] # Create a list of all the things we need to shop for

object_list = [] # Create an empty list where we will store objects

class ingredient(): # This class defines the ingredient object
    def __init__(self, name, qty): # This init function takes the name and qty, and asigns it to the object in question
        self.name = name 
        self.qty = qty
    def list_total(self): # This function lists the content of the current item in a human readable way
        print("Total ounces of " + self.name + ": " + str(float(self.qty) * servings))

for listitem in shopping_list: # For every item on our shopping list
    print("Enter ingredient 1: " + str(listitem))
    object_list.append(ingredient(listitem, input("Ounces of " + str(listitem) + ": "))) # Create a new object, add it to our list using inputs from the user

servings = float(input("Enter total number of servings: ")) # Ask the user for the total number of servings
print("") # Print a blank line
for item in object_list: # For every object in our object list
    item.list_total() # call that objects respective list_total function