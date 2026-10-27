# guyyariv/TempoTokens

⭐ 130 · Python · MIT · 推送 2026-05-18 · [GitHub](https://github.com/guyyariv/TempoTokens) · [官网](https://pages.cs.huji.ac.il/adiyoss-lab/TempoTokens/) · 个人维护

**AAAI 2024 论文官方实现：音频生成对齐视频的 PyTorch 代码**

论文 Diverse and Aligned Audio-to-Video Generation via Text-to-Video Model Adaptation 的官方 PyTorch 实现：在已有文本条件视频生成模型与预训练音频编码器（BEATs）之间训练轻量适配网络，将音频表示映射到文生视频模型的输入表示，支持文本、音频及两者联合条件生成视频。在 VGGSound、Landscape、AudioSet-Drum 三个数据集上训练，提供训练命令、预训练权重下载与 inference.py 生成脚本，另提出 AV-Align 对齐评估指标。面向复现实验的科研用户，需 git clone 源码安装并自配 Accelerate 环境。

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

- 轻量适配网络将音频表示映射到文生视频模型输入空间
- 支持文本、音频及文本+音频联合条件的视频生成
- 提供 VGGSound/Landscape/AudioSet-Drum 三数据集训练与预训练权重
- 提出基于双模态能量峰值检测的 AV-Align 对齐评估指标

## 适用场景

- 用我自己的音频文件生成语义与时序对齐的视频
- 复现论文的音频到视频生成实验与评估
- 在自定义数据集上训练音频条件视频生成模型

## 场景标签

`视频生成` · 领域:内容生成

## 证据(README 行号)

> L7: We consider the task of generating diverse and realistic videos guided by natural audio samples from
> L12: and a pre-trained audio encoder model. The proposed method is based on a lightweight adaptor network,
> L58: The ```inference.py``` script serves the purpose of generating videos using trained checkpoints.

## 星数曲线

```mermaid
xychart-beta
    title "guyyariv/TempoTokens 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 129 --> 131
    line [130, 130]
```

2026-10-18 130 → 2026-10-27 130（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `6ed1175349d9` · [字段定义](../../DATASET.md)*
