import cv2
import os
import platform
from datetime import datetime
import numpy as np

# Dossier pour stocker les photos
output_folder = "PED"

# Créer le dossier s'il n'existe pas
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Nom du fichier basé sur la date actuelle
current_date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = os.path.join(output_folder, f"{current_date}.jpg")

# Augmenter la luminosité de l'écran
if platform.system() == "Windows":
    os.system("powershell (Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,100)")

# Capturer une photo avec la webcam
def take_photo():
    cap = cv2.VideoCapture(0)  # Ouvre la webcam
    if not cap.isOpened():
        print("Erreur : Impossible d'accéder à la webcam.")
        return

    ret, frame = cap.read()
    if ret:
        cv2.imwrite(filename, frame)  # Sauvegarder l'image capturée
        print(f"Photo prise et sauvegardée dans : {filename}")
    else:
        print("Erreur : Impossible de capturer une image.")
    cap.release()  # Fermer la webcam
    cv2.destroyAllWindows()

# Exécution des étapes
if __name__ == "__main__":
    take_photo()  # Prendre la photo
