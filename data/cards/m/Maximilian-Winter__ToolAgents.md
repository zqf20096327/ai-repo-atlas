# Maximilian-Winter/ToolAgents

⭐ 39 · Python · MIT · 推送 2026-09-17 · [GitHub](https://github.com/Maximilian-Winter/ToolAgents) · 个人维护

**创建函数调用 AI agent 的轻量 Python 框架，统一多 LLM 接口**

Python 框架，面向开发者构建函数调用（function-calling）agent：提供统一消息格式与接口，接入 OpenAI、Anthropic、Mistral、Groq 等 API，以及任意兼容这些格式的自定义 base_url 端点（OpenRouter、vLLM、llama-cpp-server、Ollama 等）。支持 Pydantic 模型、Python 函数与 OpenAI 风格规范三种方式定义工具；附带 tool-agents CLI，从 .tool-agents 项目文件夹运行 JSON 定义的流水线（含条件、循环、并行等流程控制），API key 不落盘、条件表达式沙箱化。MIT 许可。

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

- 统一消息格式，可在保留聊天记录的情况下切换 LLM 提供商
- 三种自定义工具方式：Pydantic 模型、Python 函数、OpenAI 风格规范
- tool-agents CLI 运行项目内 JSON 流水线，支持条件/循环/并行流程控制
- 兼容任意 OpenAI/Anthropic/Groq/Mistral 形态的自定义 base_url 端点

## 适用场景

- 我需要在多个 LLM 提供商之间无缝切换并保留聊天记录
- 我想用 Pydantic 模型或普通函数快速给 agent 定义工具
- 我想把 agent 工作流作为 JSON 项目资产进行版本管理并命令行运行

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: ToolAgents is a lightweight and flexible framework for creating function-calling agents with various language models
> L15:  (OpenRouter, vLLM, llama-cpp-server, Ollama, an internal gateway)

## 星数曲线

```mermaid
xychart-beta
    title "Maximilian-Winter/ToolAgents 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 38 --> 40
    line [39, 39]
```

2026-10-18 39 → 2026-10-28 39（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `ed18cccdaa16` · [字段定义](../../DATASET.md)*
