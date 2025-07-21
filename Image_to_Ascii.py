import cv2

#dic_ascii = {(0,25) : '@', (26, 50) : '%', (51, 75) : '#', (76, 100) : '*', (101,125) : '+', (126,150) : '=', (151, 175) : '-', (176, 200) : ':', (201, 225) : '.', (226, 255) : ' '}

dic_ascii = {(0,25) : ' ', (26, 50) : '.', (51, 75) : ':', (76, 100) : '-', (101,125) : '=', (126,150) : '+', (151, 175) : '*', (176, 200) : '#', (201, 225) : '%', (226, 255) : '@'}

def get_char(px):
    for (min, max), char in dic_ascii.items():
        if px >= min and px <= max:
            return char

image = cv2.imread("Chatte_Maine_Coon_Crop.jpg")

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

image_gray = cv2.resize(image_gray, (400, 160))

line = ""

height, width = image_gray.shape

for i in range(height):
    line += "\n"
    for j in range(width):
        line += get_char(image_gray[i][j])

print(line)

#cv2.imshow("Mon Image", image_gray)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
