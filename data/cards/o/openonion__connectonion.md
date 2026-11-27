# openonion/connectonion

⭐ 1,566 · Python · Apache-2.0 · 推送 2026-11-26 · [GitHub](https://github.com/openonion/connectonion) · [官网](https://docs.connectonion.com) · 组织维护

**面向 AI agent 的命令行工具集：一条 co 命令接入邮件、浏览器与聊天工具**

ConnectOnion 提供 CLI 工具 co，让用户和 AI agent 通过命令行访问 Gmail/Outlook、Chrome、文件、聊天应用与 issue 跟踪器等工具；agent 通过 --help 按需发现命令。附带 co rem 功能，将邮件与编码会话上下文整理为本机 Markdown 页面供后续任务复用。安装脚本使用 uv 隔离 Python 环境；每日调度目前要求 macOS；所选来源内容会发送给所配置的模型。另提供 Python 框架用于构建自有 agent。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一 co 命令行统一访问邮件、日历、浏览器、聊天与 issue 工具
- agent 经 --help 按需发现命令，工具 schema 不预占上下文
- co rem 将邮件与编码会话整理为本机关联 Markdown 页面
- co audit 依据 agent 阅读方式为 CLI 帮助页评分

## 适用场景

- 让 Claude Code/Codex 等编码 agent 直接操作我的收件箱和日历
- 把邮件和编码会话的上下文沉淀成本地笔记供后续任务复用
- 通过命令行管道与脚本组合自动化日常工作流

## 场景标签

`工作流自动化` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L5: **The agent CLI harness. CLI is all you need.**
> L277: ConnectOnion is also a Python framework for building your own agents on the

## 星数曲线

```mermaid
xychart-beta
    title "openonion/connectonion 星数(近 16 点)"
    x-axis ["2026-10-25", "2026-10-29", "2026-10-30", "2026-11-01", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-16", "2026-11-19", "2026-11-22", "2026-11-23", "2026-11-27"]
    y-axis "stars" 1495 --> 1573
    line [1501, 1502, 1503, 1504, 1501, 1507, 1553, 1560, 1561, 1563, 1564, 1565, 1564, 1565, 1567, 1566]
```

2026-10-25 1,501 → 2026-11-27 1,566（+65）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `b93732fa61d1` · [字段定义](../../DATASET.md)*
