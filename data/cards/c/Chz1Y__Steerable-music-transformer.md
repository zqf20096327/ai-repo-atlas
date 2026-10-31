# Chz1Y/Steerable-music-transformer

⭐ 14 · Python · MIT · 推送 2026-05-27 · [GitHub](https://github.com/Chz1Y/Steerable-music-transformer) · 个人维护 · 中文 README

**论文官方代码：小节级条件 Transformer 精准控制音乐节奏复杂度**

论文《Steerable Rhythmic Complexity in Autoregressive Music Generation》的官方 PyTorch 实现：基于 REMI+ 语法，在小节级注入 [Level_1]–[Level_10] 复杂度标签并配合 [EOS] 截断机制，在 349 首巴赫四声部合唱曲上从零训练 4 层 8 头微缩 Transformer，实现生成音乐节奏密度的受控调节。面向科研复现者，提供数据构建、训练、生成、评估与消融实验全流程脚本，输出学术级量化图表。

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

- REMI+ 语法小节级复杂度标签（[Level_1]–[Level_10]）条件控制
- 4 层 8 头微缩 Transformer，349 首巴赫四声部合唱曲从零训练
- 目标复杂度与实际音符密度线性相关 Pearson r=0.893
- 内置数据构建、训练、生成、评估与消融实验复现脚本

## 适用场景

- 复现论文的受控音乐生成实验与图表
- 研究节奏复杂度与和声特征的解耦方法
- 在巴赫合唱曲数据上训练和微调小型音乐生成模型

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L12: Welcome! This repository contains the official implementation of the paper **"Steerable Rhythmic Complexity in Auto
> L16: This project introduces a lightweight, highly accurate conditioning mechanism based on the **REMI+ syntax**. By exp
> L27: 4. Generate & Evaluate: Run `generate_samples.py` followed by `evaluate_and_plot.py` to reproduce the academic figu

## 星数曲线

```mermaid
xychart-beta
    title "Chz1Y/Steerable-music-transformer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `0489f5ed8f34` · [字段定义](../../DATASET.md)*
