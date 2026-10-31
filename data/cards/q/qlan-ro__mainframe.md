# qlan-ro/mainframe

⭐ 44 · TypeScript · MIT · 推送 2026-10-27 · [GitHub](https://github.com/qlan-ro/mainframe) · [官网](https://github.com/qlan-ro/mainframe) · 个人维护

**统一界面编排 AI 编码 agent 的开发环境（桌面+守护进程+移动端）**

由无头守护进程与客户端两部分构成：守护进程生成并监管 Claude Code、Codex 等 agent CLI，管理项目与会话历史，暴露 HTTP/WebSocket API；客户端包括桌面应用（内建守护进程）、未发布的移动伴侣应用，可通过 Cloudflare Tunnel 配对远程守护进程。桌面端提供文件编辑、沙盒预览、看板任务管理、@引用上下文等功能，并有基于 manifest.json + activate() 的插件系统。作者声明项目为个人周末项目、进行中、Windows/Linux 未测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 守护进程生成并监管 Claude/Codex 等 agent CLI，暴露 HTTP/WS API
- 多项目会话管理、应用内文件编辑与沙盒预览
- 通过命名隧道配对远程守护进程与移动伴侣应用
- 能力声明的插件系统，Claude 适配器本身即插件

## 适用场景

- 在一个界面里同时管理多个 AI 编码 agent 的会话
- 在服务器上无头运行 agent 并从桌面或手机远程操控
- 基于守护进程 API 构建自己的 UI 或自动化集成

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L24: Mainframe brings all your AI coding agents into one interface. Instead of juggling terminal windows, switching betw
> L40: - **The daemon** — a headless service that does the real work: spawns and supervises the agent CLIs, owns projects 
> L44: claude · codex CLIs  ◄── spawns ──  DAEMON  ◄── HTTP/WS ──  desktop app · mobile app · your tools

## 星数曲线

```mermaid
xychart-beta
    title "qlan-ro/mainframe 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-31 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `0739dded0024` · [字段定义](../../DATASET.md)*
