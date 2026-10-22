# worldbench/3EED

⭐ 212 · Python · Apache-2.0 · 推送 2025-12-26 · [GitHub](https://github.com/worldbench/3EED) · [官网](https://project-3eed.github.io) · 组织维护

**跨车辆/无人机/四足平台的 3D 视觉定位数据集与基线**

NeurIPS 2025 Dataset & Benchmark Track 论文 3EED 的官方仓库：发布首个跨越车辆、无人机、四足三类平台的大规模 3D grounding 数据集，含同步 RGB、LiDAR 与语言标注，数据集与基线模型放在 HuggingFace。仓库同时提供基于 BUTD-DETR/WildRefer 思路的基线训练、评估与可视化代码，支持 CUDA 11.1 与 CUDA 12.4 两种环境，需编译自定义 CUDA 算子，语言编码器使用 RoBERTa-base。数据来源为 Waymo Open Dataset 与 M3ED。Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖车辆/无人机/四足三类平台的大规模 3D grounding 数据集
- RGB、LiDAR 与语言多模态同步标注
- 提供统一评测协议与基线训练/评估/可视化代码
- 基线模型与预测结果托管于 HuggingFace

## 适用场景

- 在多平台真实场景上评测 3D 视觉定位方法
- 训练基于语言指代的 3D 定位基线模型
- 复现论文结果并可视化点云上的 3D 检测框

## 场景标签

 · 领域:3D 视觉/空间智能

## 证据(README 行号)

> L24: - **Cross-Platform**: First 3D grounding dataset spanning **vehicle**, **drone**, and **quadruped** platforms
> L50: - **[2025.09]** 3EED has been accepted to **NeurIPS 2025 Dataset and Benchmark Track**! 🎉

## 星数曲线

```mermaid
xychart-beta
    title "worldbench/3EED 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-21"]
    y-axis "stars" 211 --> 213
    line [212, 212]
```

2026-10-18 212 → 2026-10-21 212（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `5e6d42c0a3a1` · [字段定义](../../DATASET.md)*
