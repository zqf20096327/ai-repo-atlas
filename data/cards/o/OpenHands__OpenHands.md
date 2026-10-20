# OpenHands/OpenHands

⭐ 91,197 · TypeScript · MIT · 推送 2026-10-18 · [GitHub](https://github.com/OpenHands/OpenHands) · [官网](https://openhands.dev) · 组织维护

**自托管的编码 agent 控制中心：管理多 agent 与自动化**

OpenHands Agent Canvas 是一个自托管开发者控制中心，用于启动与编码 agent 的对话并自动化日常任务，如生成报告发布到 Slack、将 GitHub issue 分解为任务。默认本地运行，可连接多个 agent 后端：本地、Docker 容器、VM 或企业基础设施，也可选用 OpenHands Cloud/Enterprise。开箱即用运行开源 OpenHands agent，也支持 Claude Code、Codex、Gemini CLI、Pi、OpenCode 等 ACP 兼容 agent。提供 npm 安装与 Docker 沙箱模式，项目状态为 beta。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 动量与使用信号

- 维护:`active` — 距上次 push 0.6 天,年发版 63,461 位贡献者
- 涨星:近 1 天 **+101**(自 20261016 起算)
- 安装:npm 包 `@openhands/agent-canvas` 月下载 17,530

## 能力要点

- 支持 OpenHands、Claude Code、Codex、Gemini 等 ACP 兼容 agent
- 本地/Docker/VM/云多种后端可切换，不丢失焦点
- 创建定时或 webhook 触发的自动化，集成 Slack、GitHub、Notion 等
- 支持任意 LLM（bring your own model）

## 适用场景

- 自托管管理多个编码 agent 并在本地与云端后端间切换
- 配置定时或 webhook 触发的自动化任务并推送结果到 Slack
- 在多个 Docker 沙箱中并发运行 agent 做代码审查和依赖更新

## 场景标签

`编码 Agent` `多智能体` `代码审查` · 领域:Agent 开发

## 证据(README 行号)

> L4:  The self-hosted developer control center for coding agents and automations.
> L29: Agent Canvas runs the open source OpenHands agent out-of-the-box, but can use third-party agents such as Claude Cod
> L37: |**Bring your own model**|Use with any LLM|

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `d4a1a44ea490` · [字段定义](../../DATASET.md)*
