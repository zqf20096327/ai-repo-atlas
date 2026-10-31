# mondaycom/agent-tool-protocol

⭐ 101 · TypeScript · MIT · 推送 2026-08-10 · [GitHub](https://github.com/mondaycom/agent-tool-protocol) · [官网](https://agenttoolprotocol.com) · 组织维护

**让 AI agent 以沙箱代码执行方式调用外部系统的协议与运行时**

由 monday.com 维护的 Agent Tool Protocol（ATP）：LLM 生成 TypeScript/JavaScript 代码，在隔离 V8 沙箱（内存限制、超时、无 Node 访问）中执行，从而并行调用多个 API、过滤转换数据并链式组合操作。提供 atp.* 运行时 SDK（LLM 调用、embedding、审批、缓存、日志）、OpenAPI 与 MCP 兼容适配、LangChain/LangGraph 客户端工具，以及来源追踪等防提示注入的安全机制。面向构建生产级 AI agent 的开发者，以 npm 包分发；需 Node.js 18+，isolated-vm 依赖本地原生编译。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LLM 生成代码在隔离 V8 VM 中执行（内存限制、超时、AST 校验）
- atp.* 运行时 SDK：LLM 调用、embedding、人审审批、缓存、日志
- OpenAPI 与 MCP 兼容，单服务器可接入多个 API/MCP
- provenance 来源追踪与数据外泄防护等安全策略

## 适用场景

- 构建需要并行调用多个 API 并就地处理数据的 agent
- 用 LangChain/LangGraph agent 接入外部系统
- 对 agent 代码执行施加沙箱隔离与审计日志

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L7: Agent Tool Protocol (ATP) is a next-generation protocol that enables AI agents to interact with external systems by 
> L12: - **Runtime SDK** (`atp.*`) for LLM calls, embeddings, approvals, caching, and logging
> L14: - **Client tools** for seamless integration with LangChain, LangGraph, and other frameworks

## 星数曲线

```mermaid
xychart-beta
    title "mondaycom/agent-tool-protocol 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-28", "2026-10-31"]
    y-axis "stars" 99 --> 102
    line [101, 100, 101, 101]
```

2026-10-18 101 → 2026-10-31 101（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `9880898eb78d` · [字段定义](../../DATASET.md)*
