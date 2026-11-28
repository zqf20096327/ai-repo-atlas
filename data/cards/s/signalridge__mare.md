# signalridge/mare

⭐ 5 · Rust · Apache-2.0 · 推送 2026-11-27 · [GitHub](https://github.com/signalridge/mare) · [官网](https://signalridge.github.io/mare/) · 个人维护

**可扩展的 AI 编码 agent 框架：Rust 内核 + Lua 5.5 热重载插件**

mare 是一个以 Rust 为内核、Lua 5.5 为扩展层的编码 agent 框架：内核负责进程沙箱、会话持久化与终端 UI 渲染，而 agent loop、工具、模型提供方、压缩、权限策略与主题均以基于 cordis-lua 的插件实现，可同名单覆盖并 /reload 热替换。配置通过 init.lua 完成，支持 git 包管理。提供 TUI、headless --json、RPC、--web WebSocket 与 ACP 编辑器接口多种前端。安装覆盖一行脚本、brew/scoop/nix/yay、Docker/GHCR、发布包与 cargo 源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- agent loop、工具、模型提供方、权限策略等全部为可热重载的 Lua 5.5 插件
- Rust 层提供 OS 沙箱（bubblewrap/Landlock/Seatbelt/受限令牌）、崩溃安全 JSONL 会话与编辑前快照
- 一套会话模型对接 TUI、headless、RPC、Web 与 ACP 编辑器多种前端
- 支持 git 包管理（mare.plugins.add 与 mare-lock.json）与插件 override 热替换

## 适用场景

- 在项目中通过终端 TUI 运行 AI 编码 agent
- 用 Lua 插件定制 agent 工具、权限策略与 UI 主题
- 在脚本与 CI 中以 headless --json 方式调用 agent
- 通过 ACP 将 agent 接入编辑器

## 场景标签

`Agent 框架` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L4:  A hyperextensible agent harness.
> L17: At its core, mare is a small Rust kernel that confines processes, keeps sessions durable, renders the terminal UI (


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `8f77ea2c7f7e` · [字段定义](../../DATASET.md)*
