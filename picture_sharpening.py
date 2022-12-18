import cv2
import numpy as np

def sharpen_image(image_path):
    # Foto öffnen und in NumPy-Array konvertieren
    image = cv2.imread(image_path)

    # Schärfe des Bildes verbessern
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)
    sharpened_image = cv2.filter2D(image, -1, kernel)

    # Schärftes Bild anzeigen
    cv2.imshow("Sharpened Image", sharpened_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Pfad zum Foto
image_path = "path to your file"

# Foto schärfen
sharpen_image(image_path)
