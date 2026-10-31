# alexk-dev/golemcore-bot

⭐ 41 · Java · Apache-2.0 · 推送 2026-07-31 · [GitHub](https://github.com/alexk-dev/golemcore-bot) · [官网](https://golemcore.me) · 个人维护

**面向企业的渠道接入 Agent 运行平台，支持技能/插件/MCP/记忆**

GolemCore Bot 是运行渠道连接型 AI Agent 的平台：通过仪表盘、Telegram 或 webhook 与 Agent 对话，支持技能、插件、MCP 服务器接入，提供记忆编排、延迟跟进、执行轨迹追踪与 Hive 控制面协调。插件可贡献工具、渠道、语音提供方与 RAG 摄取。以 Docker 镜像分发，内置 Spring Boot 运行时；另有实验性本地 app-image 打包（jpackage、捆绑 Java 运行时、picocli 启动器）。运行需 Docker 与至少一个 LLM provider API key；本地原生打包标注为 experimental。Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 插件原生运行时：插件可贡献工具、渠道、语音提供方与 RAG 摄取
- 技能可启动 MCP 服务器，运行时含 MCP 目录与发现流程
- 延迟跟进、渐进式记忆编排与恢复路径支持长时任务
- 执行轨迹、瀑布视图与导出快照用于调试

## 适用场景

- 在 Telegram、webhook 或仪表盘中运行对话式 Agent 并检查执行轨迹
- 通过技能、插件与 MCP 服务器扩展 Agent 能力
- 将 Agent 接入 Hive 做控制面协调与巡检

## 场景标签

`Agent 框架` `聊天机器人` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L11: GolemCore Bot is the agent platform for AI-native companies building on the GolemCore ecosystem.
> L17: 1. **Run agents** — chat in the dashboard, Telegram, or webhook-driven flows, then inspect execution, memory, and t

## 星数曲线

```mermaid
xychart-beta
    title "alexk-dev/golemcore-bot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-31 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `70075be75548` · [字段定义](../../DATASET.md)*
