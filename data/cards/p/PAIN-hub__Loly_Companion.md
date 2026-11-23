# PAIN-hub/Loly_Companion

⭐ 4 · JavaScript · 推送 2026-11-05 · [GitHub](https://github.com/PAIN-hub/Loly_Companion) · [官网](https://pain-hub.github.io/Loly_Companion/) · 个人维护

**监控 AI 编码 agent 的桌面悬浮屏岛伴侣**

面向编排自主 AI 编码 agent（Gemini CLI、Claude Code、Cursor 等）的开发者，提供固定在屏幕顶部的悬浮 notch 界面：实时展示 agent 的工具调用与文件改动，通过 Unix socket 或 HTTP hook 接收外部 agent 的事件，并可在悬浮条上批准或拒绝终端命令执行（Allow/Deny/Always）。内置自主多文件编码 agent（Gen-v5），支持文件读写、目录列举、命令执行等工具，工作区沙箱限制在仓库根目录内。数据与 API key 存储于本地 SQLite。提供 Windows/Linux/macOS 预编译包，也可 npm 源码运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 悬浮屏岛实时展示 agent 工具调用、执行输出与文件 diff（SSE 流式）
- 外部 agent 经 /tmp/coucou.sock 或 /api/hook 推送审批请求，一键批准/拒绝终端执行
- 多 Provider 架构：Gemini 默认，可切换 Claude、GPT-4o 与 Chrome Built-in AI（Gemini Nano）
- 审计日志、文件 diff、会话全部本地 SQLite 存储，无遥测

## 适用场景

- 让 Claude Code 等后台 agent 改代码时，不用切窗口就能看到它要执行什么命令并批准
- 在悬浮条上直接指挥内置 agent 检查、重构本地仓库文件
- 团队要求审计日志与凭据不出本机时用它本地留存记录

## 场景标签

`编码 Agent` `AI 助手` · 领域:编码与开发

## 证据(README 行号)

> L31: When autonomous agentic systems (such as Gemini CLI, Claude Code, Antigravity, and Cursor) perform complex multi-tu
> L89: - **IPC & HTTP Hooks**: External agents stream status events and approval requests via local Unix socket (`/tmp/cou
> L36: - **In-Pill Permission Approvals**: Grant or deny terminal executions (`Allow`, `Deny`, `Always`) directly from the

## 星数曲线

```mermaid
xychart-beta
    title "PAIN-hub/Loly_Companion 星数(近 3 点)"
    x-axis ["2026-10-29", "2026-11-08", "2026-11-23"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-10-29 3 → 2026-11-23 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 mid · 依据 README sha `ce752d1ead89` · [字段定义](../../DATASET.md)*
