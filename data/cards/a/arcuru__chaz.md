# arcuru/chaz

⭐ 68 · Rust · AGPL-3.0 · 推送 2026-10-30 · [GitHub](https://github.com/arcuru/chaz) · [官网](https://chaz.is) · 个人维护

**实验性 AI agent 框架，含 Matrix 桥接与多 agent 编排**

构建于 eidetica 之上的实验性 AI agent 框架：提供 ReAct 工具调用循环（内置 12 个工具）、多 agent 编排（Agent 与一次性 Worker 模板、深度限制）、扩展框架与事件日志审计。主要桥接为 Matrix bot，可连接任意 OpenAI 兼容的 LLM 提供方，另含本地 TUI；会话状态经 eidetica SQLite 持久化并可跨实例同步。README 明确标注实验性，API 与数据格式可能随时变更，不建议用于重要数据。安装途径包括 Nix、Docker 与 cargo 源码编译。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- ReAct 工具调用循环，内置 12 个工具
- Matrix 桥接 + 本地 TUI 双入口，可连接任意 OpenAI 兼容提供方
- 基于 eidetica SQLite 的持久会话与跨实例会话同步（ticket 机制）
- 安全机制：泄漏检测、网络控制、shell 沙箱、工具审批门

## 适用场景

- 通过 Matrix 聊天室与 LLM agent 交互
- 在终端 TUI 中测试与调试多 agent 工作流
- 多台机器协作驱动同一会话（会话同步）

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L3: Chaz is an experimental AI agent framework built on eidetica. It features a ReAct tool-calling loop, multi-agent orc
> L15: - **ReAct tool-calling loop** — agents reason, act, and observe in a loop with 9 built-in tools

## 星数曲线

```mermaid
xychart-beta
    title "arcuru/chaz 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 67 --> 69
    line [68, 68]
```

2026-10-18 68 → 2026-10-31 68（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `1bb3199192d7` · [字段定义](../../DATASET.md)*
