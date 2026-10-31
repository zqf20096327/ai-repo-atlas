# jakubpeleska/redelex

⭐ 25 · Jupyter Notebook · MIT · 推送 2026-10-27 · [GitHub](https://github.com/jakubpeleska/redelex) · [官网](https://relational.fel.cvut.cz/) · 组织维护

**面向研究者的关系深度学习开发与评测框架**

Python 框架，用于在关系数据库上开发与评测关系深度学习（RDL）模型：将 SQL 数据库转换为适合 GNN 的异构图表示，自动做属性类型推断与编码，提供 CTU 仓库 70+ 关系数据集访问并集成 RelBench 接口。支持静态/时序节点预测、链接预测、预训练任务，可对比 GraphSAGE、DBFormer 等深度模型与 LightGBM、命题化等传统方法。要求 Python 3.12，pip 安装，开发环境用 uv 管理，CUDA 为可选分组。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SQL 数据库到异构图的自动转换与属性类型推断编码
- CTU 仓库 70+ 关系数据集与 RelBench 接口集成
- 支持节点级/链接预测/时序任务/预训练（值掩码）
- RDL 模型与传统 ML（LightGBM、命题化）的结构化对比

## 适用场景

- 在自有 SQL 数据库上做关系深度学习实验
- 跨 70+ 关系数据集基准评测 RDL 与传统 ML 方法
- 按结构与规模筛选适合 RDL 的数据集

## 场景标签

`模型评测` `模型训练` · 领域:评测与运维

## 证据(README 行号)

> L10: **ReDeLEx** (Relational Deep Learning Exploration) is a Python framework for the development and evaluation of **Re
> L12: It provides tools to transform SQL databases into heterogeneous graph representations suitable for Graph Neural Net

## 星数曲线

```mermaid
xychart-beta
    title "jakubpeleska/redelex 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-31 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `1449fc17f699` · [字段定义](../../DATASET.md)*
