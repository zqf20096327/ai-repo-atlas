# BIGPPWONG/EdgeBox

⭐ 212 · TypeScript · GPL-3.0 · 推送 2026-04-22 · [GitHub](https://github.com/BIGPPWONG/EdgeBox) · 个人维护 · 中文 README

**本地运行的 LLM Agent 桌面沙箱：GUI+CLI，MCP 协议全支持**

基于 E2B Code Interpreter 开源代码改造的本地沙箱桌面应用（Electron+React 前端、Node.js 后端），把云端沙箱能力搬到本地 Docker 容器中。除 CLI 外通过内嵌 VNC 提供 Ubuntu 图形桌面，预装 Chrome 与 VS Code，agent 可程序化控制鼠标键盘、截屏、操作桌面应用。全部能力经 MCP HTTP 接口暴露，含代码执行（Python/TS/R/Java/Bash）、文件系统、shell、容器生命周期管理与多会话隔离（x-session-id）。运行前提是本机安装 Docker Desktop；桌面工具需在设置中启用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- VNC 图形桌面环境，支持 GUI 自动化与截屏的 Computer Use
- 完整 MCP 协议暴露 20+ 工具（代码执行/文件/鼠标键盘/窗口管理）
- 每会话映射独立 Docker 容器，支持多会话并发与资源限额
- 兼容任意 MCP 客户端（Claude Desktop、OpenWebUI、LobeChat 等）

## 适用场景

- 让 LLM agent 在隔离容器中安全执行 AI 生成的代码
- 通过 MCP 让 agent 操控浏览器、VS Code 等桌面应用
- 本地运行数据隐私敏感的 agent 工作负载，替代云端沙箱

## 场景标签

`GUI 自动化` `浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L10:  A fully-featured, GUI-powered local LLM Agent sandbox with complete support for the MCP protocol.
> L59: - **Standardized Protocol**: All sandbox features are exposed via the **MCP (Model Context Protocol)** HTTP interfa
> L119: **[LLM Agent (Claude, GPT, etc.)]** `<- MCP (HTTP Stream) ->` **[EdgeBox App]** `<- Docker API ->` **[Isolated San

## 星数曲线

```mermaid
xychart-beta
    title "BIGPPWONG/EdgeBox 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-31"]
    y-axis "stars" 210 --> 213
    line [212, 211, 212]
```

2026-10-18 212 → 2026-10-31 212（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `c435381265f6` · [字段定义](../../DATASET.md)*
