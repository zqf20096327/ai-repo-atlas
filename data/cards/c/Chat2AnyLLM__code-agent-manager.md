# Chat2AnyLLM/code-agent-manager

⭐ 51 · Go · 推送 2026-08-17 · [GitHub](https://github.com/Chat2AnyLLM/code-agent-manager) · [官网](https://chat2anyllm.github.io/code-agent-manager/) · 组织维护

**统一管理 17 种 AI 编程助手的 CLI/桌面工具**

Go 编写的 CLI（CAM），外加 Tauri 桌面壳与 Go sidecar API，用于在单一界面安装、配置、升级和启动 17 种 AI 编程助手（Claude、Codex、Gemini、Qwen、Copilot、Cursor 等），统一管理 API key（.env）、SQLite 状态、指令文件（CLAUDE.md/AGENTS.md 等）、技能、插件与 381+ 预配置 MCP 服务器目录，并提供 cam doctor 诊断与交互式 TUI。从源码构建安装，需要 Go 1.26.2+，桌面构建还需 Cargo/Rust 环境。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一 CLI 管理 17 种 AI 编程助手的安装/配置/升级/卸载
- 381+ 预配置 MCP 服务器目录
- 统一管理指令文件、技能、插件与 agent 配置
- Tauri 桌面应用与 CLI 共用同一 Go 后端

## 适用场景

- 同时使用多个 AI 编程助手时统一管理配置与 API key
- 跨助手同步指令文件与安装 MCP 服务器
- 批量升级或卸载多个编码助手

## 场景标签

 · 领域:开发者工具/AI 助手管理

## 证据(README 行号)

> L8: Tired of juggling multiple AI coding assistants? **CAM** is a unified Go CLI to manage configurations, instructions,
> L69: CAM now uses a **Tauri desktop shell** with a **Go sidecar API**. The same Go backend packages power both the termi
> L166: CAM supports **17 AI coding assistants**:

## 星数曲线

```mermaid
xychart-beta
    title "Chat2AnyLLM/code-agent-manager 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 50 --> 52
    line [51, 51]
```

2026-10-18 51 → 2026-10-29 51（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `c15e0324f5d7` · [字段定义](../../DATASET.md)*
