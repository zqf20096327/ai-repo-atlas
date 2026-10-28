# neo4j-labs/meta-knowledge-graph

⭐ 34 · Python · 推送 2026-09-07 · [GitHub](https://github.com/neo4j-labs/meta-knowledge-graph) · 组织维护

**给 AI agent 的自学习图记忆层，基于 Neo4j**

面向 AI agent 的记忆层，由 MCP 服务器与生命周期钩子两部分组成：钩子记录每次会话事件并在提交时注入项目上下文，Stop 时由 LLM 提取循环从会话中蒸馏 `:Learning` 候选与逐工作窗口的 `:Observation` 时间线；MCP 服务器将项目记忆、图、系统提示词及可选数据目录/仓库以工具形式提供给 agent。本体 harness 无关，随附 Claude Code 与 Codex 的现成接线，其余 MCP-capable harness 可复用同一脚本。系统提示词冻结，由 `:UserProfile` 节点承载用户级适应；宿主前置仅 uv 与可达的 Neo4j 实例。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MCP 服务器 + 生命周期钩子组成捕获-召回闭环，harness 无关
- LLM 提取循环蒸馏 project/user 双作用域的 `:Learning` 与情节记忆时间线
- 随附 Claude Code 与 Codex 插件包及 B2B 销售助手端到端示例
- 所有会话/学习/观察按 user id 打标，各用户独立 `:UserProfile`

## 适用场景

- 让 Claude Code/Codex 等编程 agent 跨会话记住项目决策与用户偏好
- 为自建 MCP harness 接入图结构项目记忆与自动学习提取
- 搭建带记忆的 B2B 销售/客户成功助手演示

## 场景标签

`Agent 记忆` `知识图谱` · 领域:Agent 开发

## 证据(README 行号)

> L3: The **Meta Knowledge Graph** (MKG) is a self-improving, graph-structured memory
> L18: - **Lifecycle hooks** — plain Python scripts that log every session event,
> L55: - **Other harnesses** — any MCP-capable harness with lifecycle hooks can drive the

## 星数曲线

```mermaid
xychart-beta
    title "neo4j-labs/meta-knowledge-graph 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 32 --> 35
    line [33, 34]
```

2026-10-18 33 → 2026-10-28 34（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `644055c85a93` · [字段定义](../../DATASET.md)*
