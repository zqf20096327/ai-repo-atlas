# nla-group/rote

⭐ 15 · Python · MIT · 推送 2026-10-03 · [GitHub](https://github.com/nla-group/rote) · 组织维护

**复杂度受控符号序列的学习与外推复现基准**

ROTE（Rollout Testing of Exact memorization）生成指定 LZW 复杂度的符号序列种子，训练有限上下文的下一符号预测模型，并评测教师强制预测与闭环 rollout 外推，报告 DL/JW 距离等指标。面向研究神经记忆与外推能力的科研用户。包含固定预算多模型对比（LSTM/GRU/minGRU/Transformer/LinearAttention/Performer/RWKV 式等）与匹配参数量检查，附 Slurm 脚本、结果合并与可视化流程。当前从源码安装，Python 3.10+，核心依赖 NumPy 与 pandas，可选 PyTorch 等神经依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 按指定 LZW 复杂度生成符号序列种子
- 同时评测教师强制预测与闭环 rollout 外推（DL/JW 距离）
- 内置 LSTM/GRU/minGRU/Transformer/LinearAttention/Performer/RWKV 式模型对比
- 提供 Python API、CLI、Slurm 脚本与可视化流程

## 适用场景

- 评测自研下一符号预测模型的记忆与外推能力
- 复现论文中的复杂度扫描与匹配参数量实验
- 研究序列复杂度对神经模型外推表现的影响

## 场景标签

`模型评测` `科研工具` · 领域:评测与运维

## 证据(README 行号)

> L9: **ROTE** (Rollout Testing of Exact memorization) is a reproducible benchmark for learning and extending controlled s
> L82: The main track compares LSTM, GRU, minGRU, minLSTM, Transformer, LinearAttention, Performer, and a compact RWKV-sty

## 星数曲线

```mermaid
xychart-beta
    title "nla-group/rote 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `82f50e007fae` · [字段定义](../../DATASET.md)*
