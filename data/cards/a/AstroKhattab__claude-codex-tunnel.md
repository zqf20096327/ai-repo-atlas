# AstroKhattab/claude-codex-tunnel

⭐ 4 · Shell · MIT · 推送 2026-11-21 · [GitHub](https://github.com/AstroKhattab/claude-codex-tunnel) · 个人维护

**让 Claude Code 与 Codex CLI 互相委派任务并直播对话的 CLI**

以一个 `tunnel` 命令连接 Claude Code 与 OpenAI Codex 两个 CLI：一侧以 markdown brief 交付任务，另一侧以 `codex exec` 或 `claude -p` 启动真实进程执行，回传带 verdict 的 markdown 报告，并在终端窗口直播对话流。安装脚本注册 tunnel 命令、两侧的 agent skills 与两个 Claude subagents。默认 review/research 只读、写操作沙箱化，禁止 commit/push/deploy，区分 DONE/APPROVE/REVISE/BLOCK/FAILED 五种裁决；依赖用户已登录的 CLI 与既有计划，无需 API key。

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

- 双向委派：Claude→Codex 与 Codex→Claude，以子进程方式启动对方 CLI
- 无需服务器、API key 或 MCP 配置，复用已登录的 CLI 与订阅
- live 终端窗口展示发出的 brief、对方执行的命令与返回的 verdict
- 安全默认值：review 只读、写操作沙箱、敏感动作需人工批准

## 适用场景

- 让 Codex 复查 Claude Code 写的代码提交
- 把 PLAN.md 中的计划交给另一个模型实现
- 在同一 bug 上获取另一个模型模型的第二意见

## 场景标签

`多智能体` `代码审查` · 领域:Agent 开发

## 证据(README 行号)

> L19: - **Real integration.** It starts the other CLI as a real process (`codex exec` or
> L44: |a skill that teaches Claude to delegate to Codex|`~/.claude/skills/claude-codex-tunnel/`|

## 星数曲线

```mermaid
xychart-beta
    title "AstroKhattab/claude-codex-tunnel 星数(近 2 点)"
    x-axis ["2026-11-23", "2026-11-24"]
    y-axis "stars" 3 --> 5
    line [4, 4]
```

2026-11-23 4 → 2026-11-24 4（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `de99647ebe4e` · [字段定义](../../DATASET.md)*
