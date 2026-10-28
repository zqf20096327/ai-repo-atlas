# IBazylchuk/paparats-mcp

⭐ 34 · TypeScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/IBazylchuk/paparats-mcp) · [官网](https://www.npmjs.com/package/@paparats/cli) · 个人维护

**自托管语义代码搜索 MCP 服务器：让 AI 编码 agent 跨仓库按含义查代码**

面向 Claude Code、Cursor、Codex、Copilot 等 MCP 客户端的开源自托管 MCP 服务器。本地索引多个仓库：tree-sitter 语法树切分、基于调用图的方法级 find_usages/change_impact、按 chunk 的 git 历史与工单、模块图与 agent 维护的架构记忆。默认用 Qdrant 与本地 llama.cpp 嵌入模型（约 2.3 GB、2–6 GB RAM），代码不出本机；Voyage/OpenAI 云端嵌入与远程 Qdrant 为可选。支持 11 种语言的调用图；索引约 10 分钟增量刷新。提供 Docker Compose 与 npm CLI 两种安装方式，三个端点（coding/support/knowledge）供团队与多个 agent 共享一个索引。跨仓库调用尚未关联。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 跨多仓库按语义搜索代码，附文件行号与调用图
- find_usages / change_impact 给出最多三跳的调用方与受影响测试
- 默认本地嵌入模型（bge-code-v1 / Qwen3-Embedding-0.6B）+ Qdrant，代码不出本机
- 按 chunk 的 git 历史（作者/时间/工单号）与架构记忆、术语表

## 适用场景

- 大型或多仓库代码库上减少 agent 的 grep-阅读上下文消耗
- 改动前查询谁依赖这段代码及受影响测试
- 团队与多个 agent 共享同一索引服务器

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L11: **Paparats MCP is an open-source, self-hosted MCP server that gives Claude Code, Cursor,
> L14: your machine or your server in Docker, with local embedding models by default, so your

## 星数曲线

```mermaid
xychart-beta
    title "IBazylchuk/paparats-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 10 --> 12
    line [11, 11]
```

2026-10-18 11 → 2026-10-28 11（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `18641313358e` · [字段定义](../../DATASET.md)*
