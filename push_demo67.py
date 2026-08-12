import json, os, shutil, subprocess, tempfile

base = r"C:\Users\guopi\GitHub\courses\future-media-internet\labs\kaggle-demos"
scripts_dir = r"C:\Users\guopi\AppData\Roaming\Python\Python314\Scripts"

notebooks = [
    ("guopingtan/fmi-demo6-hd-impairments", "fmi-demo6-hd-impairments", "demo6-hd-video-impairments.ipynb"),
    ("guopingtan/fmi-demo7-vr-impairments", "fmi-demo7-vr-impairments", "demo7-vr-video-impairments.ipynb"),
]

for kid, title, fname in notebooks:
    src = os.path.join(base, fname)
    if not os.path.exists(src):
        print(f"SKIP: {fname}")
        continue

    tmpdir = tempfile.mkdtemp()
    meta = {"id": kid, "title": title, "code_file": "notebook.ipynb", "language": "python", "kernel_type": "notebook", "is_private": False, "enable_gpu": False, "enable_internet": True}
    with open(os.path.join(tmpdir, "kernel-metadata.json"), "w", encoding="utf-8") as f:
        json.dump(meta, f)
    shutil.copy2(src, os.path.join(tmpdir, "notebook.ipynb"))

    kaggle_exe = os.path.join(scripts_dir, "kaggle.exe")
    result = subprocess.run([kaggle_exe, "kernels", "push", "-p", tmpdir], capture_output=True, text=True)
    output = result.stdout + result.stderr
    if "successfully pushed" in output:
        print(f"OK: https://www.kaggle.com/code/{kid}")
    else:
        print(f"FAIL: {kid} - {output.strip()[:200]}")

    shutil.rmtree(tmpdir, ignore_errors=True)
