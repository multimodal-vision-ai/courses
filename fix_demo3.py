import json

path = r"C:\Users\guopi\GitHub\courses\future-media-internet\labs\kaggle-demos\demo3-quality-assessment.ipynb"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Fix the known issue: double-backslash-quote should be escaped-quote
# In the raw text: \\" should become \"
content = content.replace('学习\\\\"人', '学习\\"人')
content = content.replace('看\\\\")', '看\\")')

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

try:
    with open(path, "r", encoding="utf-8") as f:
        json.load(f)
    print("OK: demo3 fixed and valid")
except json.JSONDecodeError as e:
    print(f"Still broken: {e}")
