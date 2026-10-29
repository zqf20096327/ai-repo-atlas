# VforVitorio/F1-StratLab

⭐ 30 · Python · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/VforVitorio/F1-StratLab) · [官网](https://f1stratlab.com/) · 个人维护

**F1 赛事回放与多智能体进站策略模拟平台**

开源多智能体 AI 平台：六个专项策略 agent（节奏/轮胎/局势/进站/车队无线电/规则）由蒙特卡洛编排器协调，在逐圈 2D 赛事回放中输出可解释的每圈策略建议。数据来自 FastF1/OpenF1，模型含 XGBoost、TCN+MC Dropout、LightGBM、Whisper 与基于 Qdrant 的 FIA 规则检索。提供 CLI、Arcade 桌面回放、React Web 分析三种运行方式；需 Python 3.10-3.12 与 OPENAI_API_KEY（或 LM Studio）。本项目为本科毕业设计。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 六个专项 agent + 蒙特卡洛编排器，逐圈输出可解释策略
- 2D 逐圈赛事回放（Arcade）与赛后分析 Web 应用（React+FastAPI）
- 车队无线电转录与 NLP（Whisper/RoBERTa/SetFit/BERT-large）
- 基于 Qdrant+BGE-M3 的 FIA 规则检索

## 适用场景

- 回放真实 F1 比赛并查看逐圈策略建议与依据
- 赛后遥测分析与车手对比
- 通过自然语言对话查询已完成的比赛

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L9: F1 StratLab is an open-source multi-agent AI platform for Formula 1 race replay and real-time strategy simulation. R
> L31: In Formula 1, strategic decisions must be made within seconds while juggling weather, tire wear, track position, an
> L38: - Six specialised strategy agents (pace, tire, race situation, pit, radio, regulations) plus a Monte Carlo orchestr

## 星数曲线

```mermaid
xychart-beta
    title "VforVitorio/F1-StratLab 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-29"]
    y-axis "stars" 28 --> 31
    line [29, 30, 30]
```

2026-10-18 29 → 2026-10-29 30（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `2ed239bcc778` · [字段定义](../../DATASET.md)*
