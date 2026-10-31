# lucidrains/h-net-dynamic-chunking

⭐ 80 · Python · MIT · 推送 2026-10-29 · [GitHub](https://github.com/lucidrains/h-net-dynamic-chunking) · 个人维护

**H-net 动态分块机制的 PyTorch 实现，供序列建模研究**

lucidrains 对 CMU Hwang 等人 H-net 论文中动态分块机制的独立 PyTorch 实现。提供 DynamicSequenceChunker 模块，支持构建多层层级结构（如 3 层），并有 HNet 包装器供在模型中使用。通过 pip 以 h-net-dynamic-chunking 包安装；附 Enwik8 双层级训练示例（需额外安装 examples 可选依赖并运行 train.py）。属于研究性代码，引用对应论文 Dynamic Chunking for End-to-End Hierarchical Sequence Modeling。

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

- DynamicSequenceChunker 模块的 PyTorch 实现
- 支持多层层级结构（如 3 层）与 HNet 包装器
- 提供 Enwik8 数据集 2 层级训练示例

## 适用场景

- 在层级序列建模任务中试验动态分块机制
- 复现或扩展 H-net 论文中的分块组件

## 场景标签

 · 领域:深度学习/序列建模

## 证据(README 行号)

> L5: Implementation of the dynamic chunking mechanism in H-net by Hwang et al. of Carnegie Mellon
> L16: import torch

## 星数曲线

```mermaid
xychart-beta
    title "lucidrains/h-net-dynamic-chunking 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 79 --> 81
    line [80, 80]
```

2026-10-18 80 → 2026-10-31 80（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `a2362ba92952` · [字段定义](../../DATASET.md)*
