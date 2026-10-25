# gintasz/neuralyzer

⭐ 40 · TypeScript · MIT · 推送 2026-08-07 · [GitHub](https://github.com/gintasz/neuralyzer) · 个人维护

**AI agent 扩展：一键清空会话上下文并重发首条消息**

为 AI agent harness（pi、OpenCode）提供的扩展，仅添加一个无参数工具 neuralyzer：调用后清除会话中全部用户与助手消息，并重新发送第一条消息副本。用途是把传统外置于 agent 的循环控制器（如 shell while 循环）交还给 agent 自身，实现循环工程，同时避免 /loop 持续累积上下文导致的 token 成本增加。README 说明 Claude Code 目前无相应扩展接口可支持此能力。

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

- 单个无参数工具：清空全部会话消息并重发首条消息
- 将循环控制器从外部脚本交还给 agent 自身
- 通过 pi 与 OpenCode 两种 harness 安装

## 适用场景

- 让 agent 在循环任务中自主重置上下文
- 替代 shell 循环式 Ralph loop，避免上下文膨胀
- 周期性检查类任务（如轮询 PR 后决定继续或重置）

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L5: Watch the first minute of this video as an introduction. This extension adds 1 tool for AI agent harness to call, na
> L16: Easier and more ergonomic loop engineering. A traditional Ralph loop is basically running this command in your shel

## 星数曲线

```mermaid
xychart-beta
    title "gintasz/neuralyzer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 39 --> 41
    line [40, 40]
```

2026-10-18 40 → 2026-10-25 40（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `2a11abb292c3` · [字段定义](../../DATASET.md)*
