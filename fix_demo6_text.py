import json, os

base = r"C:\Users\guopi\GitHub\courses\future-media-internet\labs\kaggle-demos"

# Chinese markdown for demo6 cell 6
trans = {
    "demo6-hd-video-impairments.ipynb": {
        6: [
            "## 关键结论\n\n"
            "- **丢包**：丢失的宏块（灰色方块）。错误隐藏有帮助，但会留下可见伪影。\n"
            "- **抖动**：水平撕裂（线条错位）。对于无缓冲的直播场景尤为致命。\n"
            "- **带宽骤降**：强制降分辨率导致整体模糊。\n"
            "- **组合损伤**：复合伪影比单一损伤更严重。\n\n"
            "## 实际缓解方案\n"
            "- YouTube/Netflix：ABR（自适应码率）+ FEC（前向纠错）+ 抖动缓冲\n"
            "- WebRTC/Google Meet：NACK（重传）+ FEC + 自适应编码\n"
            "- 5G URLLC：超低时延降低抖动敏感性\n"
        ],
        0: [
            "# Demo 6：HD 视频的网络损伤模拟\n\n"
            "**课程**：未来媒体互联网\n"
            "**时长**：约 10 分钟\n"
            "**环境**：Kaggle Notebook（CPU，NumPy + Matplotlib + SciPy）\n\n"
            "## 实验目标\n\n"
            "模拟丢包、抖动和带宽骤降对 HD 视频画质的影响，\n"
            "展示不同网络损伤类型如何产生视觉上各异的效果。"
        ],
    }
}

for fname, cell_fixes in trans.items():
    path = os.path.join(base, fname)
    with open(path, "r", encoding="utf-8") as f:
        nb = json.load(f)
    for ci, new_src in cell_fixes.items():
        nb["cells"][ci]["source"] = new_src
    with open(path, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
    print(f"Fixed {fname}")

print("Done")
