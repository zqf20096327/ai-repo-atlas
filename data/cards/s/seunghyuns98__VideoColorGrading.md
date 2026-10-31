# seunghyuns98/VideoColorGrading

⭐ 99 · Python · Apache-2.0 · 推送 2025-12-29 · [GitHub](https://github.com/seunghyuns98/VideoColorGrading) · 组织维护

**基于扩散模型的参考引导视频调色框架（ICCV 2025）**

ICCV 2025 论文的官方实现：给定参考图像与输入视频，通过扩散模型生成查找表（LUT）实现参考场景与输入视频间的色彩属性对齐。提供预训练权重的推理脚本 video_demo.py，支持两阶段训练（GS-Extractor 与 L-Diffuser）与评估；训练数据基于 Condensed Movie Dataset（3,000 部电影的 33,000+ 片段）与 Video Harmonization Dataset 的 100 个 LUT 基底。作者来自 GIST、延世大学与 Adobe Research，通过 conda 环境脚本与预训练权重（Google Drive）运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 参考图像引导的视频调色，扩散模型生成 LUT
- 提供预训练权重与推理脚本 video_demo.py
- 两阶段训练流程（GS-Extractor、L-Diffuser）与评估脚本
- 基于 Condensed Movie Dataset（33,000+ 片段）构建训练数据

## 适用场景

- 用参考图风格对视频做自动色彩校正
- 复现 ICCV 2025 论文的推理与训练
- 在自己的视频数据集上训练定制调色模型

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L21: We present a reference-based video color grading framework. Our key idea is to generate a look-up table (LUT) for c
> L15: ICCV 2025

## 星数曲线

```mermaid
xychart-beta
    title "seunghyuns98/VideoColorGrading 星数(近 5 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-27", "2026-10-29", "2026-10-31"]
    y-axis "stars" 94 --> 100
    line [95, 97, 98, 99, 99]
```

2026-10-18 95 → 2026-10-31 99（+4）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `501c3a03de28` · [字段定义](../../DATASET.md)*
