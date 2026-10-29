# tkalevra/FaultLine

⭐ 20 · Python · AGPL-3.0 · 推送 2026-10-28 · [GitHub](https://github.com/tkalevra/FaultLine) · 个人维护

**给本地 AI 用的可校验知识图谱记忆层，经 MCP 共享**

为已运行的 LLM 提供持久化记忆的自托管服务：从对话中抽取事实，经校验门过滤后存入结构化知识图谱（PostgreSQL 为权威存储），纠错时归档旧值而非覆盖；通过 8002 端口的 MCP/OpenAPI 服务将同一记忆库共享给 OpenWebUI、Claude Desktop 等客户端。每用户独立 PostgreSQL schema 实现多租户隔离。/expand 命令可从指定文档或内置知识学习领域本体。需 Docker 部署，依赖外部 LLM 后端（Ollama/LM Studio/OpenAI 等）；首次启动下载约 500MB 的 GLiNER2 抽取模型，CPU 即可运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 事实经校验门存储，拒绝幻觉写入，纠错归档旧值
- MCP 服务使 OpenWebUI、Claude Desktop 等多客户端共享同一记忆库
- 每租户独立 PostgreSQL schema（无共享 user_id 列）实现隔离
- /expand 可从在线文档构建领域本体并可被用户纠正

## 适用场景

- 让本地 LLM 跨会话记住主机、IP、MAC、人物偏好等结构化事实
- 多客户端共享同一份私有记忆库
- 多用户共用部署时保证各人记忆互不可见

## 场景标签

`知识图谱` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L21: FaultLine exposes an MCP server. That means the same memory store is available to OpenWebUI, Claude Desktop, or any
> L174: FaultLine hooks into an LLM you already run — it doesn't host one. (If you *don't* have a model handy, `docker com

## 星数曲线

```mermaid
xychart-beta
    title "tkalevra/FaultLine 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `9c25d4227b41` · [字段定义](../../DATASET.md)*
