# notch-ai/autosteer

⭐ 67 · TypeScript · MIT · 推送 2025-11-26 · [GitHub](https://github.com/notch-ai/autosteer) · 组织维护

**管理多工作区 Claude Code 会话的桌面应用**

基于 Electron 的跨平台桌面应用，为 Claude Code 提供多工作区（worktree）管理：每个工作区有独立文件系统与上下文，支持持久化会话保存与恢复、按项目隔离的标签页、令牌用量与成本统计、MCP 服务器管理与认证处理、协议消息追踪查看器及自定义斜杠命令扩展。需先安装 Claude Code。macOS/Linux/Windows(WSL) 提供安装包，配置存储于 ~/.autosteer/，数据本地保存且无遥测。面向使用 Claude Code 的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- worktree 隔离的多工作区管理与持久化会话
- 令牌用量与成本按消息/工作区统计
- MCP 服务器管理与 MCP 认证处理
- 协议追踪查看器与 JSONL trace 文件（自动轮转）

## 适用场景

- 在多个项目间切换并保留各自的 Claude Code 会话上下文
- 监控 Claude Code 的令牌消耗与成本
- 管理与调试 MCP 服务器及 SDK 消息流

## 场景标签

 · 领域:开发者工具/LLM 客户端

## 证据(README 行号)

> L8: AutoSteer is a desktop application that enhances your Claude Code experience with multi-workspace management. Built 
> L27: - Status Panel - View session information, manage MCP servers, and handle MCP authentication

## 星数曲线

```mermaid
xychart-beta
    title "notch-ai/autosteer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 66 --> 68
    line [67, 67]
```

2026-10-18 67 → 2026-10-26 67（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `fde632d06e4b` · [字段定义](../../DATASET.md)*
