# recommend-dev/recommend-agentic-trust-layer

⭐ 26 · Python · MIT · 推送 2026-08-31 · [GitHub](https://github.com/recommend-dev/recommend-agentic-trust-layer) · 组织维护

**面向 AI agent 的事实核查层：检验声明是否被真实来源支持**

输入一条声明，系统实时抓取网络来源或用户自有文档，经多证据通道（Exa/SerpAPI/OpenAlex 等）、逐通道裁决、反向质询与校准后输出真值评分（0-100）与独立置信度及来源。支持浏览器单条核查、以 MCP 工具（verify_claim）接入 agent、以及对 Open Knowledge Format 知识库整体打 verified 标记（含引用完整性模式）。限制：每次核查耗时 10-20 秒并消耗 API 额度（内置每日限额），需 Gemini 与 Exa API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多证据通道并行检索+逐通道裁决+反向质询的核查流水线
- 真值评分与置信度两个独立数字，校准步骤只能降低置信度
- MCP 工具接入 agent（verify_claim）
- OKF 知识库批量打标与引用完整性校验模式

## 适用场景

- agent 行动前先核查其将使用的事实声明
- 对共享知识库文档逐条核查并打 verified 标记
- 检验内部文档引用的来源是否真的支持其声明

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3: **A fact-checker for the things you tell your AI agents. It checks a statement against real sources (the web, or you
> L112: Give your agent a `verify_claim` tool and it stops answering factual questions from memory:
> L125: If your agents write into a shared knowledge base (for example in Google's

## 星数曲线

```mermaid
xychart-beta
    title "recommend-dev/recommend-agentic-trust-layer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-26 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `bbe01875e716` · [字段定义](../../DATASET.md)*
