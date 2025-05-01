import os
from PIL import Image

# Wurzelverzeichnis festlegen (aktuelles Verzeichnis)
root_dir = "./Versuch0"

# Alle Dateien durchlaufen
for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.lower().endswith(".bmp"):
            bmp_path = os.path.join(dirpath, filename)
            png_path = os.path.splitext(bmp_path)[0] + ".png"

            try:
                with Image.open(bmp_path) as img:
                    img.save(png_path, "PNG")
                print(f"Konvertiert: {bmp_path} → {png_path}")
            except Exception as e:
                print(f"Fehler bei {bmp_path}: {e}")
