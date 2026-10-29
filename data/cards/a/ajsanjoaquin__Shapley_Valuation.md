# ajsanjoaquin/Shapley_Valuation

⭐ 28 · Python · MIT · 推送 2026-06-01 · [GitHub](https://github.com/ajsanjoaquin/Shapley_Valuation) · 个人维护

**PyTorch 复现的 TMC-Shapley 数据估值方法**

对 ICML 2019 论文 What is your data worth? Equitable Valuation of Data（Ghorbani & Zou）的 PyTorch 复现：通过截断蒙特卡洛采样计算 Shapley 值，为神经网络训练数据的重要性排序，可应用于剔除有害训练样本或按多来源数据的贡献分配补偿。当前仅支持分类准确率作为性能度量，且缺少重训练步骤（作者欢迎 PR 修复）。面向机器学习研究者使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- TMC-Shapley 数据估值的 PyTorch 实现
- Shapley 值满足空数据/平等性/可加性三条性质
- 输出采样 Shapley 值的 pickle 文件，可转为 numpy 数组

## 适用场景

- 评估各训练样本对模型性能的贡献
- 清理有害训练数据
- 按数据贡献为多来源数据分配补偿

## 场景标签

 · 领域:机器学习/数据估值

## 证据(README 行号)

> L4: This is a PyTorch reimplementation of Computing Shapley Values via Truncated Monte Carlo sampling from
> L17: Computing Shapley values help when you need a system to rank the importance of your training data,

## 星数曲线

```mermaid
xychart-beta
    title "ajsanjoaquin/Shapley_Valuation 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-29 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `9224ae82b7b7` · [字段定义](../../DATASET.md)*
