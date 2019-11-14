from PIL import Image
import numpy as np
import os

if os.path.exists("output.py"): # If an existing file exists
    try:
        os.remove("output.py") # Remove it
    except:
        "Unable to remove file!"
else: # Otheriwise
    print("Creating empty file") # We're good!

selected_image = Image.open('image.png') # Could be upgraded to be an input
pix = selected_image.load() # Load the image
width, height = selected_image.size # Get the width and height
output_file = open("output.py", "a") # Set the output file
output_file.write("image_list = [") # Write the first char
resolution = int(input("Set your res (default is 2): ")) # Ask the user for the res

list_of_colors = [[0,0,0],[0,0,255],[150,75,0],[0,255,255],[255,215,0],[128,128,128],[0,255,0],[75,0,130],[255,165,0],[251,96,127],[160,32,240],[255,0,0],[143,0,255],[255,255,255],[250,255,0]]
list_of_names = ["black", "blue",   "brown",   "cyan",     "gold",     "gray",       "green",  "indigo",  "orange",   "pink",      "purple",    "red",    "violet",   "white",      "yellow"]

def closest(colors,color):
    colors = np.array(colors) # all the colors are now an array
    color = np.array(color) # the current color is another array
    distances = np.sqrt(np.sum((colors-color)**2,axis=1)) # get all the distances 
    index_of_smallest = np.where(distances==np.amin(distances)) # find the array with the smallest distance
    smallest_distance = colors[index_of_smallest] # Get that distance
    return smallest_distance #return the closest color

for row in range(0, height, resolution):
    for column in range(0, width, resolution):
        try:
            red, green, blue, alpha = pix[column, row]
        except:
            red, green, blue = pix[column, row]
        #print (str(red) + " " + str(green) + " " + str(blue))
        
        #print([red, green, blue])
        closest_color = ((closest(list_of_colors, [red,green,blue])).tolist())[0]
        #print(closest_color)
        
        index_in_array = 0
        for i in list_of_colors:
            #print(i)
            if i == closest_color:
                output_color = list_of_names[index_in_array]
            index_in_array = index_in_array + 1
            
        print("Current Color: " + str(output_color) + ", Current line: " + str(row) + "/" + str(height) + "   ", end="\r")
        if(output_color != "white"):
            output_file.write("\"" + str(column) + " " + str(row) + " " + output_color + "\", ")
output_file.write("""]

# This code autogenerated by joe
import random
shuffleDraw = False # Change this to true to enable shuffled draw
if shuffleDraw:
    random.shuffle(image_list)

speed(0) # Go at max speed
resolution = """ + str(resolution) + """ # Set to res of image
current_progress = 0.0
last_progress = 0
print("Starting...")
for current_pixel in image_list: # For every pixel
    split_pixel = current_pixel.split() # split into values on " "
    x = split_pixel[0] # The first value is x
    y = 400 - int(split_pixel[1]) # The second value is y
    selectColor = split_pixel[2] # The third value is color
    
    current_progress = current_progress - 1 # Calculate Percentage
    percentage = (100 * float(current_progress)/float(len(image_list))) * -1
    if(last_progress != int(percentage)):
        print("Progress: " + str(int(percentage)) + "%")
        last_progress = int(percentage)
    
    penup() # Bring up the cursor
    setposition(int(x) - 200, int(y) - 200) # Go to the pixel location (tranformed by 200)
    pendown() # Begin drawing
    color(selectColor) # Set the color
    pensize(resolution * 2) # Set the pen size
    forward(1) # Go forward
print("Done") # Done!
""")
