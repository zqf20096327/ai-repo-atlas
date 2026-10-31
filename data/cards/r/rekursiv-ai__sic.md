# rekursiv-ai/sic

⭐ 15 · Python · Apache-2.0 · 推送 2026-04-01 · [GitHub](https://github.com/rekursiv-ai/sic) · [官网](https://rekursiv.ai) · 个人维护

**研究论文配套实验代码：时间即置信度训练 TRM 解数独**

收录 Speed is Confidence 论文及其实验代码。提出 halt-first ensembling 与 WTA 训练方法：在推理时选取最先停止的模型，实现 97% 数独准确率且减少 10 倍推理步数；通过维护 K=4 并行潜状态仅反传最低损失胜者，在 1 倍推理成本下达到 96.9%。代码基于 Tiny Recursive Models（TRM）与 HRM 改进，全部实验在单张 RTX 5090 上完成，采用修改的 SwiGLU 配合 Muon 优化器与高学习率。Apache-2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- halt-first ensembling 在 Sudoku-Extreme 达到 97% 准确率，推理步数减少 10 倍
- WTA 训练（K=4 并行潜状态）以 1 倍推理成本匹配集成性能
- 基线训练 48 分钟、完整 WTA 6 小时（单张 RTX 5090）
- 修改的 SwiGLU 使 Muon 优化器与高学习率可用

## 适用场景

- 复现论文中 WTA/halt-first 集成的训练实验
- 研究时间即置信度与胜者通吃机制在小型递归模型上的应用
- 在有限算力下进行推理类任务的训练实验

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L3: This repository contains the "Speed is Confidence" research paper and its associated experiments.
> L13: We apply this principle to Tiny Recursive Models (TRM) [Jolicoeur-Martineau et al., 2025]. On Sudoku-Extreme, a bas
> L15: Halt-first ensembling unlocks this potential: by selecting the first model to halt, we achieve 97% accuracy vs. 91%

## 星数曲线

```mermaid
xychart-beta
    title "rekursiv-ai/sic 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `239bec6a3782` · [字段定义](../../DATASET.md)*
