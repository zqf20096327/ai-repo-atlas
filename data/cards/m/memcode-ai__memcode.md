# memcode-ai/memcode

⭐ 18 · Go · MIT · 推送 2026-10-14 · [GitHub](https://github.com/memcode-ai/memcode) · [官网](https://memcode.ai/docs) · 组织维护

**带仓库持久记忆的开源终端编码 Agent 与自托管网关**

单个 Go 二进制，两种运行方式：Code 是终端交互式编码 agent，在 .memcode 目录维护仓库子系统、历史尝试与用户偏好的持久记忆，随仓库携带供团队共享；Agents 是同一二进制的自托管网关，接入 Telegram、Slack、Discord 等 12 个聊天渠道，并可运行按计划自治的 agent（策略门控、动作日志、文件访问限定）。支持任意 OpenAI 兼容端点：自有 API key、本地 Ollama 或托管账户。还提供持续任务自动化与子 agent 并行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 在 .memcode 中维护仓库子系统、失败尝试与用户偏好的持久记忆
- 同一二进制可作自托管网关，接入 Telegram/Discord/Slack 等 12 个渠道
- 自治 agent 运行采用策略门控、动作日志与文件访问限定
- 通过环境变量接入任意 OpenAI 兼容端点（含本地 Ollama）

## 适用场景

- 在终端里让记住仓库上下文的编码 agent 续接上周的工作
- 从 Telegram/Slack 等聊天渠道向 agent 下发任务并跟进
- 让 agent 按计划无人值守处理依赖更新、安全告警分类等持续职责

## 场景标签

`编码 Agent` `Agent 记忆` `模型网关` `工作流自动化` · 领域:Agent 开发

## 证据(README 行号)

> L3:  The coding agent that remembers your repo.
> L13: One Go binary, two ways to run it. **Code** is the interactive agent in your terminal. **Agents** is the same binar
> L166: The CLI is the agent: all model selection, escalation, and recovery run client-side; every backend is a plain serv

## 星数曲线

```mermaid
xychart-beta
    title "memcode-ai/memcode 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-31 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `bb0bd624fb57` · [字段定义](../../DATASET.md)*
