# colapsis/agentid-protocol

⭐ 14 · Python · MIT · 推送 2026-05-16 · [GitHub](https://github.com/colapsis/agentid-protocol) · [官网](https://agentid.live) · 组织维护

**AI agent 持久身份/记忆/协作的示例集（MCP 服务）**

agentid.live 平台的官方示例仓库：通过单个 MCP 服务器为 AI agent 提供持久 URL、共享记忆与协作原语。含 8 个示例（持久记忆、代码审阅、双/三 agent 交接、任务追踪、密钥库等），原语覆盖 write/read/search_memory、start_mission、handoff、get_secret 等。运行需 Python 3.10+ 与免费 AgentID 账号，示例亦可通过配置接入 Claude Desktop、Cursor 等 MCP 客户端。共享工具模块封装 MCP 连接与 Anthropic 工具调用循环。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 8 个真实场景示例覆盖记忆、任务、交接、密钥原语
- 单 MCP 服务器提供持久 URL 与共享记忆，无需自建后端
- 支持接入 Claude Desktop / Cursor / Windsurf 等 MCP 客户端
- get_secret 从 AgentID Drive 读取密钥，不落入配置文件

## 适用场景

- 让 agent 跨会话记住信息并共享记忆
- 搭建多 agent 流水线（researcher→analyst→writer）的交接模式
- 在 Claude Desktop 等客户端中直接使用这些示例 agent

## 场景标签

`多智能体` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L10: AgentID gives your AI agents a persistent URL, shared memory, and coordination primitives via a single MCP server. 
> L47: Every agent gets these tools via its MCP URL (`https://agentid.live/api/mcp/{handle}`).

## 星数曲线

```mermaid
xychart-beta
    title "colapsis/agentid-protocol 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `2a1f347d4409` · [字段定义](../../DATASET.md)*
