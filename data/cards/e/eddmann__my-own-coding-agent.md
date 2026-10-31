# eddmann/my-own-coding-agent

⭐ 19 · Python · 推送 2026-04-22 · [GitHub](https://github.com/eddmann/my-own-coding-agent) · 个人维护

**教学用可扩展 Python 编码 Agent 框架，支持多 LLM 提供方**

用 Python 编写的教学性编码 Agent harness：目标是通过亲手构建来理解 Codex、Claude Code 等系统的运作方式。提供 Provider 无关的 LLM 接入（OpenAI、Anthropic、OpenRouter、Ollama 等）、流式输出与工具调用、JSONL 会话持久化与分叉恢复、上下文压缩、Markdown+YAML 技能系统、提示模板、扩展 API 与内置工具套件，支持 TUI/headless CLI/本地 Web 三种交付方式。要求 Python 3.14+ 与 uv，通过 make 运行。

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

- Provider 无关 LLM 接入（OpenAI、Anthropic、OpenRouter、Ollama）
- JSONL 会话持久化与分叉恢复、上下文压缩
- Markdown+YAML 技能系统与提示模板（斜杠命令）
- TUI、headless CLI 与本地 Web 三种交付方式

## 适用场景

- 学习编码 Agent 的内部构造并自行修改扩展
- 搭建可切换多家 LLM 提供方的编码助手
- 通过扩展 API 定制工具与输入/工具调用流程

## 场景标签

`Agent 框架` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L5: An educational, expandable coding‑agent harness built in Python.
> L19: - Provider‑agnostic LLM support (OpenAI, Anthropic, and OpenAI‑compatible APIs like OpenRouter and Ollama)

## 星数曲线

```mermaid
xychart-beta
    title "eddmann/my-own-coding-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `1e4bd734eade` · [字段定义](../../DATASET.md)*
