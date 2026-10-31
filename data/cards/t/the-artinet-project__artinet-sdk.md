# the-artinet-project/artinet-sdk

⭐ 47 · TypeScript · Apache-2.0 · 推送 2026-02-20 · [GitHub](https://github.com/the-artinet-project/artinet-sdk) · [官网](https://artinet.io/) · 组织维护

**一行代码构建 A2A 协议兼容 agent 的 TypeScript SDK**

面向开发者的 AgentExecutor 库，基于 Agent2Agent (A2A) 协议为任意 agent 添加标准化、可互操作的通信层。核心机制：cr8 快速创建 A2A 兼容 agent（可挂载 Express 服务器、嵌入应用内、部署到 AWS Lambda）、dock 将 OpenAI/Claude/LangChain 等框架的 agent 接入、AgentMessenger 客户端连接远程 A2A 服务器、cr8 编排本地与远程多 agent 协作。内置 SQLiteStore 任务存储，可插拔 Pino/Winston 日志与 OpenTelemetry 追踪，兼容 MCP。要求 Node.js ≥ 18.9.1，Apache 2.0 许可。

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

- cr8 一行代码创建并启动 A2A 兼容 Express 服务器
- dock 接入 OpenAI、Claude、LangChain 等框架的 agent
- 支持 AWS Lambda 等 serverless 部署与应用内嵌入
- 内置 SQLiteStore（drizzle-orm）持久化与可插拔日志/追踪

## 适用场景

- 让不同框架的 agent 通过 A2A 协议互相通信
- 把现有 agent 快速封装为 A2A 服务器对外提供服务
- 本地与远程 agent 的多 agent 编排

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L13: The <u>@artinet/sdk</u> is a universal, robust and production ready <code>AgentExecutor</code> library that adds a 
> L15: > Runs on the Agent2Agent (A2A) Protocol from the Agentic AI Foundation.

## 星数曲线

```mermaid
xychart-beta
    title "the-artinet-project/artinet-sdk 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 46 --> 48
    line [47, 47]
```

2026-10-18 47 → 2026-10-31 47（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `178006df1b86` · [字段定义](../../DATASET.md)*
