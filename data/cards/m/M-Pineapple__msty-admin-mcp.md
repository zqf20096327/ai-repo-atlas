# M-Pineapple/msty-admin-mcp

⭐ 14 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/M-Pineapple/msty-admin-mcp) · [官网](https://glama.ai/mcp/servers/M-Pineapple/msty-admin-mcp) · 个人维护

**管理 Msty Studio Desktop 的 MCP 服务器，含 56 个管理工具**

面向 Msty Studio Desktop 2.9+ 的 Python MCP 服务器，提供 56 个工具、分 9 个阶段：自动检测 Studio 安装路径与 SQLite 数据库（只读打开）、清点 personas/知识栈/工作区等实体、读取 insights 分析指标、检测并查询本地推理服务（Ollama/MLX/llama.cpp/Nexus）、基于 Anthropic Bloom 的行为评测（谄媚/幻觉等），以及将本地模型无法回答的问题转发给本机 Cursor agent 的 handoff 机制。以 pip 安装，支持 stdio 与 HTTP 两种传输，需 Python 3.10+；数据库写入默认拒绝，导入走 Toolbox JSON。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 56 个 MCP 工具覆盖安装检测、清单、分析、校准、Bloom 评测与 Nexus 桥接
- 只读打开 Studio SQLite，SQL 查询中凭证类列强制返回 NULL
- 本地模型到 Cursor agent 的 ask_frontier 单工具转发机制
- 支持 Ollama/MLX/llama.cpp/Nexus 多后端本地模型查询

## 适用场景

- 用自然语言管理 Msty Studio 的安装、健康状态与实体清单
- 查看本地模型性能指标并做 Bloom 行为评测
- 让本地模型把难题转交给 Cursor agent 并在 Msty 对话中返回答案

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L12: Comprehensive MCP server for administering **Msty Studio Desktop 2.9+** with **56 tools** across 9 phases: real Stu
> L86: Once the server is registered with Msty Studio (or another MCP host), ask in natural language. The host maps your w
> L149: ├── Local AI (Ollama) → port 11964

## 星数曲线

```mermaid
xychart-beta
    title "M-Pineapple/msty-admin-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `53d2390f0e08` · [字段定义](../../DATASET.md)*
