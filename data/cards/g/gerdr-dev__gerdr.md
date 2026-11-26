# gerdr-dev/gerdr

⭐ 6 · Go · MIT · 推送 2026-11-25 · [GitHub](https://github.com/gerdr-dev/gerdr) · [官网](https://gerdr.dev) · 个人维护

**多编程 agent 统一窗口：分屏会话、审批卡片与手机远程**

面向开发者的桌面/浏览器 GUI，用于在同一窗口管理 Claude Code、Codex 及任意 ACP agent：提供分屏、标签页与工作区，审批和提问以卡片形式一键处理，可在消息运行中途插话，支持会话回退与按目录恢复终端中的历史会话。界面本身可由 agent 修改，支持 TypeScript 插件与 skills/MCP。可从手机通过 relay（配对码+passkey）或 LAN 直连远程访问。Windows/iOS 发行包尚未提供，需从源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多 agent 同窗管理：分屏、标签页、工作区，支持任意 ACP agent 与内置 Gerdr Agent（GPT/DeepSeek API）
- 审批与提问以卡片呈现，一键批准命令或编辑
- 界面可由 AI 实时修改，附 TypeScript 插件与插件商店
- 远程访问：relay 配对码+passkey、Android/iOS 应用与 LAN 直连

## 适用场景

- 同时管理多个 Claude Code / Codex 会话而不切换终端
- 外出时从手机查看并继续指挥编码 agent
- 让 agent 之间互相分发任务并读取回复

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L15: **One window for all your coding agents.**
> L34: - **beyond Claude and Codex** — several accounts side by side, any ACP agent, and a built-in Gerdr Agent for GPT / 
> L51: - Desktop app (macOS / Windows) or any browser; remote access via relay (pairing codes + passkeys); Android and iOS


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `b983164969c9` · [字段定义](../../DATASET.md)*
