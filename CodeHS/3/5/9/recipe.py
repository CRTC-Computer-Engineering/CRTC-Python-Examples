"""
This program made by Joe S
"""

servings = -1
shopping_list = ["mixed greens", "blueberries", "walnuts"]

object_list = []

class ingredient():
    def __init__(self, name, qty):  
        self.name = name 
        self.qty = qty
    def list_total(self):
        print("Total ounces of " + self.name + ": " + str(float(self.qty) * servings))

for listitem in shopping_list:
    print("Enter ingredient 1: " + str(listitem))
    object_list.append(ingredient(listitem, input("Ounces of " + str(listitem) + ": ")))

servings = float(input("Enter total number of servings: "))
print("")
for item in object_list:
    item.list_total()