# junduck/overthink

⭐ 23 · Python · MIT · 推送 2026-04-23 · [GitHub](https://github.com/junduck/overthink) · 个人维护

**受 HRM 启发的小型 Transformer 股市日内预测模型**

面向量化/机器学习开发者的股市日内时序预测模型实现：受 Sapient Intelligence 的层级推理模型（HRM）启发，用浅层 Transformer 堆叠加深层推理循环替代大模型，推理时部分迭代以 no_grad 运行以平衡内存带宽与计算效率。附带机制包括 FiLM 条件调制（注入市场指标/宏观特征）、日内时间相位编码、多尺度趋势损失。提供 example.py / example_film.py / Jupyter notebook 示例，通过 uv 运行，MIT 许可。README 未给出实际回测结果数据。

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

- 浅层 Transformer + 深层递归推理循环的架构设计
- FiLM 条件调制注入市场指标或宏观数据
- 日内交易时段时间相位编码与多尺度趋势损失
- 支持 decoder-only、RoPE、teacher forcing 等配置项

## 适用场景

- 我在做日内股票价格预测，想要一个可直接运行的模型实现
- 我想研究 HRM 类层级推理架构在金融时序上的效果
- 我需要在预测中融入宏观或市场指标作为条件特征

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L3: Overthink implements a hierarchical reasoning model for stock market intraday forecasting.
> L40: Instead of creating a large deep tranformer model, Overthink creates a shallow stack of transformer layers but runn

## 星数曲线

```mermaid
xychart-beta
    title "junduck/overthink 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-29 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `1bb5606a3584` · [字段定义](../../DATASET.md)*
