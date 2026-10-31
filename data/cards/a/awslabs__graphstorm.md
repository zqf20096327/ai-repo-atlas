# awslabs/graphstorm

⭐ 455 · Python · Apache-2.0 · 推送 2026-06-30 · [GitHub](https://github.com/awslabs/graphstorm) · 组织维护

**面向 ML 科学家的十亿级图机器学习训练框架**

AWS 开源的企业级图机器学习（GML）框架，用于在数十亿节点/边规模的工业图上训练与部署 GML 模型。提供内置 GML 模型集合，支持单命令零代码训练与推理、分布式训练/推理，以及通过编程接口分布式训练用户自定义 GML 模型；支持 CPU 或 NVIDIA GPU。要求 Python 3.8+、PyTorch 1.13+、DGL 1.0+ 与 transformers 4.3.0+，可通过 pip 本地安装，分布式场景推荐配合 Amazon SageMaker AI 使用。附带 OGB arxiv 节点分类与链接预测的快速上手示例。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单命令完成 GML 模型训练与推理，无需编写代码
- 十亿级节点/边的分布式训练与推理
- 内置 GML 模型集合与大量配置项
- 提供编程接口以分布式方式训练自定义 GML 模型

## 适用场景

- 我在工业规模图数据上训练节点分类或链接预测模型
- 我需要用自定义 GNN 模型实现扩展到大规模图
- 我用一条命令完成 GML 模型的训练与推理流程

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L9: GraphStorm is an enterprise-grade graph machine learning (GML) framework designed for scalability and ease of use.
> L12: GraphStorm provides a collection of built-in GML models and users can train a GML model
> L20: - Single-command GML model training and inference

## 星数曲线

```mermaid
xychart-beta
    title "awslabs/graphstorm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 454 --> 456
    line [455, 455]
```

2026-10-18 455 → 2026-10-31 455（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `44fcc39297ab` · [字段定义](../../DATASET.md)*
