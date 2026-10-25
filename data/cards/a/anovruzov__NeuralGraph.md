# anovruzov/NeuralGraph

⭐ 151 · Rust · MIT · 推送 2026-10-24 · [GitHub](https://github.com/anovruzov/NeuralGraph) · [官网](myceliclabs.com) · 个人维护

**给 Claude 等 MCP agent 的本地持久化图记忆服务**

用 Rust 编写的本地优先记忆服务器：把对话轮次异步抽取为结构化记忆、实体与类型化关系，存入单个 SQLite 文件；检索用向量与 BM25 双通道按名次融合，支持说话者路由、时间感知的事实覆盖与审计式遗忘。通过 MCP（stdio 与 Streamable HTTP）接入 Claude Desktop/Claude Code 等 MCP 客户端，并提供 CLI、REST API 与实时仪表盘。默认搭配本地 Ollama 模型（如 qwen2.5:7b-instruct），也支持确定性假模型模式无模型运行。检索效果在 LoCoMo 基准上评测并公布实验细节。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 对话轮次异步抽取为实体-关系图记忆，单个 SQLite 文件存储
- 向量+BM25 按名次融合检索，说话者路由与时间感知覆盖
- 九个 MCP 工具（检索/上下文/画像/增删记忆）+ CLI + REST API + 仪表盘
- --fake-llm 模式无需下载模型即可运行全流程

## 适用场景

- 给 Claude Desktop 或 Claude Code 添加跨会话持久记忆
- 为任意 MCP 客户端提供本地化、无 API key 的记忆后端
- 导入 JSONL 聊天记录建立可检索的个人知识图

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L19: NeuralGraph gives Claude and any MCP-capable agent memory that survives the end of a
> L81: The MCP server is `neuralgraph-chat-memory` (v1.0.0). It speaks **stdio** for desktop
> L240: crates/neuralgraph-memory/  THE ASSISTANT — memory server, MCP, worker, store, dashboard (Rust)

## 星数曲线

```mermaid
xychart-beta
    title "anovruzov/NeuralGraph 星数(近 3 点)"
    x-axis ["2026-10-22", "2026-10-23", "2026-10-25"]
    y-axis "stars" 150 --> 163
    line [162, 152, 151]
```

2026-10-22 162 → 2026-10-25 151（-11）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `234fa62ab62e` · [字段定义](../../DATASET.md)*
