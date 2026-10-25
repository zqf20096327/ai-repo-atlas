# HazyResearch/hebbian-mlps

⭐ 34 · Python · Apache-2.0 · 推送 2026-07-22 · [GitHub](https://github.com/HazyResearch/hebbian-mlps) · 组织维护

**MLPs are Hebbians 论文实验复现代码库**

HazyResearch 发布的论文《MLPs are Hebbians: Constructing Efficient Fact-Storing MLPs for Transformers》（COLM 2026）配套代码库，用于复现论文实验，涵盖 Hebbian MLP 构造、Transformer 集成、Qwen3 激活实验与事实编辑实验。通过 git clone 加 pip 可编辑安装使用，Qwen3 实验需额外安装 Hugging Face 可选依赖，实验通过 scripts/paper/run.py 命令运行并生成图表。Apache 2.0 许可。

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

- Hebbian MLP 构造与 Transformer 集成实验代码
- Qwen3 激活实验与事实编辑实验复现支持
- scripts/paper/run.py 统一入口运行并绘图

## 适用场景

- 复现 COLM 2026 论文实验结果
- 研究事实编辑与 MLP 参数存储机制
- 在 Qwen3 上运行激活相关实验

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L10: This repository contains the code to replicate the experiments from the paper,
> L11: including Hebbian MLP constructions, Transformer integration, Qwen3 activation

## 星数曲线

```mermaid
xychart-beta
    title "HazyResearch/hebbian-mlps 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-25 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `81a109789188` · [字段定义](../../DATASET.md)*
