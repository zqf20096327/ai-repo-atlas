# major7apps/pensyve

⭐ 97 · Rust · NOASSERTION · 推送 2026-10-29 · [GitHub](https://github.com/major7apps/pensyve) · 组织维护

**AI agent 的持久化记忆运行时：跨会话存取事实与对话**

开源的 agent 记忆运行时，存储事实、对话（情景）、观察与动作结果四类记录，供后续会话检索。Rust 引擎用 SQLite 做本地存储并在本地运行 embedding 模型做语义搜索，无需账号或 API key；可通过 Python SDK、MCP server（供 Claude Code/Cursor/Codex 使用）、CLI、REST 网关访问，TypeScript/Go SDK 经自托管网关连接。注意：Pensyve Cloud 已于 2026-10-01 关闭，项目处于维护模式，仅提供安全修复与依赖更新，不再新增功能。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四类记忆记录：事实/对话/动作结果/观察
- 本地 SQLite 存储 + 本地 embedding 模型语义搜索，无需 API key
- 多接入方式：Python SDK、MCP server（stdio/HTTP）、CLI、REST 网关
- consolidation 机制提升重复事实并更新记忆保留

## 适用场景

- 给 Python agent 增加跨会话持久记忆
- 让 Claude Code、Cursor 或 Codex 通过 MCP 读写记忆
- 用 TypeScript/Go SDK 共享自托管的团队记忆库

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L10: Pensyve is an open-source runtime for persistent AI agent memory. It stores facts,
> L12: in later sessions. You can use it through Python, a Model Context Protocol
> L16: locally to search by meaning. TypeScript and Go clients connect to a gateway

## 星数曲线

```mermaid
xychart-beta
    title "major7apps/pensyve 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 96 --> 98
    line [97, 97]
```

2026-10-18 97 → 2026-10-30 97（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `6ef96734deca` · [字段定义](../../DATASET.md)*
