import cv2
import numpy as np 

cap = cv2.VideoCapture('voiture_rouge.mp4')

dic_ascii = {(0,25) : 'tiles/tile10.jpeg', (26, 50) : 'tiles/tile9.jpeg', (51, 75) : 'tiles/tile8.jpeg', (76, 100) : 'tiles/tile7.jpeg', (101,125) : 'tiles/tile6.jpeg', (126,150) : 'tiles/tile5.jpeg', (151, 175) : 'tiles/tile4.jpeg', (176, 200) : 'tiles/tile3.jpeg', (201, 225) : 'tiles/tile2.jpeg', (226, 255) : 'tiles/tile1.jpeg'}

def get_char(px):
    for (min, max), char in dic_ascii.items():
        if px >= min and px <= max:
            return char

while True:
    ret, frame = cap.read()
    if not ret:
        break

    image_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    image_gray = cv2.resize(image_gray, (800, 400))

    height, width = image_gray.shape

    output = np.zeros_like(image_gray)

    h, w = 20, 20

    for i in range(0, height, h):
        for j in range(0, width, w):
            if i + h <= height and j + w <= width:
                tile = cv2.imread(get_char(image_gray[i][j]))
                tile = cv2.resize(tile, (h,w))
                tile = cv2.cvtColor(tile, cv2.COLOR_BGR2GRAY)
                output[i:i + h, j:j + w] = tile
                
    output += 30

    cv2.imshow("video", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()