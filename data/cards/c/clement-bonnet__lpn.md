# clement-bonnet/lpn

⭐ 116 · Jupyter Notebook · Apache-2.0 · 推送 2025-11-25 · [GitHub](https://github.com/clement-bonnet/lpn) · 个人维护

**NeurIPS 2025 论文《Searching Latent Program Spaces》官方代码**

Latent Program Network（LPN）的论文官方实现：一种归纳式程序合成架构，通过学习可用于搜索的潜在空间实现测试时自适应。仓库基于 JAX 提供 hydra 配置、re-arc 数据处理工具、模型架构与训练脚本；安装需先按官方文档装 JAX，再克隆仓库、设置 PYTHONPATH、pip 安装依赖，并配置 HuggingFace token 与 WandB API key。Apache 2.0 许可，面向论文复现与研究人员。

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

- 学习潜在空间的归纳程序合成架构，支持测试时自适应
- 提供 hydra 配置、re-arc 数据处理与训练脚本
- ARC Prize 2024 第三名论文奖、NeurIPS 2025 spotlight 论文代码

## 适用场景

- 复现论文中的 LPN 训练与实验
- 在 ARC 类归纳推理任务上开展研究
- 基于潜在程序空间搜索开展后续研究

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L2: Code for the paper _Searching Latent Program Spaces_, 3rd paper award at ARC Prize 2024, and published at NeurIPS 20
> L11: The LPN is an architecture for inductive program synthesis that builds in test-time adaption by learning a latent s
> L41: python src/train.py --config-name pattern_2d

## 星数曲线

```mermaid
xychart-beta
    title "clement-bonnet/lpn 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-29"]
    y-axis "stars" 114 --> 117
    line [115, 116, 116]
```

2026-10-18 115 → 2026-10-29 116（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `06ae484bf3e0` · [字段定义](../../DATASET.md)*
