# TRahulsingh/DeepfakeDetector

⭐ 39 · Python · MIT · 推送 2026-04-21 · [GitHub](https://github.com/TRahulsingh/DeepfakeDetector) · 个人维护

**基于 EfficientNet-B0 的深度伪造图像/视频检测系统**

用 PyTorch 实现的深伪检测系统：以 ImageNet 预训练的 EfficientNet-B0 为骨干，接自定义二分类头，输入 224x224 图像，输出真/伪判定与置信度；视频采用首帧或 10 帧均匀采样取概率平均。提供 Gradio 网页界面拖拽分析图像与视频、命令行分类脚本、批量评估（含高斯模糊与 JPEG 压缩噪声模拟）、完整 PyTorch Lightning 训练管线，支持导出 ONNX 与 .pt。README 罗列 FaceForensics++、Celeb-DF、DFDC 等训练数据集，需自行下载模型或训练。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- EfficientNet-B0 骨干 + 二分类头，输出真/伪与置信度
- Gradio 网页界面支持图像与视频拖拽分析
- 视频 10 帧均匀采样概率平均，另含单帧快速模式
- PyTorch Lightning 训练管线，支持 ONNX/.pt 导出与噪声鲁棒性评估

## 适用场景

- 上传图像或视频判断是否为深度伪造
- 用公开深伪数据集训练自己的检测模型
- 对一批真实样本做带噪声模拟的批量评估

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L3: A state-of-the-art deepfake detection system built with PyTorch and EfficientNet-B0, featuring a user-friendly web i
> L15: - **Web Interface**: Interactive Gradio-based web application for easy testing
> L218: - **Output**: Binary classification (Real/Fake) with confidence scores

## 星数曲线

```mermaid
xychart-beta
    title "TRahulsingh/DeepfakeDetector 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 38 --> 40
    line [39, 39]
```

2026-10-18 39 → 2026-10-25 39（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `64a5e1310a52` · [字段定义](../../DATASET.md)*
