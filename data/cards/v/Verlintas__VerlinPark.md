# Verlintas/VerlinPark

⭐ 3 · Rust · GPL-3.0 · 推送 2026-11-27 · [GitHub](https://github.com/Verlintas/VerlinPark) · 个人维护

**给 agent 团队用的原生 macOS 多智能体开发环境**

以 Rust 守护进程加 SwiftUI 原生外壳的形式，在隔离的 Git worktree 中运行 Leader→Manager→Worker→Labour 四层编码 agent 团队：计划经校验后按依赖批次派发，合并需 Verifier 判定并通过持久化合并队列。全程会话以 append-only SQLite 事件日志记录计划、消息、LLM 请求、工具调用与预算状态，可回放与导出。支持 MCP 工具、ACP 外部 agent、SKILL.md 技能包、token/USD 预算池与缓存优先提示。仅面向 macOS；冲突自动解决、部分归档格式等明确未实现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 四层 agent 团队结构，每个任务独立 Git worktree 与权限策略
- append-only 事件日志记录全部计划、消息、工具调用与成本，支持 vp replay/export
- 支持 MCP（stdio/HTTP/SSE）与外部 ACP agent，SKILL.md 技能包导入
- 会话与项目级 token/USD/时钟预算池，原子容量预留

## 适用场景

- 让多个编码 agent 并行开发且互不覆盖彼此的检出目录
- 需要完整审计每个 agent 决策与 token 花费的团队
- 在本地模型（LM Studio/Ollama/llama.cpp）上运行 agent 团队

## 场景标签

`多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L3: **A native macOS agentic development environment for agent teams.**
> L21: It is not a chat window bolted onto an editor. It is a native control plane for planning, running, reviewing, and l
> L61: - Cloud APIs first; any OpenAI-compatible endpoint (LM Studio, Ollama, llama.cpp) works as a local provider.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `65c164687b94` · [字段定义](../../DATASET.md)*
