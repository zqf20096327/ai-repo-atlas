# pyc-team/pytorch_concepts

⭐ 159 · Python · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/pyc-team/pytorch_concepts) · [官网](https://pytorch-concepts.readthedocs.io/en/latest/) · 组织维护

**基于 PyTorch 的概念化可解释深度学习模型构建库**

PyC（PyTorch Concepts）是构建在 PyTorch 与 PyTorch Lightning 之上的库，用于实现可解释且因果透明的深度学习模型。提供注释张量、概念层、概念损失、干预操作、可解释概率图模型等原语，以及配置文件驱动的大规模实验 API（基于 Hydra 与 WandB）。分层设计：无代码 API、一行实例化的高层 API、图模型中层 API 与底层可解释层。自述为 Alpha 阶段，公开 API 可能不稳定。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 注释张量与概念层等可解释建模原语
- with 块内对概念执行干预（intervention）
- 可解释概率图模型与概率推断
- 基于 Hydra/WandB 的配置驱动大规模实验 API

## 适用场景

- 构建以概念为中间表示的可解释深度学习模型
- 在模型中对概念做干预实验与因果分析
- 用配置文件批量运行可解释模型实验与基准测试

## 场景标签

 · 领域:机器学习/可解释AI

## 证据(README 行号)

> L16:  PyC is a library built upon PyTorch and PyTorch Lightning to easily implement **interpretable and causally transpa
> L17: The library provides primitives for annotated tensors, interpretable layers, interventions, interpretable probabili

## 星数曲线

```mermaid
xychart-beta
    title "pyc-team/pytorch_concepts 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 158 --> 160
    line [159, 159]
```

2026-10-18 159 → 2026-10-28 159（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `30bbb21fbb4a` · [字段定义](../../DATASET.md)*
