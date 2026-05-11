import os

print("Extraction Kobo")
os.system("python scripts/extract_kobo.py")

print("Jointure")
os.system("python scripts/merge_data.py")

print("Transformation")
os.system("python scripts/transform.py")

print("Pipeline terminé")
