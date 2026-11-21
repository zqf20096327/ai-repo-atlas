# SeyhmusKaya/agent-symphony

⭐ 10 · TypeScript · MIT · 推送 2026-06-03 · [GitHub](https://github.com/SeyhmusKaya/agent-symphony) · 个人维护

**基于 Claude Agent SDK 的桌面多 Agent 分层编排器**

基于官方 Claude Agent SDK（进程内运行）构建的 Tauri+SvelteKit 桌面应用，将 Agent 组织为 Architect→Project Chief→Specialist/Worker 的层级结构，含 11 个内置 Advisor。提供按 Agent 的技能文件与自动分配、并行任务分发、跨 Agent 通信、CodeGraph 代码检索（tree-sitter+SQLite FTS+embeddings）、会话内上下文压缩、逐 token/成本跟踪、SSH 部署与预算控制。支持 Claude Pro/Max 订阅登录或 Anthropic/DeepSeek API key 三种认证路径。当前仅支持 Windows，需 Node.js 20+，桌面构建需 Rust 工具链。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 五级角色层级（Architect/Chief/Specialist/Advisor/Worker）与跨 Agent 消息机制
- 双模型提供方：Claude 与 DeepSeek（经 Anthropic 兼容端点），可按 Agent 切换
- CodeGraph 语义代码检索（tree-sitter 7 种语言 + SQLite FTS + embeddings）
- 逐会话、逐 Agent 的 token 与 USD 成本跟踪及预算自动降级

## 适用场景

- 在一个桌面面板里同时推进多个项目的多 Agent 协作开发
- 用 Claude Pro/Max 订阅而非按 token 计费运行 Agent 团队
- 配置 DeepSeek key 作为更低成本的运行路径
- 通过预算上限自动切换到更便宜的模型控制开销

## 场景标签

`多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L41: **Architect — Agent Symphony** is a desktop application that turns the Claude Agent SDK into a **hierarchical organ
> L49: If you've used **Claude Code**, **CrewAI**, **AutoGen**, or **LangGraph**: those are frameworks and CLIs you *scrip
> L95: ### 🔀 Multi-provider model routing (Claude + DeepSeek)

## 星数曲线

```mermaid
xychart-beta
    title "SeyhmusKaya/agent-symphony 星数(近 2 点)"
    x-axis ["2026-11-13", "2026-11-21"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-11-13 10 → 2026-11-21 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `5e8d1bb681bd` · [字段定义](../../DATASET.md)*
