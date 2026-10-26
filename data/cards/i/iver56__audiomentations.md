# iver56/audiomentations

⭐ 2,324 · Python · MIT · 推送 2026-04-13 · [GitHub](https://github.com/iver56/audiomentations) · [官网](https://iver56.github.io/audiomentations/) · 个人维护

**Python 音频数据增强库：为音频 ML 训练提供变换**

Audiomentations 是一个 Python 音频数据增强库，API 设计参考 albumentations，用于提升音频深度学习模型在真实环境下的表现。提供 40 余种变换，包括加噪（高斯/彩色/短噪声）、音高与时间变换、各类滤波器、混响模拟（ApplyImpulseResponse、RoomSimulator）、MP3 压缩、响度归一化等。支持 CPU 运行、单声道与多声道音频，可集成到 TensorFlow/Keras 或 PyTorch 训练流水线。通过 pip 安装，MIT 许可，支持 Linux/macOS/Windows。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 40 余种音频变换（加噪、滤波、音高/时间变换、混响模拟等）
- 支持单声道与多声道音频，CPU 运行
- 可集成 TensorFlow/Keras 或 PyTorch 训练流水线
- Compose 机制可组合多个变换

## 适用场景

- 训练音频分类或识别模型前扩充训练数据
- 模拟真实环境的噪声、混响与失真以提升模型鲁棒性
- 在现有 PyTorch/TensorFlow 流水线中插入增强步骤

## 场景标签

 · 领域:音频机器学习/数据增强

## 证据(README 行号)

> L9: Audiomentations is a Python library for audio data augmentation, built to be fast and easy to use - its API is inspi
> L11: Audiomentations runs on CPU, supports mono audio and multichannel audio and integrates well in training pipelines,

## 星数曲线

```mermaid
xychart-beta
    title "iver56/audiomentations 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 2322 --> 2325
    line [2323, 2324]
```

2026-10-18 2,323 → 2026-10-26 2,324（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `b529dcb2b839` · [字段定义](../../DATASET.md)*
