# theo-kirby/ouroboros

⭐ 30 · Python · MIT · 推送 2026-10-27 · [GitHub](https://github.com/theo-kirby/ouroboros) · [官网](https://borris.dev) · 个人维护

**让 Claude Code/Codex/Pi 长时间自主跑任务的循环框架**

面向需要 agent 连续运行数小时的开发者的 Python 框架：一份 charter（使命、完成标准、约束、质量门槛）指导 Actor/Critic/Scribe 三角色循环——Actor 完成并测试一项改动，Critic 只读评审、对照 charter 回退不合格改动并写下一个 prompt，Scribe 记录过程并折叠记忆。需 Python 3.12+、uv 和至少一个已登录的 agent CLI（claude/codex/pi），用 tmux/tern/systemd 会话维持运行。提供用量上限、卡死检测、实时运行页面与 Pushover 推送。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Actor/Critic/Scribe 三角色循环，charter 由 agent 不可编辑
- 用量窗口计量与多 harness 回退切换，运行不阻塞
- append-only 记忆与 state-claims 图，支持文件或 Flywheel/Governor 后端
- 每次运行的实时页面（进度/用量/记忆图/迭代时间线）与 Pushover 告警

## 适用场景

- 让 agent 按我写好的章程通宵推进项目并获得可读分支
- 出差时通过手机查看长时运行的进度与告警
- 对 agent 产出做逐项对照章程的评审与回退

## 场景标签

`编码 Agent` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L5:  Autonomous framework for long-running agents
> L17: guides Claude Code, Codex or Pi through a loop that runs for hours: one agent
> L30: You need Python 3.12+, `uv`, and at least one


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `d00e4ab21e82` · [字段定义](../../DATASET.md)*
