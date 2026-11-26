# rapttor/sparkbots

⭐ 7 · TypeScript · MIT · 推送 2026-11-25 · [GitHub](https://github.com/rapttor/sparkbots) · [官网](https://rapttor.github.io/sparkbots/) · 个人维护

**把多个 AI 编码 agent 会话可视化为 3D 办公室机器人**

本地运行的 Web 应用，读取 Claude Code、Codex、OpenCode 的会话历史，将其渲染为低多边形 3D 园区：每个会话是一个工位机器人，按状态着色（工作中/等待/出错/完成/休眠），并提供 2D 面板替代视图。支持从侧栏与任意会话对话（流式回复、fork、排队消息），带写入安全限制与权限提示处理；按项目/模型/服务统计用量与成本估算，历史存入本地 SQLite。可选公共大厅 Unity 默认关闭。安装依赖 Node 22.13+ 与 pnpm。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 3D 园区可视化：每会话一个机器人，支持 100 worker 视图
- 侧栏与 agent 对话，含 fork、排队与安全写入限制
- 按日/项目/模型的用量统计与成本估算，本地 SQLite 持久化
- 可选公共大厅 Unity，默认关闭

## 适用场景

- 同时跑多个 agent 会话时一眼看清哪个在等权限或出错
- 从界面直接与某个会话的 agent 继续对话或派生新机器人
- 统计各项目各模型的 token 用量与成本估算

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L7: SparkBots turns the session history of your coding agents into a small low-poly campus you can walk around. Every **
> L50: - Safety rails built in: a session open in a terminal is never written to (fork instead), one run per session at a 


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `59ef98febe42` · [字段定义](../../DATASET.md)*
