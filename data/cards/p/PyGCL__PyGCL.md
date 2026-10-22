# PyGCL/PyGCL

⭐ 967 · Python · Apache-2.0 · 推送 2026-02-17 · [GitHub](https://github.com/PyGCL/PyGCL) · [官网](https://PyGCL.readthedocs.io) · 组织维护

**图对比学习 PyTorch 库：为研究者提供模块化 GCL 组件**

基于 PyTorch 的图对比学习（GCL）开源库，面向机器学习研究者与开发者：将已发表论文中的 GCL 算法拆解为四类模块化组件——图增广、对比架构与模式、对比目标、负采样策略，并附带模型训练、评估与实验管理工具。内置 DGI、GRACE、GraphCL、BGRL 等 14 种方法实现与示例。通过 pip 安装，依赖 Python 3.8+、PyTorch 1.9+、PyTorch-Geometric、DGL、Scikit-learn 等前置包，DGL 的 CUDA 版本需用户自行安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四类模块化组件：增广（11 种）、对比架构、对比目标（6 种损失）、负采样策略
- 实现 DGI、GRACE、GraphCL、BGRL、VICReg 等 14 种已发表方法并附示例
- 支持组合与随机选择增广、单/双分支及无负样本对比架构
- 提供 LR/SVM/RF 三种嵌入质量评估器与实验管理工具

## 适用场景

- 在节点/图分类任务上快速复现已发表的图对比学习算法
- 组合模块化组件构建自己的 GCL 算法
- 对比评估不同 GCL 方法学到的图表示质量

## 场景标签

 · 领域:机器学习/图表示学习

## 证据(README 行号)

> L3: PyGCL is a PyTorch-based open-source Graph Contrastive Learning (GCL) library, which features modularized GCL compon
> L50: Our PyGCL implements four main components of graph contrastive learning algorithms:
> L61: For a quick start, please check out the `examples` folder. We currently implemented the following methods:

## 星数曲线

```mermaid
xychart-beta
    title "PyGCL/PyGCL 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 965 --> 968
    line [966, 967, 967]
```

2026-10-18 966 → 2026-10-22 967（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `c18107f19e04` · [字段定义](../../DATASET.md)*
