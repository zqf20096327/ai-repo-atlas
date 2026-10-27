# pubnub/pubnub-mcp-server

⭐ 33 · TypeScript · NOASSERTION · 推送 2026-10-22 · [GitHub](https://github.com/pubnub/pubnub-mcp-server) · [官网](https://www.npmjs.com/package/@pubnub/mcp) · 组织维护

**向 LLM 工具暴露 PubNub 文档与 API 的 MCP 服务器**

PubNub 官方维护的 Model Context Protocol 服务器，把 20+ 语言的 SDK 文档、应用与 keyset 管理、实时消息收发、用户/频道管理、Presence、Illuminate 与 Insights 分析等能力以 MCP 工具形式提供给 Cursor、VS Code、Claude Code/Desktop、Codex、Gemini CLI 等 AI 助手。提供托管版（https://mcp.pubnub.com，HTTP + OAuth，免安装）与本地版（npx @pubnub/mcp@latest，stdio，需 Node.js ≥20，API key 可选解锁更多功能），用 TypeScript 编写并附带测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 托管版免安装，OAuth 自动认证；本地版用 npx 运行
- 覆盖 SDK 文档查询、应用/keyset 管理、实时消息收发、App Context CRUD
- 提供 HIPAA 合规聊天与 React 应用脚手架等内置 prompts
- 支持 8 种以上 MCP 兼容 AI 客户端的接入配置说明

## 适用场景

- 在 IDE 内让 AI 助手查阅 PubNub SDK 文档并生成代码
- 通过 AI 助手管理 PubNub 应用、keyset 与实时消息通道
- 用内置 prompts 快速搭建 HIPAA 合规聊天或 React 实时应用

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L3: A hosted Model Context Protocol (MCP) server that exposes PubNub SDK documentation and PubNub API resources to LLM-p
> L17: - **🔧 Multi-Platform Integration** - Works with Cursor, Visual Studio Code, Claude Code, and other MCP-compatible A

## 星数曲线

```mermaid
xychart-beta
    title "pubnub/pubnub-mcp-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-27 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `386ba29e5459` · [字段定义](../../DATASET.md)*
