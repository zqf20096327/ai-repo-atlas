# TSircGroup/monarchgru

⭐ 4 · Python · MIT · 推送 2026-10-16 · [GitHub](https://github.com/TSircGroup/monarchgru) · 组织维护

**面向 IoT 永远在线关键词检测的紧凑 GRU 模型研究代码**

MonarchGRU 论文（IEEE AICAS 2026）官方实现：用 Monarch 矩阵替换 GRU 大部分权重矩阵，最大模型 h=64 仅 29K 参数，在 12 类 Google Speech Commands v2 上达 97.9% 测试准确率。仓库提供 PyTorch 训练与测试代码、数据下载与划分脚本、训练好的 checkpoint，以及 inference.py 对自定义 16 kHz WAV 片段输出关键词与概率；依赖 conda 环境与 NVIDIA GPU（无 GPU 时 CPU 亦可运行推理）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Monarch 矩阵（b=4 块）将 GRU 权重与 MAC 减半
- 最大模型 29.2K 参数，GSC v2 准确率 97.94%
- 提供 h=64/b=4 预训练 checkpoint 与单行关键词预测推理
- 含 Slurm 训练与评测脚本

## 适用场景

- 在 IoT 设备上部署低参数量关键词检测模型
- 复现论文中 MonarchGRU 的训练与测试结果
- 用自己的 16 kHz WAV 音频片段测试关键词识别

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L3: MonarchGRU is a compact recurrent neural network for **always-on** keyword spotting on IoT devices. Its
> L161: - Predict the keyword in your own clips (mono 16 kHz WAV files of at most one second):
> L166:  example `clip.wav: yes (94.2%)`.

## 星数曲线

```mermaid
xychart-beta
    title "TSircGroup/monarchgru 星数(近 3 点)"
    x-axis ["2026-11-08", "2026-11-14", "2026-11-21"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-08 3 → 2026-11-21 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `9cf9de994b3f` · [字段定义](../../DATASET.md)*
