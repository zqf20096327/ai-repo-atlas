# thellmwhisperer/human.md

⭐ 20 · Python · MIT · 推送 2026-04-10 · [GitHub](https://github.com/thellmwhisperer/human.md) · 个人维护

**约束 AI 编程助手作息的配置框架与守护脚本**

放置在仓库中的 human.md 配置文件，配套 install.sh 安装的 human-guard：通过 shell wrapper 在会话启动前检查工作时段，通过 PreToolUse 钩子在会话中拦截越界工具调用，实现工作时间、会话时长、休息与屏蔽时段的两层强制执行；另有仅依赖 agent 自觉遵守的手动模板模式。面向使用 Claude Code 等 AI 编程助手的开发者，需要 jq 与 Python/Node/Bun/Deno 之一，shell 为 zsh 或 bash。

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

- human.md 定义工作时段、会话上限与屏蔽时段
- wrapper 启动前检查 + PreToolUse 钩子会话中拦截的双层强制
- soft/advisory 两种执行级别，支持 min_activity_gap_seconds 过滤 agent 自主活动
- 提供 curl 一键安装脚本与卸载脚本

## 适用场景

- 限制自己深夜或超长时间使用 AI 编程助手
- 为深度写作/架构时段屏蔽 AI 编程会话
- 团队为使用 Claude Code 的工程师设置使用边界

## 场景标签

 · 领域:开发者工具/人机协作健康

## 证据(README 行号)

> L18: `human.md` is a configuration file you place in your repository to tell AI coding agents how to treat you — the hum
> L127: ```text

## 星数曲线

```mermaid
xychart-beta
    title "thellmwhisperer/human.md 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `81cf7144d1fb` · [字段定义](../../DATASET.md)*
