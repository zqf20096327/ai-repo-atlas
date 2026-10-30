# leapmux/leapmux

⭐ 116 · Go · NOASSERTION · 推送 2026-10-29 · [GitHub](https://github.com/leapmux/leapmux) · [官网](https://leapmux.dev) · 组织维护

**在单一工作区内并行运行多个 AI 编程 Agent 的多路复用器**

面向同时使用多个编程 Agent 的开发者：将 Claude Code、Codex、Cursor 等 30 种 Agent 与 shell 终端组织在同一工作区，每个 Agent 绑定独立 git worktree 与分支，界面支持平铺/浮动窗口，可在本地或远程机器运行，会话跨重启保持。架构为单个 Go 二进制 + SolidJS 前端 + Tauri 桌面壳，分 Frontend/Hub/Worker 三组件，Frontend↔Worker 流量经后量子 Noise_NK 加密、Hub 中继但不可读内容；Worker 出站连接可位于 NAT 后。以浏览器或原生桌面应用使用，源码构建需 Go/Node/Bun/Rust 等较多前置依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 30 种编程 Agent（Claude Code、Codex、Cursor、Gemini CLI 等）
- 每 Agent 独立 git worktree/分支，平铺或浮动窗口布局，会话跨重启保持
- Frontend↔Worker 后量子端到端加密，Hub 中继但无法读取内容
- 单一二进制多模式运行（solo/hub/worker/dev），Hub 存储支持 SQLite/PostgreSQL/MySQL 等 7 种

## 适用场景

- 同时跑三四个编程 Agent 时避免共享工作树互相覆盖
- 为每个 Agent 分配独立分支并统一监控进度
- 在远程机器上运行 Agent 会话并在本地浏览器接管

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L16: LeapMux runs several coding agents and shell terminals in one workspace.
> L23: ## Supported Agents
> L25:  Claude Code&nbsp;

## 星数曲线

```mermaid
xychart-beta
    title "leapmux/leapmux 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 115 --> 117
    line [116, 116]
```

2026-10-18 116 → 2026-10-30 116（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `3fb27d5aaa55` · [字段定义](../../DATASET.md)*
