# pardnchiu/Agenvoy

⭐ 642 · Go · AGPL-3.0 · 推送 2026-11-23 · [GitHub](https://github.com/pardnchiu/Agenvoy) · [官网](https://agenvoy.com/) · 个人维护 · 中文 README

**本地常驻的个人 AI agent 工具：一句话完成工具生成与任务自动化**

以单个 Go 二进制运行的本地守护进程式 AI agent harness：将对话拆解为步骤、调用工具并交付结果；当没有可用工具时先调用无密钥公共 API，否则自动编写脚本工具并在沙箱中测试后复用。内置 MCP 服务器与客户端，可与 Claude Code、Codex 等 agent 共享同一工具库；提供调度器、三层记忆、Web/TUI/Telegram/Discord 等多通道接入，数据存于本机 SQLite，命令默认在 macOS sandbox-exec 或 Linux bubblewrap 沙箱中执行。当前处于 review-and-cleanup 阶段。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 自动生成工具：检测能力缺口后编写、沙箱测试并注册脚本工具
- 内置 MCP 服务器，Claude Code/Codex/OpenCode 可共享全部沙箱工具
- 一句话创建一次性与 cron 定时任务，结果推送到指定渠道
- 数据、密钥留本机：SQLite 存储 + OS keychain + 默认沙箱执行

## 适用场景

- 用一句话让 agent 查询实时数据并生成报告
- 把每日股票/commit 汇总等重复工作做成定时任务
- 让本地文件问答（RAG）代替翻找文档
- 多个 AI agent 共享一套自动构建的工具库

## 场景标签

`AI 助手` `RAG` · 领域:对话与助手

## 证据(README 行号)

> L87: Agenvoy is a Taiwan-developed AI Agent Harness by Pardn Chiu, built to turn conversation into completed work on you
> L211: |MCP server & client|Shares every sandboxed tool with Claude Code, Codex and any MCP client; calls external MCP se

## 星数曲线

```mermaid
xychart-beta
    title "pardnchiu/Agenvoy 星数(近 25 点)"
    x-axis ["2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25"]
    y-axis "stars" 477 --> 901
    line [512, 522, 557, 594, 642, 701, 762, 809, 866, 512, 570, 580, 586, 594, 599, 603, 604, 608, 615, 618, 621, 624, 628, 634, 642]
```

2026-10-25 512 → 2026-11-25 642（+130）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 high · 依据 README sha `25aa7b16808d` · [字段定义](../../DATASET.md)*
