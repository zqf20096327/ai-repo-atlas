# scottonanski/persistent-mind-model-v1.0

⭐ 46 · Python · NOASSERTION · 推送 2026-08-21 · [GitHub](https://github.com/scottonanski/persistent-mind-model-v1.0) · 个人维护

**事件溯源的 AI 心智/记忆运行时：可重建身份与承诺审计**

Persistent Mind Model 是一个事件溯源运行时，将语言模型系统的记忆、反思、身份与承诺外置为可重建的自传式结构。核心机制：在 SQLite 中记录哈希链事件账本，重建 Mirror/MemeGraph/ConceptGraph 投影，做有界检索与检索溯源，并提供结构化承诺生命周期管理与条件校验。提供交互式客户端 pmm、一次性命令 pmm-turn（支持 dummy/Ollama/OpenAI 适配器）与 STDIO MCP 服务器。需 Python 3.9+，pip 安装，明确列出参考策略不统一、关系角色仅部分强制等限制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 哈希链事件账本与可重建的 Mirror/MemeGraph/ConceptGraph 投影
- 检索溯源：记录事件进入模型上下文的原因
- 结构化承诺 open/close/reopen 与身份转变的条件校验提升
- 交互式、一次性 JSON 与 MCP 三种入口

## 适用场景

- 为 AI agent 构建可审计的长期记忆与身份连续性
- 追踪模型自我描述变化背后的经历与反思链
- 通过 MCP 服务器接入 Claude 类客户端使用持久记忆

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L21: The current implementation is an event-sourced runtime beneath that aspiration.
> L101: ```bash

## 星数曲线

```mermaid
xychart-beta
    title "scottonanski/persistent-mind-model-v1.0 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 45 --> 47
    line [46, 46]
```

2026-10-18 46 → 2026-10-30 46（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `8264eaa12995` · [字段定义](../../DATASET.md)*
