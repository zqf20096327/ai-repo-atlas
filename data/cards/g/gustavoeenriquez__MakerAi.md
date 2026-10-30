# gustavoeenriquez/MakerAi

⭐ 215 · Pascal · MIT · 推送 2026-10-27 · [GitHub](https://github.com/gustavoeenriquez/MakerAi) · [官网](https://www.youtube.com/@cimamaker3945) · 个人维护

**Delphi 原生 AI 应用框架：RAG、自主 Agent、MCP 与多 LLM 接入**

面向 Delphi（10.4+ 有限支持，Delphi 12 Athens 起完整支持）与 Free Pascal/Lazarus（FPC 3.2+，fpc 分支）的 AI 应用开发框架。提供对各 LLM 供应商的原生专用组件（OpenAI、Claude、Gemini、Ollama、Groq、DeepSeek 等）及运行时可切换供应商的通用连接器；在此之上包含向量与图式 RAG 管道（VQL/GQL 查询语言）、带图编排与人工审批的自主 Agent、MCP 服务器/客户端、ChatTools（PDF/视觉/语音/Shell/Computer Use）、SKILL.md 技能、A2A 协议、护栏与 OpenTelemetry 追踪，以及 FMX 可视聊天组件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- RAG 管道（向量与图式）配 SQL 风格的 VQL/GQL 查询语言
- 自主 Agent 图编排，含检查点与 human-in-the-loop 审批
- MCP 服务器与客户端，兼容新版无状态规范与旧握手
- 通用连接器：运行时切换 LLM 供应商而无需改应用代码
- Free Pascal/Lazarus 全量移植（fpc 分支，12 个 LLM 驱动）

## 适用场景

- 在 Delphi 中构建多供应商、检索增强的生产级智能系统
- 通过 MCP 暴露或消费工具，或用 A2A 让 Agent 图互联
- 用 FMX 可视组件快速搭建多模态聊天界面

## 场景标签

`RAG` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L21: But on top of that, MakerAI is a **complete AI application ecosystem** that lets you build production-grade intelli
> L25: - **MCP Servers and Clients** — expose or consume tools using the Model Context Protocol (dual-era: stateless spec 
> L31: - **Universal Connector** — switch providers at runtime without changing your application code

## 星数曲线

```mermaid
xychart-beta
    title "gustavoeenriquez/MakerAi 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-30"]
    y-axis "stars" 213 --> 216
    line [214, 215, 215]
```

2026-10-18 214 → 2026-10-30 215（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `acd309f598c4` · [字段定义](../../DATASET.md)*
