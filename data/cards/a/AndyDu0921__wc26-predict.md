# AndyDu0921/wc26-predict

⭐ 32 · Python · MIT · 推送 2026-07-22 · [GitHub](https://github.com/AndyDu0921/wc26-predict) · 个人维护 · 中文 README

**2026 世界杯预测研究系统：7 级融合模型与无泄漏回测**

面向足球预测研究的工程系统，含 FastAPI 后端、Streamlit Dashboard 与 SQLite 数据库。核心机制：Dixon-Coles、Elo、Pi-Rating、Weibull、市场赔率等 7 级顺序融合，加 Stacking 元学习器与加权共形预测；强调赛前信息状态快照、walk-forward 回测、数据泄漏保护与输入/权重/校准版本留存。V4.11 引入 FIFA 官方赛后数据、事件时间线与比赛状态分段作为复盘学习资产。限制：strict 回测样本仅 37 场，候选模型只能进入 shadow/proposal 流程；明确声明不提供赛事情境决策建议。运行需配置多个 API Key（市场赔率必需、LLM 可选）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 7 级顺序融合预测链（DC/NegBin/Weibull/Elo/Pi/Market）+ Stacking 元学习器 + 加权共形预测
- walk-forward 回测门：按 T-24h/T-6h/T-90m 真实时间模拟，主指标为 log loss/Brier/RPS
- 赛前信息状态快照与数据泄漏保护（输入 hash、数据时间戳、版本留存）
- V4.11 Match Data OS：FIFA 官方赛后数据、事件时间线、比赛状态分段的可追溯复盘

## 适用场景

- 在无泄漏前提下做世界杯比赛结果的概率预测研究
- 对比候选模型与传统基准在 walk-forward 回测中的表现
- 赛后复盘预测误差并生成自进化提案（proposal-only，需人工批准）

## 场景标签

 · 领域:体育预测/统计建模研究

## 证据(README 行号)

> L37: - **预测流水线**：DC → Enhancer → NegBin(5%) → Weibull → Elo → Pi → Market（7 级顺序融合）+ 战意因子 + 平局下限 12% + 分歧自适应 + 动态市场提升 + D
> L283: - **Fusion chain**: DC → Enhancer → NegBin(5%) → Weibull → Elo → Pi → Market (7-stage sequential fusion) + motivat
> L293: This is not a commercial tipping product. It is an engineering system for football prediction research, pre-match 

## 星数曲线

```mermaid
xychart-beta
    title "AndyDu0921/wc26-predict 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-27 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `54ec055d9cce` · [字段定义](../../DATASET.md)*
