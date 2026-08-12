import os, json, shutil, tempfile
from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

# Update demo1 with the fixed/formatted version
kid = "gptan1975/fmi-demo1-traffic-classification"
fname = "demo1-traffic-classification.ipynb"
base_dir = r"C:\Users\guopi\GitHub\courses\future-media-internet\labs\kaggle-demos"
src = os.path.join(base_dir, fname)

tmpdir = tempfile.mkdtemp()
metadata = {
    "id": kid,
    "title": "fmi-demo1-traffic-classification",
    "code_file": fname,
    "language": "python",
    "kernel_type": "notebook",
    "is_private": False,
    "enable_gpu": False,
    "enable_internet": True,
}
with open(os.path.join(tmpdir, "kernel-metadata.json"), "w", encoding="utf-8") as f:
    json.dump(metadata, f, indent=2)
shutil.copy2(src, os.path.join(tmpdir, fname))

try:
    api.kernels_push(tmpdir)
    print(f"OK: updated demo1 -> https://www.kaggle.com/code/fmi-demo1-traffic-classification")
except Exception as e:
    print(f"FAIL: {e}")

shutil.rmtree(tmpdir, ignore_errors=True)
