# DIYgod/pinky

⭐ 2,782 · Go · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/DIYgod/pinky) · 个人维护

**让 AI agent 在用户审批下操作 iPhone/Android 手机**

Pinky 是一个跨平台（macOS/Windows/Linux）桌面应用，通过 MCP 协议让任意 agent（如 Claude Code、Cursor 或脚本）操作真实的 iPhone 或 Android 手机；每一步操作经其 gateway 强制执行审批规则，支付等风险操作默认等待用户确认，全程留有截图与录屏记录。手机端 App 也可独立运行任务，模型可自选。当前状态为 pre-alpha，支持 Android 10–17 与 iOS 17.4+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | `idea` | |

## 能力要点

- gateway 强制审批：规则由 Pinky 执行，agent 无法自行批准
- 银行/钱包/密码管理类应用默认对 agent 不可见
- Android 13+ 提供隐藏第二屏，手机主屏归用户
- 每次运行生成带步骤标注的录屏，可导出 HTML 报告

## 适用场景

- 让 agent 代为在手机上发消息、下单，同时保留人工审批
- 把手机操作任务交给手机端 App 独立完成，无需电脑
- 定时或条件触发的手机自动化任务

## 场景标签

`GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L7: Pinky lets any agent (Claude Code, Claude Desktop, Codex, Cursor or a script) operate a real iPhone or Android phone
> L11: - **Any agent, one click.** Settings › Agents connects Claude Code, Claude Desktop, Codex, Cursor and more, and any
> L17:  You decide what waits: Pinky You approve the risky steps. Payments, trades and transfers wait for your click; in S

## 星数曲线

```mermaid
xychart-beta
    title "DIYgod/pinky 星数(近 12 点)"
    x-axis ["2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26"]
    y-axis "stars" 2008 --> 2852
    line [2078, 2139, 2208, 2287, 2373, 2458, 2535, 2585, 2637, 2675, 2717, 2782]
```

2026-11-13 2,078 → 2026-11-26 2,782（+704）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `d5a6380a1d91` · [字段定义](../../DATASET.md)*
