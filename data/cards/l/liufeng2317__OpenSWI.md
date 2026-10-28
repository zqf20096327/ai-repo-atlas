# liufeng2317/OpenSWI

⭐ 19 · Jupyter Notebook · CC-BY-4.0 · 推送 2025-11-19 · [GitHub](https://github.com/liufeng2317/OpenSWI) · [官网](https://liufeng2317.github.io/OpenSWI/) · 组织维护 · 中文 README

**面波频散曲线反演的大规模基准数据集（超2300万样本对）**

面向地球物理勘探与深部构造研究的基准数据集，含三个子集：OpenSWI-shallow（源自 OpenFWI 二维模型，超 2200 万条一维速度剖面与频散曲线对）、OpenSWI-deep（基于 14 个全球/区域三维模型约 126 万对）、OpenSWI-real（Long Beach 与中国地震参考模型项目的实测数据，用于泛化评估）。同时发布数据构建流水线 SWIDP 工具箱（含基于 Disba 的并行正演求解器）与 Transformer/CNN 结构的深度学习反演模型及训练示例。数据托管于 Hugging Face，采用 CC BY 4.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `viral` | CC-BY-4.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenSWI-shallow 超过 2200 万对速度剖面-频散曲线样本
- OpenSWI-deep 基于 14 个全球/区域 3D 地质模型约 126 万对
- SWIDP 模块化数据构建流水线（含优化并行 Disba 求解器）
- 提供 CNN+Transformer 端到端反演网络 DispFormer 与训练示例

## 适用场景

- 训练与评测面波频散曲线反演的深度学习模型
- 用实测数据（Long Beach、CSRM）评估模型泛化能力
- 复用 SWIDP 流水线构建自己的频散曲线数据集

## 场景标签

 · 领域:地球物理/地震学

## 证据(README 行号)

> L9: > **OpenSWI: A Massive-Scale Benchmark Dataset for Surface Wave Dispersion Curve Inversion**
> L13: >> **Abstract:** Surface wave dispersion curve inversion plays a critical role in both shallow resource exploration
> L16: **More Details of the OpenSWI Datasets can be found at huggingface** (OpenSWI Huggingface)

## 星数曲线

```mermaid
xychart-beta
    title "liufeng2317/OpenSWI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `701d439bc49f` · [字段定义](../../DATASET.md)*
