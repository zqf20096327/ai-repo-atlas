# generalbots/generalbots

⭐ 96 · Rust · MIT · 推送 2026-10-24 · [GitHub](https://github.com/generalbots/generalbots) · [官网](https://generalbots.org) · 组织维护

**Rust 自托管多 agent AI 平台：编排 LLM 与 80 个业务应用**

用 Rust 编写的自托管多 agent AI 平台，包含桌面套件（Chat、CRM、Mail、Drive、Calendar 等 80 个应用）、云控制台和 113 个后端 crate。核心机制：botserver 消息管线经 BASIC(Rhai) 引擎、知识库注入、LLM 路由与工具执行；botllm 层支持 DeepSeek、Qwen、GLM、Kimi、Anthropic 或本地 llama.cpp 等任意 OpenAI 兼容端点，含自动故障转移与成本跟踪。支持完全离线/气隙部署，首个启动脚本自动拉起 PostgreSQL、MinIO、Qdrant 等全套依赖。机器人以目录形式（.gbai）定义，低代码 BASIC 语法编写。需从源码用 Rust 工具链构建运行。

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

- 80 个套件应用与 113 个后端 crate，桌面套件/云控制台/登录三端口分离
- botllm 层路由多家模型与任意 OpenAI 兼容端点，含自动故障转移与成本跟踪
- Agentic RAG、Graph RAG、持久记忆与多模态检索
- BASIC 低代码定义机器人行为，bot 以 .gbai 目录形式自动加载

## 适用场景

- 在自己基础设施上运行含 Chat/CRM/Mail/Drive 的一体化 AI 平台
- 编排多个具备独立人设、工具与知识库的 agent
- 气隙/离线环境下的数据主权化部署
- 通过 WhatsApp/Teams/Telegram 渠道对外提供 agent 服务

## 场景标签

`多智能体` `聊天机器人` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L5: **Multi-agent AI platform for autonomous agents, agentic AI orchestration and LLM workflow automation.**
> L48: Most "AI agent" tooling stops at a chat window. General Bots is the platform underneath it: an orchestration layer 
> L111: The full picture, top to bottom. **Clients and channels** reach **Caddy**, which routes to **botui** (three ports,

## 星数曲线

```mermaid
xychart-beta
    title "generalbots/generalbots 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-26"]
    y-axis "stars" 94 --> 97
    line [95, 96, 96]
```

2026-10-18 95 → 2026-10-26 96（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `570012ce4e41` · [字段定义](../../DATASET.md)*
