# superhq-ai/neko

⭐ 23 · Rust · MIT · 推送 2026-02-27 · [GitHub](https://github.com/superhq-ai/neko) · 组织维护

**面向树莓派 Zero 2W 等低配设备的轻量 AI agent 运行时**

Rust 实现的单二进制 AI agent 运行时，目标设备为 Raspberry Pi Zero 2W 与低配 VPS。通过 OpenResponses 兼容接口对接 OpenAI、Anthropic（经代理）、Ollama 等任意提供方；记忆采用纯 Markdown 文件的三层架构（核心记忆/每日日志/召回日志），由 agent 自行维护。支持 MCP stdio 工具、SKILL.md 技能、Telegram 频道、cron 定时任务与沙箱化 Python 解释器。安装方式为 install.sh 脚本或 cargo 从源码构建，覆盖 x86_64/aarch64 的 Linux 与 macOS 平台。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenResponses 兼容 LLM 接入（OpenAI/Anthropic 代理/Ollama/自托管）
- 纯 Markdown 文件记忆，三层架构，无需数据库/向量库
- MCP stdio 工具与 AgentSkills.io 兼容技能
- Telegram 频道、cron 任务与 monty 沙箱 Python 解释器

## 适用场景

- 在树莓派或低配 VPS 上 7x24 运行个人 AI agent
- 通过 Telegram 与 agent 对话并接收定时任务结果
- 用 git 管理和审阅 agent 的纯文本记忆

## 场景标签

`Agent 框架` `Agent 记忆` `AI 助手` · 领域:Agent 开发

## 证据(README 行号)

> L4: Lightweight AI agent runtime targeting Raspberry Pi Zero 2W and low-end VPS. File-based memory, MCP tool support, Te
> L64: Works with any provider exposing `POST /v1/responses` — OpenAI, Anthropic (via proxy), Ollama, or self-hosted model
> L85: Connect external tools via Model Context Protocol stdio transport. Tools are discovered automatically and registere

## 星数曲线

```mermaid
xychart-beta
    title "superhq-ai/neko 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-29"]
    y-axis "stars" 21 --> 24
    line [22, 23, 23]
```

2026-10-18 22 → 2026-10-29 23（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `0c2db4ca4d95` · [字段定义](../../DATASET.md)*
