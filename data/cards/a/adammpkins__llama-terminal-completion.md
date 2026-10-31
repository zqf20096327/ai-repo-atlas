# adammpkins/llama-terminal-completion

⭐ 194 · Go · MIT · 推送 2026-05-31 · [GitHub](https://github.com/adammpkins/llama-terminal-completion) · [官网](https://adammpkins.github.io/llamaterm/) · 个人维护

**终端里的 AI 助手 CLI：接入任意 OpenAI 兼容 API 问答与生成命令**

用 Go 编写的单二进制终端工具 LlamaTerm，通过 OpenAI 兼容 API 提供问答、shell 命令生成、代码解释、交互式聊天与流式输出。默认对接本地 Ollama，也可配置 LM Studio、llama.cpp、OpenAI、Azure OpenAI。附带多步工具调用 agent（写文件/执行命令/取 URL，含确认门与审计日志）、RAG 索引检索、JSON schema 结构化输出、图像输入、MCP 服务器接入与 Ctrl-G 命令行补全部件。配置支持配置文件、环境变量与 CLI 参数。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一 Go 二进制、无 CGO、支持流式输出
- lt agent 多步工具调用循环（确认门、危险命令检测、审计日志）
- RAG 索引本地文件/URL 并引用检索结果回答
- 接入任意 MCP 服务器的工具集

## 适用场景

- 在终端直接向 AI 提问或生成 shell 命令
- 绑定 Ctrl-G 用自然语言改写当前命令行
- 让 agent 在工作目录内执行多步文件与命令任务
- 对本地文档目录建 RAG 索引后做引用式问答

## 场景标签

`AI 助手` `代码生成` `文档问答` · 领域:编码与开发

## 证据(README 行号)

> L5: **AI assistant in your terminal** — works with any OpenAI-compatible API.
> L86: ## Supported Providers

## 星数曲线

```mermaid
xychart-beta
    title "adammpkins/llama-terminal-completion 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 193 --> 195
    line [194, 194]
```

2026-10-18 194 → 2026-10-31 194（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `14d8fbf90486` · [字段定义](../../DATASET.md)*
