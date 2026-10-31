# acrid-auto/agent-architect

⭐ 14 · MIT · 推送 2026-10-10 · [GitHub](https://github.com/acrid-auto/agent-architect) · [官网](https://acridautomation.com/architect/) · 组织维护

**40 题问卷生成可每日自主运行的 Claude Code agent 工作区**

一个 Markdown 问卷与配套模板：用户在 Claude Code（或任意聊天 AI）中回答 40 个问题，覆盖使命、身份、运营节奏、工具、记忆、技能等 8 个模块，自动生成包含 BOOT.md、CLAUDE.md 等文件的 agent 工作区，含任务调度使 agent 每日自主执行。发送/发布类任务默认以草稿运行一周，settings.json 按需授权。由名为 Acrid 的 AI 所运营的公司维护，MIT 许可。

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

- 40 题、8 模块问卷生成完整 Claude Code 工作区
- 生成日常调度使 agent 无需提醒自主执行任务
- 默认安全策略：发布类任务先以草稿运行一周
- 无需 Claude Code 也可用任意聊天 AI 生成文件

## 适用场景

- 想搭建一个有明确身份与边界的日常自主 agent
- 为 Claude Code 生成结构化的 CLAUDE.md 与权限配置
- 通过问卷梳理 agent 的使命、升级与记忆策略

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: **Answer 40 questions. Get an AI agent that runs by itself every day.**
> L5: Not a personality prompt. A complete Claude Code workspace: who the agent is, how it talks, what it decides alone an
> L11: 1. Make an empty folder and open Claude Code in it: `mkdir my-agent && cd my-agent && claude`

## 星数曲线

```mermaid
xychart-beta
    title "acrid-auto/agent-architect 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-29", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `ce0d490fc756` · [字段定义](../../DATASET.md)*
