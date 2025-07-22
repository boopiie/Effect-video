import cv2

# Charger le classifieur de visages
face_cascade = cv2.CascadeClassifier("C:/Users/User/Desktop/CodePlaisir/visageLive/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("C:/Users/User/Desktop/CodePlaisir/visageLive/haarcascade_eye.xml")


# Ouvrir la webcam (0 = caméra principale)
cap = cv2.VideoCapture(0)

while True:
    # Lire une frame de la webcam
    ret, frame = cap.read()

    if not ret:
        print("❌ Erreur de lecture caméra.")
        break

    # Convertir en niveaux de gris
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Détection des visages
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)


    for (x, y, w, h) in faces:
        # Dessiner un rectangle autour du visage
        center = (x + w // 2, y + h // 2)  # centre de l’ellipse
        axes = (w // 3, h // 2)           # demi-largeur et demi-hauteur
        cv2.ellipse(frame, center, axes, 0, 0, 360, (0, 255, 0), 2)


        # Extraire juste la région du visage
        face_gray = gray[y:y+h, x:x+w]
        face_color = frame[y:y+h, x:x+w]

        # Détection des yeux dans le visage
        eyes = eye_cascade.detectMultiScale(face_gray,
            scaleFactor=1.1,
            minNeighbors=10,
            minSize=(30, 30))

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(face_color, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 2)
    # Afficher la frame
    cv2.imshow('Détection de Visage (appuie sur q pour quitter)', frame)

    # Quitter si touche "q"
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libérer la caméra et fermer la fenêtre
cap.release()
cv2.destroyAllWindows()
