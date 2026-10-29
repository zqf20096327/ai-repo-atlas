# NovasPlace/CSM

⭐ 46 · TypeScript · MIT · 推送 2026-10-26 · [GitHub](https://github.com/NovasPlace/CSM) · 组织维护

**AI 编码代理的跨会话记忆与连续性运行时（AgentBook 事件账本）**

为 AI 编码代理提供持久记忆与操作连续性基础设施：以 append-only 事件账本（AgentBook）记录工具与会话事件，生成有界摘要与当前状态投影，通过 turn-1 前页注入实现确定性冷启动恢复。提供混合检索（向量/全文/实体/关系）、上下文压缩与缓存、经验包与信念知识层、溯源与治理报告。存储支持 PostgreSQL（完整功能）与 SQLite（本地核心模式），以 OpenCode 插件、Claude Code 原生插件与 Codex MCP 命令接入各代理宿主。文件权威仍归 Git，不替代 Git。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AgentBook append-only 事件账本 + 滚动摘要 + turn-1 前页注入冷启动
- 混合检索：向量、全文、实体、标签、重要性与关系遍历，含回退路径
- 上下文控制：压缩、token 压力分析、持久上下文缓存、检查点
- PostgreSQL 完整路径与 SQLite 零服务本地核心两种模式

## 适用场景

- 让编码代理在跨会话、跨项目、换模型后恢复工作状态
- 保留决策、教训与失败证据，避免新会话重复犯错
- 治理与审计代理记忆：溯源、去重、召回质量报告

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L26: AgentBook combines the workspace truth already held by Git with CSM's append-only events,
> L62: |Host|OpenCode plugin, a native Claude Code plugin (hooks + MCP tools + slash commands + subagents + skills), and a
> L103: AgentBook records meaningful tool and session events in an append-only journal, summarizes them in bounded ranges,

## 星数曲线

```mermaid
xychart-beta
    title "NovasPlace/CSM 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-29"]
    y-axis "stars" 44 --> 47
    line [45, 46, 46]
```

2026-10-18 45 → 2026-10-29 46（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `01a6bf52e57d` · [字段定义](../../DATASET.md)*
