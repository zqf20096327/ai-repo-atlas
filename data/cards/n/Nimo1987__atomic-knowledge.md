# Nimo1987/atomic-knowledge

⭐ 42 · Python · MIT · 推送 2026-04-21 · [GitHub](https://github.com/Nimo1987/atomic-knowledge) · 个人维护 · 中文 README

**给已有 agent 的 Markdown 工作记忆协议：跨会话维护知识库**

面向已有 agent 用户的平台无关协议与工具包：在原始资料与回答之间插入一层由 agent 持续维护的 markdown wiki，把来源、讨论中形成的结论、比较与决策理由沉淀为可复用的工作记忆，解决会话重置导致研究上下文丢失的问题。知识模型含 raw/sources、wiki/concepts、projects、procedures、insights 与 meta/candidates 候选队列；提供 init 脚本、示例知识库、evals、可选运行时与 MCP 适配器。自述 v0.2.0 早期发布，非记忆插件、向量库或通用 RAG，需 agent 能读本地文件并执行 shell 命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- markdown wiki 工作记忆层，ingest/query/writeback/maintenance 四类核心工作流
- meta/candidates 候选队列经 open→promoted|merged|dropped 生命周期解决
- 跨 agent 平台：生成 AGENT.md 装入持久指令面，另提供 MCP 适配器
- 附带示例知识库、eval 评测场景与 lint 健康检查

## 适用场景

- 让日常使用的 agent 记住跨会话的研究结论与项目上下文
- 持续积累工具比较、方法框架与决策记录，避免重复调研
- 为不同 agent 平台接入同一份本地 markdown 知识库

## 场景标签

`Agent 记忆` `科研工具` · 领域:Agent 开发

## 证据(README 行号)

> L5: Atomic Knowledge is a platform-neutral protocol for building agent-maintained work memory in markdown.
> L91: - includes a minimal MCP adapter for tool-calling agent integrations

## 星数曲线

```mermaid
xychart-beta
    title "Nimo1987/atomic-knowledge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-26 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `78da8748773a` · [字段定义](../../DATASET.md)*
