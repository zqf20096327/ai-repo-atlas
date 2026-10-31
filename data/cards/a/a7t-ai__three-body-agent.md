# a7t-ai/three-body-agent

⭐ 14 · MIT · 推送 2026-10-10 · [GitHub](https://github.com/a7t-ai/three-body-agent) · [官网](https://three-body.a7t.ai) · 个人维护

**基于 GitHub Actions 与 Claude Code CLI 的自主开发流水线**

由五个 GitHub Actions 工作流组成的自主开发流水线：Implementer 每小时从 Projects V2 看板挑选最高优先级 issue 并实现、开 PR；Fixer 处理 CI 失败、评审评论与合并冲突；Merger 每 2 小时合并全绿 PR；另有看板同步与周里程碑滚动工作流。全部用 Shell 脚本与 GraphQL 实现，依赖仅 gh/jq/curl，智能来自模型（Claude Code CLI 由工作流自动安装，需 ANTHROPIC_API_KEY）。面向希望自动化 issue→实现→修 CI→合并全流程的开发者，配套通知走可替换的 Telegram 工作流。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 五个定时工作流覆盖取 issue、实现、修 CI、合并与看板同步
- 无框架无 SDK，仅依赖 gh/jq/curl 的 Shell + GraphQL 实现
- Claude Code CLI 由工作流自动安装，Claude 参与评审评论权衡后合并
- Telegram 通知为可插拔工作流，可替换为 Slack/Discord/邮件

## 适用场景

- 让流水线自动领取看板 issue 并提交实现 PR
- 无人值守地修复 CI 失败与合并冲突
- 自动合并通过全部检查的 PR 并同步看板状态

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L5: **An autonomous development pipeline powered by GitHub Actions and Claude Code CLI. Five workflows pick issues from 
> L14: Three systems in constant gravitational pull, each with its own orbit, producing stable results. Shell scripts and 
> L22:  - `ANTHROPIC_API_KEY` — Claude Code CLI is installed automatically by the workflows.

## 星数曲线

```mermaid
xychart-beta
    title "a7t-ai/three-body-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `7d11d8c70cc0` · [字段定义](../../DATASET.md)*
