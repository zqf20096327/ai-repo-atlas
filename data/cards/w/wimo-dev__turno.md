# wimo-dev/turno

⭐ 6 · TypeScript · Apache-2.0 · 推送 2026-11-19 · [GitHub](https://github.com/wimo-dev/turno) · [官网](https://turno.wimo.dev) · 组织维护

**给编码 agent 用户的 CLI：多账号切换且保留会话、MCP 登录与浏览器**

turno 是面向同时使用工作与个人账号运行编码 agent 的开发者的 CLI 工具。它为每个 agent 账号建立 profile：跨账号恢复或分叉会话；以本地网关（mcpd，127.0.0.1）为每账号登录一次 OAuth 远程 MCP 服务器并按 shared/project/session 作用域共享服务器进程；为每个身份提供独立 Chrome 配置的浏览器包；提供 Claude Code 插件的三个 skill 与按文件夹选账号的规则。支持 macOS/Linux，Node 22.11+，凭据存于 macOS Keychain 或 Linux Secret Service，不转发模型流量。Windows 不支持。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 跨账号会话 handoff/fork（turno session handoff）
- 本地 MCP 网关：每账号一次 OAuth 登录、共享服务器进程并缓存 tool lists
- 每个身份独立 Chrome 配置（turno-browser 独立包）
- 支持 Claude Code、Codex CLI、Copilot CLI、Cursor CLI 的同一套 profile 与文件夹规则

## 适用场景

- 在工作和个人账号间切换 Claude Code 并保留对话上下文
- 多会话共享 MCP 服务器以降低内存占用
- 按项目文件夹自动选择使用的账号
- 为脚本和 agent 会话以非交互模式运行账号切换

## 场景标签

 · 领域:开发者工具/编码 agent 账号与会话管理

## 证据(README 行号)

> L14: sign-ins. turno is for people who use a work account and a personal account with their coding
> L19: - **Your MCP sign-ins.** One local gateway logs in to each remote OAuth server once per account
> L85: - **One MCP gateway for every session.** `mcpd` listens on `127.0.0.1`, answers `initialize` and


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `5197bf7e7b15` · [字段定义](../../DATASET.md)*
