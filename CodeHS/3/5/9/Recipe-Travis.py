ingredient_one=input("Enter ingredient 1: ")
ingredient_one_weight=float(input("Ounces of " + str(ingredient_one) + ": "))
ingredient_two=input("Enter ingredient 2: ")
ingredient_two_weight=float(input("Ounces of " + str(ingredient_two) + ": "))
ingredient_three=input("Enter ingredient 3: ")
ingredient_three_weight=float(input("Ounces of " + str(ingredient_three) + ": "))
number_servings=int(input("number of servings: "))
print "Total ounces of " + str(ingredient_one) + ": " + str((float(ingredient_one_weight)*float(number_servings)))
print "Total ounces of " + str(ingredient_two) + ": " + str((float(ingredient_two_weight)*float(number_servings)))
print "Total ounces of " + str(ingredient_three) + ": " + str((float(ingredient_three_weight)*float(number_servings)))