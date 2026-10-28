# AlekseiUL/openclaw-memory-kit

⭐ 34 · Shell · MIT · 推送 2026-10-26 · [GitHub](https://github.com/AlekseiUL/openclaw-memory-kit) · [官网](https://t.me/Sprut_AI) · 个人维护

**OpenClaw AI agent 的记忆与上下文持久化套件**

为 OpenClaw AI agent 提供文件式记忆与上下文持久化：包含 BOOTSTRAP.md、MEMORY.md、handoff.md 等模板，memory/ 目录结构（core/decisions/projects/archive），auto-handoff、auto-diary、consolidator、night-cleanup 四个 cron，以及健康检查、一致性检查、归档脚本。基础功能零依赖可用，向量记忆检索（70% 向量+30% BM25 混合）需 OpenAI API key 做 embeddings。提供 install.sh 一键安装，install.sh 不修改 openclaw.json。面向个人 OpenClaw 操作者与 agent 构建者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 模板+cron+脚本+配置四类组件的文件式记忆体系
- 基础功能零依赖、无需 API key 即可用
- 混合向量检索（70% 向量 + 30% BM25）为可选增强
- compaction 前通过 memoryFlush 保存上下文

## 适用场景

- OpenClaw agent 重启或 compaction 后恢复会话上下文
- 让 agent 通过 handoff 与每日笔记持续积累记忆
- 为 agent 记忆体系做归档、清理与一致性检查

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3: Complete memory and context persistence system for OpenClaw AI agents.
> L23: An agent without memory is like a person with amnesia. Every session starts from scratch. This kit solves the probl
> L29: - personal OpenClaw operators who lose context after compaction or restarts;

## 星数曲线

```mermaid
xychart-beta
    title "AlekseiUL/openclaw-memory-kit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-28 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `c453128e2509` · [字段定义](../../DATASET.md)*
