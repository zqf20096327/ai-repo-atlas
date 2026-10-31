# istota-project/istota

⭐ 14 · Python · EUPL-1.2 · 推送 2026-10-30 · [GitHub](https://github.com/istota-project/istota) · [官网](https://istota.cynium.com) · 组织维护

**自托管个人操作系统：AI agent 加 Web UI 管理日常数据**

部署在用户自有 Debian 13 服务器或 Apple silicon Mac（Lima VM）上的个人系统：AI agent 通过维护的工具集操作聊天、持久记忆、后台任务与若干 Web 模块（feeds/简报、健康、位置、记账）。任务经 SQLite 队列执行，sandbox 用 bubblewrap 做文件系统隔离、网络走代理白名单、凭据由 broker 注入。模型后端可选 Claude Code CLI 或 OpenAI 兼容端点（Anthropic API/OpenRouter/本地模型服务器）。Pre-1.0，配置与 schema 可能变更；要求专用机器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | EUPL-1.2 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- SQLite 任务队列：状态、重试、确认、取消与用量记录
- bubblewrap 文件系统隔离、网络代理白名单、凭据 broker 注入
- 双模型路径：Claude Code CLI 或 OpenAI 兼容端点（含本地模型服务器）
- 多用户隔离：每用户独立文件、凭据、记忆与任务队列

## 适用场景

- 在自己的服务器上运行带持久记忆的个人 AI 助手
- 通过邮件、WhatsApp、SMS、Nextcloud Talk 或 CLI 向 agent 委派工作
- 用 Beancount、健康记录、位置历史等模块集中管理个人数据

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L5:  An open-source personal operating system with an AI agent and a first-class web UI.
> L11: Istota runs on your own server or in a VM on your Mac. It combines chat, persistent memory, background jobs, and we

## 星数曲线

```mermaid
xychart-beta
    title "istota-project/istota 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `ad905ceb5082` · [字段定义](../../DATASET.md)*
