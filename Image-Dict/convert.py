from PIL import Image

selected_image = Image.open('image.png')
pix = selected_image.load()
width, height = selected_image.size
output_file = open("output.txt", "a")
output_file.write("[")
resolution = 2

for row in range(0, height, resolution):
    for column in range(0, width, resolution):
        try:
            red, green, blue, alpha = pix[column, row]
        except:
            red, green, blue = pix[column, row]
        print (str(red) + " " + str(green) + " " + str(blue))
        
        #if blue > 0 and green < blue and red < blue:
        if blue < 100 and green > 30 and red < 100:
            output_color = "Green"
            output_file.write("\"" + str(column) + " " + str(row) + " " + output_color + "\", ")
        elif blue < 30 and green < 30 and red < 30:
            output_color = "Black"
            output_file.write("\"" + str(column) + " " + str(row) + " " + output_color + "\", ")
        elif blue < 30 and green > 30 and red > 30:
            output_color = "Yellow"
            output_file.write("\"" + str(column) + " " + str(row) + " " + output_color + "\", ")
output_file.write("]")