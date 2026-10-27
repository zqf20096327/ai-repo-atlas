# peterhoang1103991-cmd/pilot-ai-ticket-shipper

⭐ 58 · HTML · 推送 2026-10-26 · [GitHub](https://github.com/peterhoang1103991-cmd/pilot-ai-ticket-shipper) · 个人维护

**把标记的工单自动变成 PR 的 AI 编排 CLI 工具**

Python 编排工具：监控 GitHub/Linear/Jira/Asana 中带 pilot 标签的工单，认领后按 计划→编码→测试→PR 流水线执行，每张工单独立分支，PR 关联原工单并保留人工审查。代码生成通过外部 AI 编码后端完成：默认 Claude Code CLI，可切换 OpenCode，或走 Anthropic API、AWS Bedrock、GCP Vertex。提供顺序/并行执行、质量门重试、预算限额、仪表盘与执行回放。运行需本地 git、Claude Code CLI 在 PATH 上并通过认证，状态存于 ~/.pilot。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 工单→分支→计划→实现→验证→PR 的端到端流水线
- 后端可切换（Claude Code / OpenCode / Anthropic / Bedrock / Vertex）
- 质量门失败自动反馈重试，超限则挂起工单并附失败输出
- 按任务复杂度路由模型与推理深度，预算硬限额
- 仪表盘、持久化指标与执行回放（HTML/JSON/Markdown）

## 适用场景

- 我把打上 pilot 标签的 GitHub issue 自动变成可审查的 PR
- 小团队在保留人工合并权的前提下消化积压工单
- 通过 Telegram/Slack 与流水线对话并接收每日简报

## 场景标签

 · 领域:开发者工具/AI 编码编排

## 证据(README 行号)

> L5: Pilot is a Python tool that turns labeled tickets from GitHub, Linear, Jira, or Asana into reviewed pull requests: i
> L64: |**Claude Code**|Default execution backend|
> L132: |Claude Code CLI|Code planning and implementation|Pilot shells out to it; it must be on your `PATH` and authentica

## 星数曲线

```mermaid
xychart-beta
    title "peterhoang1103991-cmd/pilot-ai-ticket-shipper 星数(近 2 点)"
    x-axis ["2026-10-26", "2026-10-27"]
    y-axis "stars" 57 --> 59
    line [58, 58]
```

2026-10-26 58 → 2026-10-27 58（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `4738ef22ce0b` · [字段定义](../../DATASET.md)*
