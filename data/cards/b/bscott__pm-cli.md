# bscott/pm-cli

⭐ 16 · Go · MIT · 推送 2026-08-30 · [GitHub](https://github.com/bscott/pm-cli) · 个人维护

**供终端与 AI agent 使用的 ProtonMail 命令行客户端**

基于 Go 的命令行邮件客户端，通过 Proton Bridge 的 IMAP/SMTP 接口访问 ProtonMail，支持收发/回复/转发、附件下载、草稿、标签、搜索、联系人、邮箱管理与新邮件监听。面向 AI agent 工作流设计：提供 --json 与 --help-json 命令模式输出、返回情感/优先级/行动项的 summarize 语义命令、幂等键防止重复发送。密码存于系统 keyring，无桌面会话时可用环境变量替代。运行需 Proton Bridge 在线。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通过 Proton Bridge IMAP/SMTP 完成邮件读写与搜索等全套操作
- --help-json 输出完整命令模式，--json 机器可读输出
- mail summarize 返回 sentiment/priority/action_required 语义摘要
- 幂等键机制防止自动化场景重复发送

## 适用场景

- 在终端收发和管理 ProtonMail 邮件
- 让 AI agent 通过 CLI 与 JSON 输出操作邮箱
- 服务器等无桌面环境自动监控与发送邮件

## 场景标签

 · 领域:邮件/终端工具

## 证据(README 行号)

> L3: A command-line interface for ProtonMail via Proton Bridge IMAP/SMTP. Designed for terminal use and AI agent integrat
> L159: ## AI Agent Integration
> L163: ```bash

## 星数曲线

```mermaid
xychart-beta
    title "bscott/pm-cli 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `3e9da0d78042` · [字段定义](../../DATASET.md)*
