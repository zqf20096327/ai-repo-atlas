# mcp-fe/mcp-fe

⭐ 15 · TypeScript · Apache-2.0 · 推送 2026-07-22 · [GitHub](https://github.com/mcp-fe/mcp-fe) · [官网](https://mcp-fe.ai) · 组织维护

**让 AI Agent 直接读写运行中 React 应用状态的 MCP 框架**

面向前端开发者的 MCP 工具集：通过浏览器 SharedWorker/ServiceWorker 与 Node.js 代理，把运行中的前端（DOM、状态、事件历史）作为 MCP Server 暴露给 Claude/Cursor 等远程 Agent，Agent 可按需调用工具读取实时状态或触发操作，无需浏览器扩展。采用拉取模式，仅在 Agent 显式调用工具时传输数据；内置 WebMCP（navigator.modelContext）适配，支持浏览器原生 Agent 直连。以 monorepo 包形式交付，含核心 worker、事件追踪、React hooks 与 Docker 化代理服务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 浏览器 Worker 作为前端边缘 MCP Server，按需拉取实时状态
- 单次 registerTool 同时服务远程 Agent（WebSocket+代理）与浏览器原生 Agent（WebMCP）
- 零推送策略：数据仅在工具被调用时返回，敏感字段不自动外传
- 事件历史存入 IndexedDB，支持导航/交互/错误记录

## 适用场景

- 给应用内嵌能理解实时界面状态的 AI 副驾驶或客服助手
- 让 Claude/Cursor 直接查询表单状态与校验错误做调试支持
- 在税务表单、ERP 等多步流程中让 Agent 代用户导航与填写

## 场景标签

`浏览器自动化` `AI 助手` · 领域:效率与自动化

## 证据(README 行号)

> L10: MCP-FE turns your browser into an active MCP node — letting agents like Claude or Cursor query live state, read use
> L25: MCP-FE exposes the **browser runtime** as a first-class MCP Server so that context is retrievable **on demand** via

## 星数曲线

```mermaid
xychart-beta
    title "mcp-fe/mcp-fe 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `f7678a8843be` · [字段定义](../../DATASET.md)*
