import cv2

video = input("Entrez le nom de la video : ")

video += ".mp4"

print(video)

dic_ascii = {(0,25) : ' ', (26, 50) : '.', (51, 75) : ':', (76, 100) : '-', (101,125) : '=', (126,150) : '+', (151, 175) : '*', (176, 200) : '#', (201, 225) : '%', (226, 255) : '@'}

cap = cv2.VideoCapture(video)

def get_char(px):
        for (min, max), char in dic_ascii.items():
            if px >= min and px <= max:
                return char

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    line = ""

    base_height, base_width = gray.shape

    gray = cv2.resize(gray, (base_width//10, base_height//13))

    height, width = gray.shape

    for i in range(height):
        line += "\n"
        for j in range(width):
            line += get_char(gray[i][j])

    print(line)
