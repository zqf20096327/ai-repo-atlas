# simonw/llm

⭐ 12,827 · Python · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/simonw/llm) · [官网](https://llm.datasette.io) · 个人维护

**开发者在命令行与 Python 中调用多家大语言模型的 CLI 工具**

LLM 是一个 CLI 工具兼 Python 库，用于从命令行运行 prompt、发起聊天、存储历史到 SQLite、生成与保存 embeddings、从文本和图像提取结构化内容，并允许模型执行工具。通过插件机制接入不同厂商 API 与本地模型，可对接任意 OpenAI 兼容端点（如 LM Studio）。提供 pip、Homebrew、pipx、uv 等安装方式，模型密钥通过 llm keys set 配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CLI 与 Python 库双形态，prompt 与对话结果可存入 SQLite
- 插件机制接入 Gemini、Anthropic、Ollama 本地模型等
- 支持 embeddings 生成、结构化内容提取与工具执行
- 可对任意 OpenAI 兼容 Chat Completions 端点发 prompt

## 适用场景

- 在终端直接向 GPT/Gemini/本地模型提问或对话
- 把模型响应持久化到 SQLite 供后续分析
- 为本机运行的模型生成 embeddings 做检索
- 让模型在终端中调用工具完成任务

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L11: A CLI tool and Python library for interacting with **OpenAI**, **Anthropic’s Claude**, **Google’s Gemini**, **Qwen*
> L15: With LLM you can:
> L26: First, install LLM using `pip` or Homebrew or `pipx` or `uv`:

## 星数曲线

```mermaid
xychart-beta
    title "simonw/llm 星数(近 27 点)"
    x-axis ["2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26"]
    y-axis "stars" 12640 --> 12844
    line [12657, 12662, 12669, 12673, 12676, 12680, 12681, 12684, 12686, 12688, 12662, 12726, 12742, 12753, 12763, 12753, 12756, 12762, 12768, 12771, 12777, 12783, 12788, 12790, 12799, 12810, 12827]
```

2026-10-24 12,657 → 2026-11-26 12,827（+170）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `f88ead707ffd` · [字段定义](../../DATASET.md)*
