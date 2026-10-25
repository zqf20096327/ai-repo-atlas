# microsoft/Graphormer

⭐ 2,481 · Python · MIT · 推送 2026-09-26 · [GitHub](https://github.com/microsoft/Graphormer) · 组织维护

**微软开源的分子建模图 Transformer 深度学习框架**

面向研究者与开发者的分子建模深度学习包：以 Graphormer 图 Transformer 为骨干，训练自定义分子模型，应用于材料发现、药物发现等分子科学任务。v2.0 提供 Open Catalyst Challenge 模型与脚本、PCQM4M/PCQM4Mv2 预训练模型，支持 PyG、DGL、OGB、OCP 数据接口与 fairseq 骨干。代码基于固定版本的 Fairseq 与旧版 Python/PyTorch 栈，推荐容器方式运行；高级预训练版本仅在 Azure Quantum Elements 提供。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 图 Transformer 骨干用于分子建模，NeurIPS 2021 发表
- 提供 PCQM4M/PCQM4Mv2 预训练模型与 Open Catalyst Challenge 模型脚本
- 支持 PyG、DGL、OGB、OCP 数据接口与 fairseq 骨干
- 容器化环境固定 Python 3.9 / PyTorch 1.9.1 / CUDA 11.1 保证可复现

## 适用场景

- 训练分子性质预测等分子建模自定义模型
- 在 Open Catalyst / OGB 数据集上复现或微调模型
- 基于预训练模型开展材料与药物发现相关研究

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L1: Graphormer is a deep learning package that allows researchers and developers to train custom models for molecule mod
> L8: * Supports interface and datasets of PyG, DGL, OGB, and OCP.

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/Graphormer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 2480 --> 2482
    line [2481, 2481]
```

2026-10-18 2,481 → 2026-10-25 2,481（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `ec195e417544` · [字段定义](../../DATASET.md)*
