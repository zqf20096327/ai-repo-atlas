# atfortes/LLMSymbolicReasoningBench

⭐ 23 · Python · 推送 2026-08-13 · [GitHub](https://github.com/atfortes/LLMSymbolicReasoningBench) · 个人维护

**LLM 符号与逻辑推理评测数据集的合成生成实现集合**

收录并复现符号与逻辑推理任务数据集生成方法的仓库：针对未公开或无官方实现的数据集提供可复现的生成代码，每个数据集以子目录形式包含 README、依赖文件与生成代码，并附小型示例片段（如 coin-flip、last-letter-concatenation）。当前列出 Coin Flip、首/末字母拼接、Reverse List、Strawberry 五个数据集，另列 Reversal Curse 相关数据集。仓库接受社区按目录结构规范提交 PR 扩充数据集。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供缺失官方实现的数据集生成代码，便于复现
- 每个数据集子目录含 README、requirements.txt 与示例
- 已含 Coin Flip、字母拼接、Reverse List、Strawberry 等 5 个数据集
- 按目录结构规范接受社区 PR 贡献新数据集

## 适用场景

- 为 LLM 符号/逻辑推理评测生成合成数据集
- 复现论文或社区中缺少公开实现的评测数据
- 参考 PR 模板贡献自己设计的推理数据集生成方法

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: This repository is dedicated to generating datasets for symbolic and logic reasoning tasks in LLMs. Our goal is to p
> L39: - Coin Flip

## 星数曲线

```mermaid
xychart-beta
    title "atfortes/LLMSymbolicReasoningBench 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-31 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `8b867bea86fb` · [字段定义](../../DATASET.md)*
