# OleksiyM/groq-cli-chat

⭐ 20 · Go · MIT · 推送 2026-09-05 · [GitHub](https://github.com/OleksiyM/groq-cli-chat) · 个人维护

**开发者的 Groq 及 OpenAI 兼容模型一次性问答 CLI**

用 Go 编写的命令行聊天工具，通过 OpenAI 兼容 API 与 Groq 及 xAI、OpenRouter、OpenAI、Mistral、DeepSeek 等服务商交互。仅支持一次性提示（不保留对话上下文），交互式 shell 内可切换模型（最多显示 20 个）、更新模型列表、查看/切换 Markdown 格式的问答历史。每次回答输出 token 数、耗时与每秒 token 统计。通过 YAML 配置文件与环境变量设置 API key 与 base_url，内存占用声明为 11–14MB。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持任意 OpenAI 兼容 API，内置 Groq/xAI/OpenAI/OpenRouter 配置示例
- 一次性提示模式，附 token 数/耗时/每秒 token 响应统计
- 交互式 shell：切换模型、更新模型列表、Markdown 历史保存与开关
- 跨平台二进制发布（Windows/Linux/macOS），内存占用声明 11–14MB

## 适用场景

- 在终端快速向 Groq 等模型发起一次性问答
- 在旧硬件或资源受限环境运行轻量 CLI 聊天工具
- 对比不同服务商模型的响应速度（token/sec 统计）
- 以 Markdown 文件形式留存问答记录

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L3: **groq-chat** is a minimalistic, high-performance command-line interface (CLI) for interacting with Groq AI and othe
> L15: - **Support for multiple AI providers** — works with any OpenAI-compatible API.
> L253: - Support for multiple AI providers (OpenAI compartible APIs)


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `f09e09436cf6` · [字段定义](../../DATASET.md)*
