# mmr710/nightmux

⭐ 25 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/mmr710/nightmux) · [官网](https://mmr710.github.io/nightmux/) · 个人维护

**手机远程驱动多个 AI 编程代理的夜间值守自托管工具**

通过 Telegram（每项目一个 topic、一个 tmux 会话）或网页仪表盘，从手机驱动 Claude Code、Codex、Gemini、aider 等终端编程代理：在用量限额中断后保持队列并在窗口重置时自动续跑、代理间故障切换（!failover）、按计划执行（!at/!every/!shift）、循环直到测试通过（!goal），并生成早晨简报。仅用 Python 标准库、零依赖，自托管于本机，默认不对外暴露端口。另含用量成本统计（wrapped）和会话交接（handoff）两个独立工具，提供一键安装脚本、Docker 镜像与 Claude Code 插件形式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 用量限额中断后保持队列并自动恢复，支持代理间切换
- 通过 Telegram 按钮审批、发送照片/文件/语音给代理
- 仅 Python 标准库、零依赖，自托管，默认不暴露端口
- wrapped 成本统计与 handoff 交接两个可独立运行的工具

## 适用场景

- 夜间让 AI 编程代理持续跑任务，早晨看简报与待审批项
- 用量限额到期后自动切换到另一个代理继续工作
- 从手机审批代理的权限请求并查看运行状态

## 场景标签

 · 领域:开发者工具/AI 代理编排

## 证据(README 行号)

> L7: Drive **Claude Code, Codex, Gemini, agy, opencode, Cursor, Amp, Goose, Qwen Code** and **aider**
> L121: Any agent that runs in a terminal works: nightmux types into its tmux pane and reads the screen back. What it read
> L110: |🤝 **Several agents**|Claude Code, Codex, agy, opencode, Gemini, Cursor, Amp, Goose, Qwen, aider · one topic, a be

## 星数曲线

```mermaid
xychart-beta
    title "mmr710/nightmux 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-27"]
    y-axis "stars" 21 --> 26
    line [22, 25, 25]
```

2026-10-18 22 → 2026-10-27 25（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `f3fc2a62a2a4` · [字段定义](../../DATASET.md)*
