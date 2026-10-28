# keishihara/flow-matching

⭐ 130 · Python · NOASSERTION · 推送 2026-01-18 · [GitHub](https://github.com/keishihara/flow-matching) · 个人维护

**Flow Matching 论文的 PyTorch 实现，含 CFM 与 Reflow 训练**

PyTorch 实现 Flow Matching for Generative Modeling 论文的方法：支持 Conditional Flow Matching（Lipman+ 2023）与 Rectified Flow/Reflow（Liu+ 2023）两种模型。提供 2D 合成数据集（checkerboard/moons）与图像数据集（如 MNIST 类条件生成）的训练与采样脚本，训练结果与向量场可视化输出到 outputs 目录。Reflow 为蒸馏模型，需指定预训练 CFM 检查点。环境通过 uv 管理，要求 Python 3.12+，未附带模型检查点（默认设置可复现）。部分代码改编自 facebookresearch/flow_matching 等仓库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Conditional Flow Matching（Lipman+ 2023）实现
- 2-Rectified Flow/Reflow 蒸馏实现（Liu+ 2023）
- 2D 合成数据与图像数据集（MNIST 类条件）训练/采样脚本
- CFM 与 Reflow 采样过程对比可视化

## 适用场景

- 学习和复现 Flow Matching 论文方法
- 在 checkerboard/moons 等 2D 数据上做生成模型实验
- 训练类条件图像生成模型并生成样本

## 场景标签

`图像生成` `教程课程` · 领域:内容生成

## 证据(README 行号)

> L27: This repository contains a simple PyTorch implementation of the paper Flow Matching for Generative Modeling.
> L57: ## Conditional Flow Matching [Lipman+ 2023]

## 星数曲线

```mermaid
xychart-beta
    title "keishihara/flow-matching 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-28"]
    y-axis "stars" 127 --> 131
    line [128, 129, 130]
```

2026-10-18 128 → 2026-10-28 130（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `bbc4a94342de` · [字段定义](../../DATASET.md)*
