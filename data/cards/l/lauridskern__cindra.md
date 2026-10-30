# lauridskern/cindra

⭐ 35 · TypeScript · AGPL-3.0 · 推送 2026-05-18 · [GitHub](https://github.com/lauridskern/cindra) · 个人维护

**桌面端界面：运行 Forgecode 编码代理工作流**

基于 Tauri 2 桌面壳与 React/Vite/TypeScript 前端的编码代理客户端，用于在 Forgecode（以 vendor 目录内嵌）之上运行代理式编码工作流：提供项目聊天、终端输出与多会话工作区，底层含 Rust 命令层。面向使用 Forgecode 的开发者，需本地具备 Bun、Rust 工具链与 Tauri 系统依赖，从源码运行（bun run tauri dev）。README 自述为早期软件，应用、打包与 Forgecode 集成仍在调整。许可证 AGPL-3.0-or-later。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Tauri 2 桌面壳 + React 工作区 UI
- 项目聊天、终端输出与多会话工作
- Forgecode 以 vendor/ 目录内嵌 vendored

## 适用场景

- 在桌面端管理并运行 Forgecode 编码代理工作流
- 同时进行多个项目会话并查看终端输出

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: Cindra is a desktop interface for running coding-agent workflows on top of Forgecode, the #1 harness for agentic cod
> L11: - Tauri 2 desktop shell

## 星数曲线

```mermaid
xychart-beta
    title "lauridskern/cindra 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-30 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `8d8578003c8d` · [字段定义](../../DATASET.md)*
