# 1jehuang/jcode

⭐ 21,002 · Rust · MIT · 推送 2026-10-18 · [GitHub](https://github.com/1jehuang/jcode) · [官网](https://jcode.sh) · 个人维护

**Rust 编写的编码 agent 运行器：并行跑大量 agent 且低内存**

用 Rust 编写的终端编码 agent 工具（TUI/CLI），面向多 agent 并行开发流程。核心机制：无头 swarm worker 每会话额外内存约 3.1 MB，支持在同一仓库生成多个 agent 并由服务器管理协作（文件变更通知、DM/广播消息、自动冲突处理）；agent 可自主生成子 swarm。附带 agentgrep 检索工具返回文件结构并按已见内容裁剪结果以节省上下文。安装提供 macOS/Linux 一键脚本，Windows 另有说明。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 0.9 天,年发版 100,44 位贡献者
- 涨星:近 1 天 **+62**(自 20261016 起算)
- 平台:WINDOWS / MACOS / LINUX · 协议:—

## 能力要点

- 多 agent swarm：服务器管理的协作、消息通道与冲突通知
- agentgrep 工具返回文件结构并自适应裁剪以节省上下文
- 支持 Claude OAuth 与 OpenAI Codex OAuth 等多种 provider
- self dev 模式：agent 可修改、构建、测试自身源码并热重载

## 适用场景

- 在同一仓库并行运行数十个编码 agent
- 让多个 agent 协作修改代码并自动处理文件冲突
- 作为终端 TUI 编码 agent 日常开发工具

## 场景标签

`编码 Agent` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L7:  High-performance coding agents.
> L8:  Run dozens of agents in parallel without melting your machine. More agents, less RAM, no lag.
> L78: Spawn two or more agents in the same repo, and they will automatically be managed by the server to allow native col
> L111: Supports a wide range of providers, including Claude OAuth and OpenAI Codex OAuth.

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `04dbdf9fb063` · [字段定义](../../DATASET.md)*
