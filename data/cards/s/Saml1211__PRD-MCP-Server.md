# Saml1211/PRD-MCP-Server

⭐ 36 · TypeScript · MIT · 推送 2026-03-17 · [GitHub](https://github.com/Saml1211/PRD-MCP-Server) · 个人维护

**通过 MCP 协议生成产品需求文档（PRD）的服务器**

面向 MCP 客户端（Claude Desktop、Cursor、Cline、Roo Code 等）的 Model Context Protocol 服务器，提供 generate_prd、validate_prd 等工具：基于产品描述、用户故事与需求，调用 OpenAI/Anthropic/Gemini/本地模型生成结构化 PRD，AI 不可用时回退到模板生成；另含 PRD 完整性校验（可自定义规则集）与模板增删改查、导入导出。凭据支持 .env 与运行时 update_provider_config 热更新，无需重启。经 NPX、Docker 或源码安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- generate_prd 支持 openai/anthropic/gemini/local/template 多提供方
- AI 不可用时回退到模板生成
- PRD 完整性校验与可定制规则集
- 提供方凭据运行时热更新，无需重启服务器

## 适用场景

- 在 Claude Desktop 或 Cursor 中让 AI 按输入生成完整 PRD
- 对已有 PRD 做规范完整性校验
- 维护并复用不同产品类型的 PRD 模板

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L8: A specialized Model Context Protocol (MCP) server dedicated to creating Product Requirements Documents. This MCP ser
> L38: - **Multi-Provider Support**: Choose from OpenAI, Google Gemini, Anthropic Claude, or local models
> L43: - **MCP Protocol Support**: Implements the Model Context Protocol for seamless integration with MCP clients

## 星数曲线

```mermaid
xychart-beta
    title "Saml1211/PRD-MCP-Server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-31 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `b1293c66d5ca` · [字段定义](../../DATASET.md)*
