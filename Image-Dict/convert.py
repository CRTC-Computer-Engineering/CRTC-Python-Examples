from PIL import Image

selected_image = Image.open('image.png')
pix = selected_image.load()
width, height = selected_image.size
output_file = open("output.txt", "a")
output_file.write("[")
for row in range(height):
    for column in range(width):
        red, green, blue, alpha = pix[column, row]
        print (str(red) + str(green) + str(blue))
        
        if blue > 0:
            output_color = "Blue"
        else:
            output_color = "White"
        output_file.write("\"" + str(column) + " " + str(row) + " " + output_color + "\", ")
output_file.write("]")