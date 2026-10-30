# phenomenoner/openclaw-mem

⭐ 28 · Python · MIT · 推送 2026-07-26 · [GitHub](https://github.com/phenomenoner/openclaw-mem) · [官网](https://phenomenoner.github.io/openclaw-mem/) · 个人维护 · 中文 README

**面向 AI agent 的可审计记忆治理层：引用、信任策略、回滚**

为 AI agent 提供本地优先的记忆治理层：以 SQLite + JSONL 存储 agent 活动，组装带边界的 ContextPack——每条纳入的记忆带引用，每条排除的记忆带书面原因，每次记忆变更附带回滚凭证；信任策略将隔离/不可信记录排除在上下文之外。以 sidecar 方式服务 OpenClaw，也支持 Claude、Codex、Gemini 等通用 agent 框架（MCP、Channel A、hooks 集成）。默认无需外部向量数据库，混合检索（FTS + 向量）本地运行。单一维护者，v2.0.0，官方自述为年轻项目，高级功能标注为 labs。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 每条纳入记忆带引用、每条排除记忆带书面原因的 ContextPack
- 信任策略隔离不可信记录，防御记忆投毒（含可复现合成证明脚本）
- 记忆变更走 plan → checkpoint → apply → receipt → rollback 流程
- SQLite + JSONL 本地存储，默认无需外部向量数据库与云服务

## 适用场景

- 为长期运行的 agent 把控进入上下文窗口的记忆并留存审计证据
- 防止工具输出或网页文本等不可信内容经记忆检索注入提示词
- 对错误记忆变更做带凭证的回滚
- 在 OpenClaw / Claude / Codex / Gemini 等 harness 中接入治理型持久记忆

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L15: Most AI agent memory systems compete on **recall** — remember more, retrieve better. `openclaw-mem` competes on a d
> L17: Built sidecar-first for OpenClaw, usable with Claude, Codex, Gemini, and generic agent harnesses.

## 星数曲线

```mermaid
xychart-beta
    title "phenomenoner/openclaw-mem 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-30 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `a6354704d6f4` · [字段定义](../../DATASET.md)*
