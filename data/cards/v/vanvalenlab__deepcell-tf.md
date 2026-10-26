# vanvalenlab/deepcell-tf

⭐ 481 · Python · Apache-2.0 · 推送 2026-06-04 · [GitHub](https://github.com/vanvalenlab/deepcell-tf) · [官网](https://deepcell.readthedocs.io) · 组织维护

**生物图像单细胞分析深度学习库：细胞分割与追踪**

基于 TensorFlow 2 的 Python 深度学习库，面向生物图像的单细胞分析：提供细胞分割（全细胞与细胞核，2D/3D）与 2D 时间序列细胞追踪模型，支持应用预训练模型（deepcell.applications）与训练新模型（deepcell.datasets 含约 10,000 条单细胞轨迹与约 75,000 条标注）。适用数据涵盖多重染色组织图像与活细胞动态成像。通过 pip 安装，或使用带 GPU 支持的 Docker 容器（需 CUDA）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 细胞分割模型支持 2D/3D 全细胞与细胞核分割
- 2D 时间序列数据细胞追踪
- deepcell.datasets 提供带单细胞标注的生物图像数据集
- deepcell.applications 提供开箱即用的预训练模型

## 适用场景

- 对活细胞成像数据进行细胞分割与追踪
- 基于标注数据训练新的单细胞分析模型
- 在多重染色组织图像上应用预训练分割模型

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L11: `deepcell-tf` is a deep learning library for single-cell analysis of biological images. It is written in Python and
> L13: This library allows users to apply pre-existing models to imaging data as well as to develop new deep learning mode
> L67: `deepcell-tf` contains two modules that greatly simplify the development and usage of deep learning models for sing

## 星数曲线

```mermaid
xychart-beta
    title "vanvalenlab/deepcell-tf 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 480 --> 482
    line [481, 481]
```

2026-10-18 481 → 2026-10-26 481（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `788bc255df8f` · [字段定义](../../DATASET.md)*
