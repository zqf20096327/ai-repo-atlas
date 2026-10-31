# mverab/WorldCupBench

⭐ 15 · Python · 推送 2026-07-31 · [GitHub](https://github.com/mverab/WorldCupBench) · [官网](https://mverab.github.io/WorldCupBench) · 个人维护

**2026世界杯LLM预测基准：10个前沿模型开赛前冻结预测并实时计分**

LLM 预测能力评测项目：让 10 个前沿模型通过 OpenRouter 接收同一提示词，对 2026 世界杯全部 104 场比赛输出结构化 JSON 预测（含 1X2 概率、比分、晋级树），开赛前冻结不可修改。随真实赛果进行多指标计分：Brier 分数、结果准确率、精确比分、晋级准确率（对真实 32 强按 FIFA 平局规则计分）与逐轮晋级集合准确率，并支持对比 Polymarket ROI。预测带冻结时间戳与审计轨迹，社区可通过 PR 添加新模型或真实赛果。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 同一提示词驱动 10 个模型，赛前冻结、带 freeze-v3 审计轨迹（时间戳/模型检查点/方向归一化）
- 三项核心指标：Brier 分数、结果准确率（argmax）、精确比分
- qualifier_accuracy 按 FIFA 平局规则对真实 32 强计分，含位置加分与误报统计
- advancement_accuracy 逐轮按集合成员计分，仅聚合已完结轮次

## 适用场景

- 对比不同前沿 LLM 在体育赛事上的概率校准与预测能力
- 跟踪 LLM 预测相对真实赛果与 Polymarket 市场的表现
- 通过 PR 用自己的模型加入榜单参与评测

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L21: 1. **Same prompt** → 10 SOTA LLMs via OpenRouter.
> L24: 4. **Scored live** → as real results come in, we compute accuracy, Brier score, and ROI vs Polymarket.
> L80: WorldCupBench scores every model on **three independent metrics**. The

## 星数曲线

```mermaid
xychart-beta
    title "mverab/WorldCupBench 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `0c3b6b085337` · [字段定义](../../DATASET.md)*
