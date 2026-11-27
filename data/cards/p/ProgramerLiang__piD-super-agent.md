# ProgramerLiang/piD-super-agent

⭐ 3 · JavaScript · MIT · 推送 2026-11-20 · [GitHub](https://github.com/ProgramerLiang/piD-super-agent) · [官网](https://plugins.aiuo.net/plugins/corripo.superagent-orchestrator) · 个人维护 · 中文 README

**PI-Desktop 插件：主 agent 派子会话异步干活并自动回报**

PI-Desktop 的编排插件（id corripo.superagent-orchestrator），注册 SessionTask 工具提供 spawn/spawnIn/send/supervise 等 12 个 action，把任务派给独立 worker 会话；默认 notifyOnCompletion 开启，worker 回合结束由宿主把结果写回调用会话并渲染结果卡。worker 按状态契约在报告末尾写 state/human_action 两行，区分『完成』与『需要人决定』。另注册 Workers 视图查看会话行。限制：worker 不能再派 worker、无 worktree 隔离、需宿主 >= 0.14.7。

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

- 12 个 action 的 SessionTask 工具，含 spawn/spawnIn/send/supervise/setModel 等
- 默认异步：notifyOnCompletion，派完结束本轮，结果自动回写
- state/human_action 状态契约区分完成与需人决策，宽进严出解析
- Workers 视图展示会话行，结果卡三级通道降级投递

## 适用场景

- 让主 agent 并行派多个子会话分别审查、修构建
- 跨项目派活而不落到错误的 checkout
- 区分子任务『已完成』与『需要我批准/决定』

## 场景标签

`编码 Agent` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L10: PI-Desktop 插件 · id `corripo.superagent-orchestrator` · 版本 `0.2.0` · MIT（见 LICENSE）· 需要 PI-Desktop `>= 0.14.7`（含 Ses
> L28: |一个 `SessionTask` 工具|12 个 action：`spawnIn` / `spawn` / `send` / `supervise` / `status` / `workers` / `wait` / `resu

## 星数曲线

```mermaid
xychart-beta
    title "ProgramerLiang/piD-super-agent 星数(近 2 点)"
    x-axis ["2026-11-23", "2026-11-27"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-23 3 → 2026-11-27 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `c249904db9a1` · [字段定义](../../DATASET.md)*
