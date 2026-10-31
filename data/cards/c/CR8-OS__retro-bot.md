# CR8-OS/retro-bot

⭐ 14 · MIT · 推送 2026-10-22 · [GitHub](https://github.com/CR8-OS/retro-bot) · [官网](https://gather.co) · 个人维护

**Claude 会话用的敏捷回顾技能：复盘并把改进落到正确层级**

运行在 Claude Code / Cowork（Claude 桌面端）中的回顾（retrospective）插件：会话结束后触发结构化复盘，AI 先给出自我观察，再与用户共建回顾板（支持 WWW、Start/Stop/Continue、4Ls、Mad/Sad/Glad、Sailboat 五种格式），把每项改进路由到 Claude 配置的四个层级（Skill、Project、Claude.md、Process）并带版本化当场应用；每次回顾保存带日期的快照并维护持续审计日志。以插件市场或本地克隆方式安装，无外部服务与 API 依赖。作者声明仍在开发中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 把改进路由到 Skill/Project/Claude.md/Process 四层级并版本化应用
- 五种回顾格式（WWW 为默认）
- 带日期快照与持续审计日志（retro-log.md）
- 自包含，无其他技能或外部服务依赖

## 适用场景

- Claude 会话结束后跑一次复盘，把摩擦点固化成配置改进
- 跟踪 Claude 工作流配置随时间的演化记录
- 按不同场景选择回顾格式做团队式自省

## 场景标签

 · 领域:AI 协作工作流/开发者工具

## 证据(README 行号)

> L12: **An agile retrospective skill for your Claude collaboration sessions.**
> L63: After any Claude session, retro-bot runs a structured retrospective with you, and
> L157: - **Claude Code** or **Cowork** (Claude desktop): the environments retro-bot runs in

## 星数曲线

```mermaid
xychart-beta
    title "CR8-OS/retro-bot 星数(近 2 点)"
    x-axis ["2026-10-23", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-23 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `442a5e319e2c` · [字段定义](../../DATASET.md)*
