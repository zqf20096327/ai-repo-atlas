# xiaokaige1130-maker/grok-desktop

⭐ 23 · JavaScript · 推送 2026-07-24 · [GitHub](https://github.com/xiaokaige1130-maker/grok-desktop) · [官网](https://github.com/xiaokaige1130-maker/grok-desktop/releases/latest) · 个人维护 · 中文 README

**官方 Grok CLI 的跨平台桌面工作区客户端**

Electron 桌面应用，将已安装并登录的官方 Grok CLI 的 agent 能力封装为独立窗口工作区：通过 ACP 连接 grok agent 后端，支持多会话并行、计划面板、行级文件 Diff、模型与思考强度选择、审批/智能/完全访问三档权限模式，并继续管理 CLI 已有的 MCP、插件、Skills 与跨会话记忆。面向 Windows/macOS/Linux 用户提供安装包；不内置账号或模型服务，需先安装并登录官方 grok CLI。

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

- 通过 ACP 连接官方 grok agent 后端的多会话桌面工作区
- 计划面板、行级文件 Diff、三档权限模式
- MCP / 插件 / Skills / 记忆的侧栏管理
- Windows / macOS / Linux 安装包，中英双语界面

## 适用场景

- 在独立桌面窗口中长期运行多个 Grok CLI agent 会话
- 审查 agent 的计划步骤、工具调用与文件改动
- 按项目可信度切换权限模式进行日常开发

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L52: > Grok Desktop 是社区项目，不是 xAI 官方产品。它不内置账号或模型服务，而是连接你电脑上已经安装并登录的官方 `grok` CLI。
> L63: - **Agent 后端**：官方 `grok agent`，通过 ACP 通信。
> L277: - **Agent backend:** official `grok agent`, connected through ACP.

## 星数曲线

```mermaid
xychart-beta
    title "xiaokaige1130-maker/grok-desktop 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-29 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `6d8116199f34` · [字段定义](../../DATASET.md)*
