import os
import cv2
import numpy as np

# Pfad zum Ordner, durch den iteriert werden soll
folder_path = "path to your image-folder"

# Leere Liste, in der die Pfade zu den Fotos mit Hautfarbe gespeichert werden
skin_colored_photos = []

# Iterieren durch alle Dateien im Ordner
for filename in os.listdir(folder_path):
    # Nur Bilddateien verarbeiten
    if filename.endswith(".jpg") or filename.endswith(".png"):
        
        # Pfad zur aktuellen Bilddatei erstellen
        file_path = os.path.join(folder_path, filename)

        # Bilddatei öffnen und in NumPy-Array konvertieren
        image = cv2.imread(file_path)
        image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # Grenzen für Hautfarbe in HSV-Farbraum definieren
        lower_skin_color = np.array([0, 48, 80], dtype="uint8")
        upper_skin_color = np.array([20, 255, 255], dtype="uint8")

        # Maskierungsbild erstellen, das nur Pixel mit Hautfarbe enthält
        skin_mask = cv2.inRange(image_hsv, lower_skin_color, upper_skin_color)

        # Anzahl der Pixel mit Hautfarbe ermitteln
        skin_colored_pixels = cv2.countNonZero(skin_mask)

        # Wenn mehr als 50% der Pixel Hautfarbe haben, wird das Bild in die Liste aufgenommen
        if skin_colored_pixels / (image.shape[0] * image.shape[1]) > 0.5:
            skin_colored_photos.append(file_path)

# Pfad zur Datei, in der die Pfade zu den Fotos mit Hautfarbe gespeichert werden sollen
output_file_path = "example/test.txt"

# Leere Datei erstellen oder vorhandene überschreiben
open(output_file_path, "w").close()

# Pfade zu den Fotos mit Hautfarbe in die Datei schreiben
with open(output_file_path, "w") as output_file:
    for photo in skin_colored_photos:
        output_file.write(photo + "\n")
