import cv2
import numpy as np

# 1. Image principale vide (grande image)
output = np.zeros((300, 400, 3), dtype=np.uint8)

# 2. Une mini-image à insérer
tile = cv2.imread("tiles5.jpg")  # par exemple 40x40 px

tile = cv2.resize(tile, (40,40))

# 3. Position où la coller (ex: ligne 100, colonne 120)
y, x = 100, 120

# 4. Insérer l’image dans l’image principale
output[y:y+tile.shape[0], x:x+tile.shape[1]] = tile

# 5. Affichage
cv2.imshow("Mosaic", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
