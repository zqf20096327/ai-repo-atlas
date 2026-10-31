# RagavRida/agentdom

⭐ 13 · JavaScript · MIT · 推送 2026-05-14 · [GitHub](https://github.com/RagavRida/agentdom) · [官网](https://getagentdom.com) · 个人维护

**让 AI agent 统一调用 REST/浏览器/桌面/CLI 的通用运行时**

AgentDOM 是连接 AI agent 与各类软件的基础设施层：将 intent 路由到合适的执行通道（REST API、CLI 命令、Chrome CDP + DOM 自动化、macOS Accessibility 桌面桥），不做截图与坐标点击。以 npm/pip 包、CLI 和 MCP Server 形式提供，内置策略引擎（approve/deny、外部调用与发送审批）与凭据钱包（本地加密存储或 OS Keychain）。附 Publisher SDK，可从 OpenAPI 规格生成 manifest（.well-known/agentdom.json）把自有 API 暴露给 agent。要求 Node 18+，支持 AWS 一键部署脚本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- intent 四级路由：REST manifest → CLI → Chrome CDP DOM 自动化 → macOS Accessibility
- 内置策略引擎：外部调用白名单、发送前 prompt 审批、approve/deny 命令
- Publisher SDK 从 OpenAPI 规格生成 manifest，mcp-use bridge 可生成 MCP server
- 凭据存于本地钱包（0600）或 OS Keychain，不上传服务端

## 适用场景

- 让 agent 通过统一 intent 协议操作 GitHub/Stripe/Slack 等 SaaS API
- 为自有 API 发布 agentdom.json manifest，供 AI agent 直接调用
- 作为 MCP Server 接入 Claude Desktop 或 Cursor 执行自然语言目标

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L25: - **Runtime** (npm | pip): Routes any intent to the right execution layer — REST API, browser, desktop, or CLI
> L103: dispatch_intent("issues.create", args, "github.com")

## 星数曲线

```mermaid
xychart-beta
    title "RagavRida/agentdom 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `4b3cfedd0c06` · [字段定义](../../DATASET.md)*
