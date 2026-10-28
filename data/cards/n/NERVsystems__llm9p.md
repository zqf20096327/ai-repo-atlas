# NERVsystems/llm9p

⭐ 50 · Go · MIT · 推送 2026-09-01 · [GitHub](https://github.com/NERVsystems/llm9p) · 个人维护

**把 LLM 暴露为 9P 文件系统：写文件即提问、读文件得回答**

用 Go 编写的 9P 文件服务器，将大语言模型访问映射为标准文件操作：向 ask 文件写入 prompt，从同一文件读取回答；另提供 model、temperature、system、tokens、stream 等虚拟文件及流式接口。后端支持 Anthropic API 与 Claude Code CLI（Max 订阅），本地 Ollama 后端为计划中；可插拔架构便于新增提供商。适用于 Plan 9/Inferno 生态及任何能读写文件的脚本、工具与 AI agent，需配合 plan9port、Linux 9P 内核模块或 Inferno 等 9P 客户端挂载。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LLM 交互抽象为 ask/model/temperature/stream 等虚拟文件读写
- 支持 Anthropic API 与 Claude Code CLI 两种后端，可插拔扩展
- 提供流式接口（stream/ask + stream/chunk）与会话状态文件
- 任何能读写文件的语言或工具均可调用，无需 SDK

## 适用场景

- 在 Plan 9/Inferno 环境中通过文件操作访问 LLM
- 用 shell 脚本与 Unix 管道串联 LLM 调用
- 让只能读写文件的脚本或 agent 直接使用 LLM

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L5: llm9p enables users, scripts, and AI agents to interact with Large Language Models through standard filesystem opera
> L15: The pluggable backend architecture makes it easy to add new LLM providers.

## 星数曲线

```mermaid
xychart-beta
    title "NERVsystems/llm9p 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 49 --> 51
    line [50, 50]
```

2026-10-18 50 → 2026-10-28 50（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `f2a365eb883a` · [字段定义](../../DATASET.md)*
