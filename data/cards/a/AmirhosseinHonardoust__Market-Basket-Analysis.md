# AmirhosseinHonardoust/Market-Basket-Analysis

⭐ 34 · Python · MIT · 推送 2026-05-29 · [GitHub](https://github.com/AmirhosseinHonardoust/Market-Basket-Analysis) · 个人维护

**Python 购物篮分析项目：挖掘频繁项集与关联规则**

可运行的 Python 数据分析项目：先用脚本生成带真实共购偏置的合成零售交易数据（如 Laptop→Mouse/Keyboard/Bag），再基于 mlxtend 用 Apriori 或 FP-Growth 挖掘频繁项集，导出含 support、confidence、lift、leverage、conviction 的关联规则，输出 CSV、Top-N 支持度图表与 summary.json。README 自述面向快速作品集演示；参数如 min_support、min_threshold 可调，README 提示 FP-Growth 在大数据集上通常快于 Apriori。

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

- 合成交易数据生成器，含真实共购偏置，支持指定时间范围/客户数/随机种子
- Apriori 与 FP-Growth 双算法频繁项集挖掘（基于 mlxtend）
- 关联规则计算 support/confidence/lift/leverage/conviction 五种度量
- 产出 CSV、Top-N 支持度图表与 summary.json，保存于 outputs/

## 适用场景

- 零售分析中挖掘商品共购模式并导出关联规则
- 数据科学作品集演示频繁项集挖掘方法
- 在合成数据上复现购物篮分析流程并生成可视化

## 场景标签

 · 领域:数据挖掘/零售分析

## 证据(README 行号)

> L9: - Frequent itemsets via **Apriori** or **FP‑Growth** (mlxtend)
> L10: - Association rules with **support, confidence, lift, leverage, conviction**

## 星数曲线

```mermaid
xychart-beta
    title "AmirhosseinHonardoust/Market-Basket-Analysis 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 32 --> 35
    line [33, 34, 34]
```

2026-10-18 33 → 2026-10-28 34（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `b4f0a8557595` · [字段定义](../../DATASET.md)*
