# Labbeti/aac-datasets

⭐ 130 · Python · MIT · 推送 2026-03-25 · [GitHub](https://github.com/Labbeti/aac-datasets) · [官网](https://aac-datasets.readthedocs.io/) · 个人维护

**PyTorch 音频描述（Audio Captioning）数据集加载库**

为 PyTorch 提供 AudioCaps、Clotho、MACS、WavCaps 四个音频描述数据集的下载与加载支持，以 Dataset 类和 CLI（aac-datasets-download、aac-datasets-info）形式提供。README 给出各数据集的采样率、体积、子集划分与统计信息。面向 Ubuntu 20.04 及多数 Linux 发行版开发，测试 Python 3.7-3.13；AudioCaps 下载需外部依赖 ffmpeg 与 yt-dlp，且受 YouTube 反爬限制可能需要 cookies。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 4 个音频描述数据集（AudioCaps/Clotho/MACS/WavCaps）的下载与 PyTorch 加载
- 提供 CLI 命令下载与查询数据集信息
- 附各数据集的统计信息（音频数、时长、词表等）
- 兼容 audiocaps-download 1.0 包的目录结构

## 适用场景

- 训练音频描述模型时准备训练数据
- 对比各音频描述数据集的规模与统计特性
- 在脚本中批量下载 Clotho 等数据集子集

## 场景标签

 · 领域:音频/机器学习数据集

## 证据(README 行号)

> L11: Audio Captioning unofficial datasets source code for **AudioCaps** [[1]](#audiocaps), **Clotho** [[2]](#clotho), **
> L56: |Dataset|Sampling rate (kHz)|Estimated size (GB)|Source|Subsets|

## 星数曲线

```mermaid
xychart-beta
    title "Labbeti/aac-datasets 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 129 --> 131
    line [130, 130]
```

2026-10-18 130 → 2026-10-23 130（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `b5dbd145628c` · [字段定义](../../DATASET.md)*
