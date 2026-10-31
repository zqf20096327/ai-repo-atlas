# ifmelate/n8n-workflow-builder-mcp

⭐ 52 · JavaScript · MIT · 推送 2026-10-17 · [GitHub](https://github.com/ifmelate/n8n-workflow-builder-mcp) · 个人维护

**供 AI agent 用自然语言生成 n8n 工作流 JSON 的 MCP server**

MCP 服务器，向 Claude Code、VS Code、Cursor 等 MCP 客户端提供约 20 个工具，用于本地创建、编辑、连接与校验 n8n 工作流 JSON 文件，无需运行中的 n8n 实例。内置节点目录覆盖 n8n 1.86.0–2.6.2（184+ 版本），按版本过滤 node typeVersion 并做向下兼容匹配；支持 AI 组件布线（agent/model/memory/embeddings/vector store）、一次性 compose_ai_workflow 组合与非破坏性规划-审查-应用流程。API key 仅用于版本检测，设置 N8N_VERSION 可完全离线。execute 工具未实现；2.6.2 之后新增节点不在目录内。

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

- 本地写入 n8n 工作流 JSON，无需运行 n8n 实例，可完全离线
- 内置节点目录覆盖 184+ n8n 版本（1.86.0–2.6.2），按版本匹配 typeVersion
- AI 组件专用工具：add_ai_connections / connect_main_chain / compose_ai_workflow
- plan→review→apply 的非破坏性规划与原子写入机制

## 适用场景

- 用对话式 AI 客户端离线生成 n8n 工作流文件并导入或提交 git
- 在旧版自托管 n8n 上生成实例实际支持的 typeVersion 工作流
- 让 AI agent 一步组装含模型、记忆、向量库的 n8n AI 工作流

## 场景标签

`工作流自动化` `代码生成` · 领域:效率与自动化

## 证据(README 行号)

> L3: A Model Context Protocol (MCP) server for building and manipulating n8n workflows. Build n8n workflows just by promp
> L11: This server writes n8n workflow **JSON files locally**. It doesn't need a running n8n instance, and it picks node v
> L34: - **AI-Friendly Interface**: Designed specifically for interaction with AI agents

## 星数曲线

```mermaid
xychart-beta
    title "ifmelate/n8n-workflow-builder-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 51 --> 53
    line [52, 52]
```

2026-10-18 52 → 2026-10-31 52（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `b499ef7b6c80` · [字段定义](../../DATASET.md)*
