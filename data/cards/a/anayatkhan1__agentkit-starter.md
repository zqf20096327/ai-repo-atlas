# anayatkhan1/agentkit-starter

⭐ 39 · TypeScript · MIT · 推送 2026-10-23 · [GitHub](https://github.com/anayatkhan1/agentkit-starter) · [官网](https://agentkitt.xyz) · 个人维护

**带网页搜索的 AI agent 聊天应用生产级启动模板**

基于 Next.js 16 + TypeScript 的 AI 聊天应用起始模板：内置流式对话界面、可开关的网页搜索（Parallel Search MCP 免 key 匿名模式，或配置 Exa）、Clerk 用户认证、Prisma + PostgreSQL 会话持久化，模型接入 Anthropic Claude Sonnet 4.5（Vercel AI SDK）。面向需要快速搭建带认证与持久化 AI 聊天产品的开发者，提供 git clone + pnpm 安装流程，优化 Vercel 部署；运行需 Node.js 18+、PostgreSQL、Clerk 账号与 Anthropic API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 网页搜索开关：Parallel Search MCP 免 key 匿名端点或 Exa 可选后端
- Clerk 认证 + Prisma/PostgreSQL 用户级会话持久化
- 流式响应、来源引用卡片与工具调用可视化
- pnpm test:web-search 提供无需 API key 的确定性测试

## 适用场景

- 快速启动一个带登录和聊天记录的 AI 聊天应用
- 搭建可搜索网页获取实时信息的 AI agent
- 作为可定制的 agent 项目基础（改提示词/加工具/换模型）

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L3: AgentKit is a production-ready starter template for building AI agents with web search capabilities. It's designed t
> L24: - Vercel AI SDK
> L144: Search uses Parallel Search MCP when no search provider or Exa key is configured. It connects to `https://search.p

## 星数曲线

```mermaid
xychart-beta
    title "anayatkhan1/agentkit-starter 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 38 --> 40
    line [39, 39]
```

2026-10-18 39 → 2026-10-26 39（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `5617c667ca2c` · [字段定义](../../DATASET.md)*
