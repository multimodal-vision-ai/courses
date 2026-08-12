from kaggle.api.kaggle_api_extended import KaggleApi
import os, json, shutil, tempfile

api = KaggleApi()
api.authenticate()

kid = "gptan1975/fmi-demo5-semantic-communication"
fname = "demo5-semantic-communication.ipynb"
base = r"C:\Users\guopi\GitHub\courses\future-media-internet\labs\kaggle-demos"

# Try to delete old version
try:
    print("Deleting old kernel...")
    # The API might support kernel delete. Try calling the API directly.
    # If not available, we'll just note that it can't be updated.
    api.kernels_list()  # test connection
except Exception as e:
    print(f"Note: {e}")

# Create temp dir and push again
tmpdir = tempfile.mkdtemp()
metadata = {
    "id": kid, "title": "fmi-demo5-semantic-communication",
    "code_file": fname, "language": "python", "kernel_type": "notebook",
    "is_private": False, "enable_gpu": False, "enable_internet": True,
}
with open(os.path.join(tmpdir, "kernel-metadata.json"), "w", encoding="utf-8") as f:
    json.dump(metadata, f, indent=2)

src = os.path.join(base, fname)
shutil.copy2(src, os.path.join(tmpdir, fname))

try:
    api.kernels_push(tmpdir)
    print(f"OK: https://www.kaggle.com/code/{kid}")
except Exception as e:
    print(f"Cannot update (409): {kid}")
    print("Please manually re-upload the file via Kaggle UI:")
    print(f"  1. Open https://www.kaggle.com/code/{kid}")
    print(f"  2. File -> Upload Notebook -> select {fname}")
    print(f"  3. Run All -> Save Version")

shutil.rmtree(tmpdir, ignore_errors=True)
