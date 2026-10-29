# huanyingtianhe/agents-chat

⭐ 26 · TypeScript · 推送 2026-09-23 · [GitHub](https://github.com/huanyingtianhe/agents-chat) · [官网](https://wljytt.japaneast.cloudapp.azure.com/) · 个人维护

**多 AI agent 聊天与编排界面，直连 ACP 协议 CLI agent**

基于 Next.js/React/SQLite 的独立 Web 聊天 UI，通过 Agent Client Protocol 直接连通 GitHub Copilot CLI、Claude Code 及任意 ACP 兼容 agent。功能含 @mention 路由、自动调度/讨论/流水线三种编排、文件附件、Files 文件浏览编辑、按 agent 选择模型、斜杠命令、应用内 ACP 登录、cron 定时任务、Azure Relay 远程 agent 与节点注册表，聊天历史存 SQLite。需 Node.js>=20 与至少一个 ACP 兼容 agent，提供 npm 运行与 Windows/Linux 预构建包及 systemd/计划任务部署脚本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 直连 ACP 兼容 CLI agent（Copilot CLI、Claude Code 等）
- 调度/讨论/流水线三种多 agent 编排模式
- 应用内 ACP 登录、per-agent 模型选择与 cron 定时任务
- 经 Azure Relay 连接远程 agent 并提供节点注册表

## 适用场景

- 在同一界面里与多个 CLI 编码 agent 对话并 @mention 分派
- 把多个 agent 按流水线或并行讨论编排执行任务
- 定时调度某个 agent 按 cron 表达式运行
- 连接并管理远程机器上的 agent 节点

## 场景标签

`多智能体` `聊天机器人` · 领域:Agent 开发

## 证据(README 行号)

> L3: A standalone multi-agent chat UI for **ACP (Agent Client Protocol)** agents. Direct communication with ACP-compatibl
> L212: - **Auto agent orchestration** — A scheduler agent decides which agent should act next, evaluates results, and pro
> L229: - **Relay agents** — Connect to remote agents on other machines via Azure Relay.

## 星数曲线

```mermaid
xychart-beta
    title "huanyingtianhe/agents-chat 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-29 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `d92120dac276` · [字段定义](../../DATASET.md)*
