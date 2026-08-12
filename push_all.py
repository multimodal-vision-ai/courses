import os, json, shutil, tempfile, nbformat
from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

base = r"C:\Users\guopi\GitHub\courses\future-media-internet\labs\kaggle-demos"

# Format all notebooks
for fname in os.listdir(base):
    if fname.endswith(".ipynb"):
        path = os.path.join(base, fname)
        nb = nbformat.read(path, as_version=4)
        nbformat.write(nb, path)

notebooks = [
    ("gptan1975/fmi-demo1-traffic-classification", "fmi-demo1-traffic-classification", "demo1-traffic-classification.ipynb"),
    ("gptan1975/fmi-demo2-qoe-optimization", "fmi-demo2-qoe-optimization", "demo2-qoe-optimization.ipynb"),
    ("gptan1975/fmi-demo3-quality-assessment", "fmi-demo3-quality-assessment", "demo3-quality-assessment.ipynb"),
    ("gptan1975/fmi-demo4-neural-compression", "fmi-demo4-neural-compression", "demo4-neural-compression.ipynb"),
    ("gptan1975/fmi-demo5-semantic-communication", "fmi-demo5-semantic-communication", "demo5-semantic-communication.ipynb"),
]

for kid, title, fname in notebooks:
    src = os.path.join(base, fname)
    if not os.path.exists(src):
        print(f"SKIP: {fname}")
        continue

    tmpdir = tempfile.mkdtemp()
    metadata = {
        "id": kid, "title": title, "code_file": fname,
        "language": "python", "kernel_type": "notebook",
        "is_private": False, "enable_gpu": False, "enable_internet": True,
    }
    with open(os.path.join(tmpdir, "kernel-metadata.json"), "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)
    shutil.copy2(src, os.path.join(tmpdir, fname))

    try:
        api.kernels_push(tmpdir)
        url = f"https://www.kaggle.com/code/{kid}"
        print(f"OK: {url}")
    except Exception as e:
        err = str(e)
        if "409" in err:
            url = f"https://www.kaggle.com/code/{kid}"
            print(f"EXISTS: {url}")
        else:
            print(f"FAIL: {title} - {err[:100]}")

    shutil.rmtree(tmpdir, ignore_errors=True)
