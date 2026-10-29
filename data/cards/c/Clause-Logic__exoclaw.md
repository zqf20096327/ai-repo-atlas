# Clause-Logic/exoclaw

⭐ 24 · Python · NOASSERTION · 推送 2026-09-02 · [GitHub](https://github.com/Clause-Logic/exoclaw) · 个人维护

**给开发者的协议优先 AI agent 框架：自带循环与七类协议**

从 nanobot 分支精简而来的纯协议 AI agent 核心库：提供 AgentLoop、消息总线与七个 Python 协议（Channel、Conversation、LLMProvider、Tools、Bus、存储、执行器），全部组件按需选配、无内置实现。单一运行时依赖 structlog，约 2,000 行 Python，mypy strict、95% 测试覆盖率。可嵌入 FastAPI、独立脚本或 GitHub Actions，支持 CPython 与 MicroPython（可在 ESP32-S3 运行），组件可替换为 Redis、Ollama、Temporal 等。另有 Go 移植版 exoclaw-go 从 Python 标签版本定期前向移植。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 七个 Python 协议 + AgentLoop 的纯协议核心，组件全部按需选配
- 唯一运行时依赖 structlog，约 2,000 行，95% 测试覆盖率
- 同一源码树支持 CPython 与 MicroPython，可在 ESP32-S3（8MB）运行
- 可用作 GitHub Actions bot，回复 issue 与 PR 评论

## 适用场景

- 在现有 FastAPI 应用中以后台任务方式接入 agent 能力
- 搭建可自由替换 provider/存储/频道的定制 agent
- 零基础设施下用 GitHub Actions 跑一个 issue 回复 bot
- 在微控制器（ESP32-S3）上运行单租约 agent

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L9: You have an app. Wire in exoclaw and it gains tool use, conversation memory, and any LLM. You own every piece. Nothi
> L48: InboundMessage → Bus → AgentLoop → LLM → Tools → Bus → OutboundMessage → Channel

## 星数曲线

```mermaid
xychart-beta
    title "Clause-Logic/exoclaw 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-29 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `44ce82a58ac8` · [字段定义](../../DATASET.md)*
