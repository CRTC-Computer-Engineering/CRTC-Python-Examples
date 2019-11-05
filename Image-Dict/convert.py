from PIL import Image

selected_image = Image.open('image.png')
pix = selected_image.load()
width, height = selected_image.size
output_file = open("output.txt", "a")
output_file.write("[")
for row in range(0, height, 4):
    for column in range(0, width, 4):
        red, green, blue, alpha = pix[column, row]
        print (str(red) + " " + str(green) + " " + str(blue))
        
        #if blue > 0 and green < blue and red < blue:
        if blue < 30 and green < 30 and red < 30:
            output_color = "Blue"
            output_file.write("\"" + str(column) + " " + str(row) + " " + output_color + "\", ")
output_file.write("]")