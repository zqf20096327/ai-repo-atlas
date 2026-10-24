# olivkoch/nano-trm

⭐ 129 · Python · MIT · 推送 2026-03-30 · [GitHub](https://github.com/olivkoch/nano-trm) · 个人维护

**Tiny Recursive Models (TRM) 的精简 PyTorch 训练实现**

提供 TRM（ARC-AGI 2 竞赛头名论文的递归模型）的独立实现，基于 hydra、PyTorch Lightning 与 uv 构建实验流程，包含 TRM 模型定义、训练脚本与实验配置。附带小型 Sudoku 数据集（4x4/6x6），可在 A10 上几分钟完成训练；另提供 Sudoku Extreme 与 Maze Hard 数据生成与复现流程（验证集精确准确率约 87% 与 75%），以及评估与 gif 可视化脚本。面向希望在自有任务上实验 TRM 的研究与工程用户；官方结果的复现在 H100 上需 1-2 小时。

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

- TRM 模型实现与 hydra/Lightning 实验配置
- 小数据集（Sudoku 4x4/6x6）可在 A10 上几分钟训练
- 复现 Sudoku Extreme（约 87%）与 Maze Hard（约 75%）流程
- 评估与 gif 可视化脚本

## 适用场景

- 复现 TRM 在 Sudoku Extreme / Maze Hard 上的结果
- 在自有任务（如 ARC-AGI）上实验 TRM
- 低成本入门递归模型训练（A10 数分钟级）

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L10: This is an implementation of the Tiny Recursive Model (TRM).
> L20: We propose a clean implementation of TRM. We call it "nano" because it is easy to experiment with, yet incorporates

## 星数曲线

```mermaid
xychart-beta
    title "olivkoch/nano-trm 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-24"]
    y-axis "stars" 127 --> 130
    line [128, 129, 129]
```

2026-10-18 128 → 2026-10-24 129（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `bcbe6fba7e3d` · [字段定义](../../DATASET.md)*
