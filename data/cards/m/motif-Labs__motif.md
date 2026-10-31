# motif-Labs/motif

⭐ 21 · TypeScript · Apache-2.0 · 推送 2026-10-04 · [GitHub](https://github.com/motif-Labs/motif) · [官网](https://www.getmotif.dev/) · 组织维护

**自托管的 AI agent 经验图谱：会话记忆、人工审核与评测数据集**

面向使用 Claude Code、Codex、Cursor 等 coding agent 的开发者与团队：本地守护进程采集多工具会话，汇聚到自托管服务器形成经验图谱。提供 recall 全文检索式记忆召回（无需嵌入/向量库/API key）、经 MCP 向 agent 注入上下文、把会话蒸馏为带置信度的决策笔记并由人工审核（proposal/admit/reject）、从会话轨迹提取决策数据集并跑基线评测、以及 Weaver 将裁定回写为草稿 PR。记忆蒸馏为唯一调用模型的部分，可配置 claude-code/anthropic/openai/Ollama 等提供商。npm 全局安装，需 Node 22+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 采集 Claude Code/Codex/Cursor 会话到自托管服务器，经 MCP 供 agent 查询（recall/search/ask_session 等工具）
- 记忆需人工审核：提案、冲突标记、可能过期标记，裁定全程留痕不删除
- 从会话轨迹提取决策数据集（JSONL+盲测输入+清单）并评测多数基线或外部模型
- 召回基于全文检索+会话图结构，无嵌入、无向量库、无 API key

## 适用场景

- 团队成员跨工具共享 agent 会话经验，避免每次冷启动重新推导决策
- 对 agent 记忆做人工审核，裁决冲突并追踪过期知识
- 从真实会话轨迹构建带结果的决策数据集用于评测自有决策模型

## 场景标签

`Agent 记忆` `模型评测` · 领域:Agent 开发

## 证据(README 行号)

> L77: motif mcp install        # register with Claude Code, Codex and Cursor
> L160: motif mcp install
> L271: - `motif eval <directory>` evaluates a training-only majority baseline. Use

## 星数曲线

```mermaid
xychart-beta
    title "motif-Labs/motif 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-31"]
    y-axis "stars" 19 --> 22
    line [20, 21, 21]
```

2026-10-18 20 → 2026-10-31 21（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `456130782f46` · [字段定义](../../DATASET.md)*
