# ThomasTartrau/n8n-nodes-claude-code-cli

⭐ 77 · TypeScript · MIT · 推送 2026-10-07 · [GitHub](https://github.com/ThomasTartrau/n8n-nodes-claude-code-cli) · 个人维护

**在 n8n 工作流中运行 Claude Code 的社区节点**

面向 n8n 用户的社区节点，通过 Docker exec 或 SSH 连接 claude-code-runner 容器，在工作流中调用 Claude Code CLI。提供 Execute Prompt、Execute with Context、Continue/Resume Session 四种操作，支持多模型选择（Opus/Sonnet/Haiku）、细粒度工具权限控制、MCP 服务器挂载与多轮会话，输出包含成本与 token 用量。README 给出 MR/PR 代码审查、自动文档、自动修 bug、客服助手与编码机器人等用例。安装经 n8n 社区节点面板或 npm，需部署配套 Docker 容器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Docker exec / SSH 两种连接方式运行 Claude Code
- 四种节点操作：执行提示词、带上下文执行、继续/恢复会话
- 工具权限细粒度控制（允许 Read/Grep，阻止 rm、sudo、写 .env）
- 输出包含 sessionId、成本估算与 token 用量

## 适用场景

- 在 n8n 中搭建 GitLab/GitHub MR/PR 自动代码审查流水线
- 代码推送后自动生成文档并提交 PR
- Sentry 告警触发自动分析并修复 bug
- 在 Telegram/Slack/Discord 上构建编码问答机器人

## 场景标签

`工作流自动化` `代码审查` `编码 Agent` · 领域:效率与自动化

## 证据(README 行号)

> L8: **🤖 Bring the power of Claude Code AI directly into your n8n workflows**
> L43: The node uses `docker exec` to communicate with claude-code-runner. This requires:
> L28: In n8n: **Settings > Community Nodes > Install > `n8n-nodes-claude-code-cli`**

## 星数曲线

```mermaid
xychart-beta
    title "ThomasTartrau/n8n-nodes-claude-code-cli 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 76 --> 78
    line [77, 77]
```

2026-10-18 77 → 2026-10-27 77（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `390a09f34550` · [字段定义](../../DATASET.md)*
