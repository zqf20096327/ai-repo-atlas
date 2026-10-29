# alicomert/pixcode

⭐ 19 · JavaScript · NOASSERTION · 推送 2026-09-20 · [GitHub](https://github.com/alicomert/pixcode) · [官网](https://github.com/alicomert/pixcode) · 个人维护 · 中文 README

**自托管 AI 编码 agent 控制台：统一管理多种编码 CLI**

本地 Web 与桌面工作区，封装开发者已在使用的编码 CLI（Claude Code、Cursor CLI、OpenAI Codex、Gemini CLI、Qwen Code、OpenCode），在其外围提供项目选择、聊天历史、文件浏览、Shell、Git/本地变更跟踪、命令中心、多 agent 编排（Agent Team/顺序交接/多模型评审/决策辩论）、后台守护进程、Telegram 远程控制与 px_ API key 的 REST/WebSocket 自动化接口。支持 MCP 服务器管理与插件加载，源码与凭据保留在本机。需 Node.js 22+，提供 npm 安装与三平台桌面安装包；无单元测试脚本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 6 种编码 CLI 共享同一工作区与提供方面板（auth/安装检查/MCP/会话历史）
- 4 种内置多 agent 编排工作流与后台编排控制平面
- px_ API key 暴露 REST/WebSocket API 供外部自动化
- Telegram 配对作为远程提示与通知控制面
- 守护进程（systemd/LaunchAgent/自启动）保持 CLI 会话存活

## 适用场景

- 在同一界面切换管理多个 AI 编码 CLI 的项目会话
- 通过 REST API 从脚本/CI/看板创建会话并运行 agent
- 离开电脑后经 Telegram 远程下发提示并接收完成通知
- 查看 agent 刚修改了哪些文件并跳转到改动位置

## 场景标签

`编码 Agent` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L35: Pixcode is a local web and desktop workspace for AI coding agents. It wraps the
> L69: Pixcode gives every supported coding CLI a shared workspace without hiding the
> L143: Pixcode includes a project-aware orchestration control plane for background

## 星数曲线

```mermaid
xychart-beta
    title "alicomert/pixcode 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `3b1f3c74b20f` · [字段定义](../../DATASET.md)*
