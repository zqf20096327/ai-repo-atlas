# rockywuest/qdrant-mcp-pi5

⭐ 15 · JavaScript · MIT · 推送 2026-10-17 · [GitHub](https://github.com/rockywuest/qdrant-mcp-pi5) · 个人维护

**树莓派 5 上的 AI agent 本地语义记忆方案（Qdrant+MCP）**

在 Raspberry Pi 5 上以本地模式运行 Qdrant 向量数据库并通过 MCP（Model Context Protocol）为 AI agent 提供跨会话持久记忆：事实存为向量嵌入，按语义相似度检索，数据不离开设备、无需云服务或 GPU。栈含 Qdrant MCP Server、mcporter 桥接、all-MiniLM-L6-v2（默认嵌入模型，ONNX/CPU），可选 OpenClaw Hard Enforcement 插件在每次响应前自动注入相关记忆。支持本地 SQLite 模式或 Docker/k3s 服务模式，附批量导入脚本。单次查询约 3 秒。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Qdrant 本地模式 + MCP 集成，无云依赖、无 GPU
- OpenClaw Hard Enforcement 插件在响应前自动注入记忆（~100-500ms）
- 支持多 collection 与 Docker/k3s 容器化部署
- seed-memory.sh 批量导入与 metadata 过滤

## 适用场景

- 让 AI agent 在重启后仍保留事实型长期记忆
- 在个人知识库上做语义搜索（找钥匙放哪、餐厅名）
- 团队/家庭共享记忆与项目决策上下文存储

## 场景标签

`Agent 记忆` `语义搜索` · 领域:Agent 开发

## 证据(README 行号)

> L23: Local vector database (Qdrant) with MCP (Model Context Protocol) integration. Facts are stored as 384-dimensional e
> L99: Key insight: The MCP server is **stateless** — it spawns per-call, does its work, and exits. No daemon process eati
> L185: **Hard Enforcement** solves this: an OpenClaw plugin that automatically queries Qdrant before every response and i

## 星数曲线

```mermaid
xychart-beta
    title "rockywuest/qdrant-mcp-pi5 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `6b910f3fbdfb` · [字段定义](../../DATASET.md)*
