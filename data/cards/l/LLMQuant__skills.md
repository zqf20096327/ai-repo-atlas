# LLMQuant/skills

⭐ 236 · Shell · MIT · 推送 2026-05-30 · [GitHub](https://github.com/LLMQuant/skills) · [官网](https://llmquantdata.com/agent) · 组织维护 · 中文 README

**面向金融 Agent 的技能目录：18 类工作流接入 LLMQuant Data**

LLMQuant 维护的金融 agent 技能目录仓库：以类别文件夹为安装单元，每个含路由 SKILL.md 索引 workflows/*.md，指引 agent 加载对应工作流并执行 LLMQuant Data 证据契约。覆盖股票、期权、ETF、宏观、加密、信用、风险、组合等 18 类。通过 npx skills add 一键安装到 Claude Code、Codex、Cursor、Antigravity 等宿主 agent；无数据 MCP 连接时仍可作为通用工作流运行，缺失数据会被标注。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 18 个类别技能，每个含路由 SKILL.md 与 workflows 索引
- npx skills add 跨 Claude Code/Codex/Cursor 等宿主自动检测安装
- 技能以自然语言声明数据需求，由 agent 路由到 LLMQuant Data MCP
- 无 MCP 连接时仍可作为可复用工作流运行并标注缺失数据

## 适用场景

- 为投研 agent 安装股票、期权、宏观等金融分析技能
- 让研究结论以 LLMQuant 数据为证据来源
- 在多个编码 agent（Claude Code/Cursor 等）间复用同一套金融工作流

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L28: This repository is a **skill catalog**. The install/import unit is a category folder under `skills/llmquant-*` — ea
> L20: > 18 category skills — equities, options, macro, crypto, credit, portfolio, risk, and more — that route an agent to

## 星数曲线

```mermaid
xychart-beta
    title "LLMQuant/skills 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-28"]
    y-axis "stars" 233 --> 236
    line [234, 235, 235]
```

2026-10-18 234 → 2026-10-28 235（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `5f17954a25cc` · [字段定义](../../DATASET.md)*
