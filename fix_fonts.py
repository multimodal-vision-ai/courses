import json, re, os

base = r"C:\Users\guopi\GitHub\courses\future-media-internet\labs\kaggle-demos"

# Translation map for Chinese plot labels -> English
translations = {
    # demo1
    "('平均包长 (bytes)')": "('Avg Packet Length (bytes)')",
    "('平均包间隔 (s)')": "('Avg Inter-arrival Time (s)')",
    "('流量特征空间分布')": "('Traffic Feature Distribution')",
    "('分类准确率')": "('Classification Accuracy')",
    "('特征选择对分类结果的影响')": "('Impact of Feature Selection')",
    "('仅用端口号', '统计特征（5维）')": "('Port Only', 'Statistical Features (5D)')",
    "('混淆矩阵：KNN + 统计特征')": "('Confusion Matrix: KNN + Statistical Features')",
    "('预测类别')": "('Predicted')",
    "('真实类别')": "('True Label')",
    "f'{v:.1%}'": "f'{v:.1%}'",
    # demo2
    "('时间 (秒)')": "('Time (s)')",
    "('带宽 (Mbps)')": "('Bandwidth (Mbps)')",
    "('模拟网络带宽波动（100 秒）')": "('Simulated Bandwidth Fluctuation (100s)')",
    "label='低码率视频 (2 Mbps)'": "label='Low Bitrate (2 Mbps)'",
    "label='中码率视频 (5 Mbps)'": "label='Medium Bitrate (5 Mbps)'",
    "label='高码率视频 (10 Mbps)'": "label='High Bitrate (10 Mbps)'",
    "('码率 (Mbps)'": "('Bitrate (Mbps)'",
    "('缓冲 (秒)'": "('Buffer (s)'",
    # demo3
    "titles = ['原始', '轻微压缩', '中等压缩', '严重压缩']": "titles = ['Original', 'Light', 'Medium', 'Heavy']",
    "('模拟不同压缩程度的图像')": "('Images at Different Compression Levels')",
    "('传统指标：PSNR（越高越好）')": "('Traditional: PSNR (higher=better)')",
    "('感知指标：SSIM（越接近 1 越好）')": "('Perceptual: SSIM (closer to 1=better)')",
    "('PSNR (dB)')": "('PSNR (dB)')",
    "('传统指标 vs 感知指标：同一组图的两种评价'": "('Traditional vs Perceptual Metrics'",
    # demo4
    "('原始测试图像\\n（棋盘格=高频 | 渐变=低频 | 横线=边缘）')": "('Test Image\\n(Checkerboard=HF | Gradient=LF | Line=Edge)')",
    "('JPEG 模拟\\n'": "('JPEG\\n'",
    "('神经压缩\\n'": "('Neural\\n'",
    "f'{label}压缩'": "f'{label}'",
    "('JPEG vs 神经压缩：同一图像在不同压缩程度下的对比\\n（上排：JPEG | 下排：神经压缩）'": "('JPEG vs Neural Compression\\n(Top: JPEG | Bottom: Neural)'",
    # demo5
    "('MNIST 手写数字样本')": "('MNIST Digit Samples')",
    "f'Label: {label}'": "f'Label: {label}'",
    "('Semantic vs Traditional: Reconstruction at Different SNR\\n(Top: Traditional | Middle: Semantic)'": "('Semantic vs Traditional: Reconstruction at Different SNR (Top: Traditional | Bottom: Semantic)'",
}

for fname in sorted(os.listdir(base)):
    if not fname.endswith(".ipynb"):
        continue
    path = os.path.join(base, fname)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    changed = False
    for old, new in translations.items():
        if old in content:
            content = content.replace(old, new)
            changed = True

    if changed:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Fixed: {fname}")

print("Done")
