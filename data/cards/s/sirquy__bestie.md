# sirquy/bestie

⭐ 104 · TypeScript · MIT · 推送 2026-10-20 · [GitHub](https://github.com/sirquy/bestie) · [官网](https://bestieagent.com) · 个人维护 · 中文 README

**自托管本地优先的越南语 AI 伴侣运行时，带记忆/技能/权限门控**

TypeScript 编写的 CLI/运行时，用于运行个性化的 AI 伴侣：默认越南语、可编辑角色与提示词文件。支持配置多家 LLM 提供商（OpenAI/Anthropic/Groq/OpenRouter/兼容端点/本地 Ollama，以及 Gemini/Claude/Codex CLI 本地中间件），带提供商诊断与回退顺序。本地 SQLite 记忆、知识图谱 UI、Telegram/Zalo/cron 通道、权限门控的本地工具与 MCP 调用、技能安装与远程注册表、`bestie ui` 本地 Web 控制台。README 明确声明其非人类、非治疗替代。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 本地 SQLite 记忆与知识图谱 UI，配合审批/治理控制
- 多提供商配置：OpenAI/Anthropic/Groq/OpenRouter/Ollama 及 Gemini/Claude/Codex CLI 中间件
- 权限门控工具运行时与 MCP 调用，固定角色 Agent Workforce
- Telegram/Zalo/cron 通道守护进程与技能注册表安装流程

## 适用场景

- 在本地自托管一个可自定义角色的 AI 伴侣并通过 Web UI 对话
- 通过 Telegram/Zalo 与个人 AI 助手交互
- 在权限审批控制下让 AI 执行本地文件与工具操作

## 场景标签

`AI 助手` `聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L5: Bestie is a self-hosted, local-first AI companion runtime with a Vietnamese-first character, local memory, provider 
> L11: - A TypeScript CLI/runtime for running a personalized AI companion.

## 星数曲线

```mermaid
xychart-beta
    title "sirquy/bestie 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-24"]
    y-axis "stars" 104 --> 107
    line [105, 106, 106]
```

2026-10-18 105 → 2026-10-24 106（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `791d3bd99afb` · [字段定义](../../DATASET.md)*
