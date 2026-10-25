# elias-ba/ask

⭐ 49 · Shell · MIT · 推送 2026-02-28 · [GitHub](https://github.com/elias-ba/ask) · [官网](https://elias-ba.github.io/ask/) · 个人维护

**面向终端开发者的纯 bash 多供应商 LLM CLI 工具**

ask 是用纯 bash 编写的 AI CLI 工具，面向常驻终端的开发者：支持 Anthropic、OpenAI、Google Gemini、OpenRouter、DeepSeek 与本地 Ollama 等多家供应商，提供流式问答、交互式多轮对话、Agent 模式（经用户批准执行任务）、生成可复用 bash 函数、git 语义化提交信息生成，以及 --json/--csv/--md/--raw 结构化输出以接入管道。密钥经 ask keys set 管理，存于 ~/.config/ask/keys.env（600 权限）。依赖仅 curl 与 jq，通过 curl 下载或 git clone 安装，可选 glow/bat 美化输出。Ollama 本地模式无需 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多供应商支持：Anthropic/OpenAI/Gemini/OpenRouter/DeepSeek/Ollama（本地）
- Agent 模式：经批准执行任务计划
- 生成可复用 bash 函数（--fn），支持管道与结构化输出（--json/--csv/--md）
- 纯 bash 实现，无 Python/Node 运行时依赖，仅需 curl 与 jq

## 适用场景

- 在终端直接向 LLM 提问、分析日志或调试输出
- 通过 Agent 模式让 ask 代为执行批量文件任务
- 生成并保存可复用的 bash 工具函数
- 用管道组合结构化输出做日志告警与系统诊断

## 场景标签

`聊天机器人` `AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L4: ask is an AI-powered CLI tool for developers who live in the terminal. It brings multi-provider LLM support, agent c
> L10: - **Generates reusable bash functions** - Not just answers, but tools
> L15: - **Multi-provider** - Anthropic, OpenAI, Google Gemini, OpenRouter, DeepSeek, and Ollama (local)

## 星数曲线

```mermaid
xychart-beta
    title "elias-ba/ask 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 48 --> 50
    line [49, 49]
```

2026-10-18 49 → 2026-10-25 49（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `1949747ee0d2` · [字段定义](../../DATASET.md)*
