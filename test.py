import cv2

# Liste des caractères ASCII du plus foncé au plus clair
ascii_chars = "@%#*+=-:. "

def pixel_to_ascii(pixel_value):
    """Convertit une valeur de pixel (0-255) en caractère ASCII"""
    index = int(pixel_value / 256 * len(ascii_chars))
    return ascii_chars[min(index, len(ascii_chars)-1)]

# Charger l'image en niveaux de gris
img = cv2.imread("Gotaga_2018.jpg", cv2.IMREAD_GRAYSCALE)

# Redimensionner l'image pour la console (optionnel)
img = cv2.resize(img, (100, 40))  # largeur x hauteur (ajuste selon ta console)

# Convertir chaque pixel en ASCII
for row in img:
    line = "".join([pixel_to_ascii(pixel) for pixel in row])
    print(line)