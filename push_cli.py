import json, os, shutil, subprocess, tempfile

base = r"C:\Users\guopi\GitHub\courses\future-media-internet\labs\kaggle-demos"
scripts_dir = r"C:\Users\guopi\AppData\Roaming\Python\Python314\Scripts"

notebooks = [
    ("guopingtan/fmi-demo1-traffic-classification", "fmi-demo1-traffic-classification", "demo1-traffic-classification.ipynb"),
    ("guopingtan/fmi-demo2-qoe-optimization", "fmi-demo2-qoe-optimization", "demo2-qoe-optimization.ipynb"),
    ("guopingtan/fmi-demo3-quality-assessment", "fmi-demo3-quality-assessment", "demo3-quality-assessment.ipynb"),
    ("guopingtan/fmi-demo4-neural-compression", "fmi-demo4-neural-compression", "demo4-neural-compression.ipynb"),
    ("guopingtan/fmi-demo5-semantic-communication", "fmi-demo5-semantic-communication", "demo5-semantic-communication.ipynb"),
]

for kid, title, fname in notebooks:
    src = os.path.join(base, fname)
    if not os.path.exists(src):
        print(f"SKIP: {fname}")
        continue

    tmpdir = tempfile.mkdtemp()
    meta = {
        "id": kid, "title": title, "code_file": "notebook.ipynb",
        "language": "python", "kernel_type": "notebook",
        "is_private": False, "enable_gpu": False, "enable_internet": True,
    }
    with open(os.path.join(tmpdir, "kernel-metadata.json"), "w", encoding="utf-8") as f:
        json.dump(meta, f)
    shutil.copy2(src, os.path.join(tmpdir, "notebook.ipynb"))

    kaggle_exe = os.path.join(scripts_dir, "kaggle.exe")
    result = subprocess.run([kaggle_exe, "kernels", "push", "-p", tmpdir], capture_output=True, text=True)
    output = result.stdout + result.stderr
    if "successfully pushed" in output:
        print(f"OK: {kid}")
    else:
        print(f"FAIL: {kid}\n  {output.strip()[:200]}")

    shutil.rmtree(tmpdir, ignore_errors=True)
