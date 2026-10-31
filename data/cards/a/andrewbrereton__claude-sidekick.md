# andrewbrereton/claude-sidekick

⭐ 16 · TypeScript · 推送 2026-10-23 · [GitHub](https://github.com/andrewbrereton/claude-sidekick) · 个人维护

**连接 Claude 与本地 Ollama 的 MCP 服务器，分流简单任务省 token**

一个 Model Context Protocol (MCP) 服务器，将 Claude Desktop 接入本地 Ollama 模型，把文本生成、对话、嵌入、代码生成、摘要等较简单任务委托给本地模型执行，以保留 Claude token 用于复杂推理。提供 7 个 MCP 工具，可通过环境变量配置 Ollama 端点、超时与默认模型。全部推理在本地完成，无需 API key。面向使用 Claude Desktop 并装有本地 Ollama 的用户，需手动配置 claude_desktop_config.json 并构建运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 7 个 MCP 工具：文本生成/对话/嵌入/代码生成/摘要/列模型/拉取模型
- 通过环境变量可覆盖 Ollama 端点、超时与默认模型
- 全部推理本地运行，无需 API key 或外部服务
- 给出按任务类型的模型推荐（gpt-oss、llama3.2、qwen2.5、deepseek-coder 等）

## 适用场景

- Claude Desktop 用户把简单写作或摘要任务交给本地模型以节省 token
- 在本地对文档做嵌入与语义相似度计算
- 数据集分析工作流中让本地模型生成基础描述、Claude 做复杂分析

## 场景标签

`模型网关` `语义搜索` · 领域:Agent 开发

## 证据(README 行号)

> L3: A Model Context Protocol (MCP) server that connects Claude to your local Ollama models, allowing you to offload simp
> L54:   "mcpServers": {
> L65: ### `ollama_generate_text`

## 星数曲线

```mermaid
xychart-beta
    title "andrewbrereton/claude-sidekick 星数(近 2 点)"
    x-axis ["2026-10-24", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-24 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `bde0302b7c89` · [字段定义](../../DATASET.md)*
