# airtaxi/LidGuard

⭐ 13 · C# · MIT · 推送 2026-09-28 · [GitHub](https://github.com/airtaxi/LidGuard) · [官网](https://www.nuget.org/packages/lidguard) · 个人维护 · 中文 README

**让本地 AI 编程 agent 在合盖后继续运行的电源管理工具**

以 .NET 10 NativeAOT 全局工具（dotnet tool）分发的跨平台电源管理助手：跟踪 Codex、Claude Code、GitHub Copilot CLI、OpenCode 的会话，在受保护工作进行中临时阻止闲置睡眠与合盖睡眠，结束后恢复原系统电源策略，并可配置自动 Sleep/Hibernate。提供 hooks/MCP 安装命令、WSL 集成、Provider MCP 兜底通道、ask-before-sleep 回复与 Web Push 通知伴随服务器、高温紧急休眠等安全控制。支持 Windows、systemd/logind Linux、macOS；官方测试目前仅覆盖 Windows 上的 Codex，其余平台与 provider 的实际验证仍在进行。以韩国语/英语双语 README 发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 面向 AI 编程 agent 会话（Codex/Claude Code/Copilot CLI/OpenCode）的睡眠阻止与合盖保护
- 会话结束后自动 Sleep/Hibernate 并恢复原 OS 电源策略
- WSL hook/MCP 安装与面向其他 agent 的 Provider MCP 通道
- ask-before-sleep 回复、高温紧急休眠、SoftLock 等安全控制与 Web Push 通知服务器

## 适用场景

- 合上笔记本盖子让本地编程 agent 继续长任务
- agent 完成后自动让机器休眠以省电
- 合盖期间通过手机/浏览器回复 agent 的追问

## 场景标签

 · 领域:开发者工具/电源管理

## 证据(README 行号)

> L10: LidGuard lets long-running local AI coding agents keep working after you close your laptop lid. It tracks Codex, Cl
> L20: - Windows-to-WSL hook and MCP setup, so providers running inside WSL can call the Windows LidGuard runtime without 
> L114: - Provider integration: Codex, Claude Code, GitHub Copilot CLI, and OpenCode hooks/plugins; hook install/status/re

## 星数曲线

```mermaid
xychart-beta
    title "airtaxi/LidGuard 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-31"]
    y-axis "stars" 11 --> 14
    line [12, 13, 13]
```

2026-10-18 12 → 2026-10-31 13（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `3423adf17a52` · [字段定义](../../DATASET.md)*
