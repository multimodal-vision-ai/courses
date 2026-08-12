import os, nbformat

base = r"C:\Users\guopi\GitHub\courses\future-media-internet\labs\kaggle-demos"
for fname in os.listdir(base):
    if fname.endswith(".ipynb"):
        path = os.path.join(base, fname)
        nb = nbformat.read(path, as_version=4)
        nbformat.write(nb, path)
        print(f"Formatted: {fname}")
