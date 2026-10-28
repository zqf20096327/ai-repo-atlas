# qdrant/webinar-crewai-qdrant-obsidian

⭐ 29 · Python · Apache-2.0 · 推送 2026-08-07 · [GitHub](https://github.com/qdrant/webinar-crewai-qdrant-obsidian) · 组织维护

**基于 CrewAI 的智能体：用 Obsidian 知识库自动起草 Gmail 回信**

Qdrant 团队网络研讨会配套代码，实现 agentic RAG 系统：文件系统监听器监控 Obsidian Vault 变化并更新 Qdrant 索引，CrewAI agent 监控 Gmail 收件箱并基于知识库内容起草回复。代理行为由 CrewAI 实现，Qdrant 作为记忆层，任务分别使用 Gemini 与 Claude 的 API。运行需 Qdrant 实例（本地 Docker 或 Qdrant Cloud）、Google Cloud 凭据与两家模型 API key，Python 3.10+，用 Poetry 管理依赖，无需 GPU。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Obsidian Vault 文件监听并增量更新 Qdrant 索引
- CrewAI agent 监控 Gmail 收件箱并起草回复
- Qdrant 作为记忆层，支持本地 Docker 或 Qdrant Cloud
- 代码中可替换 Gemini/Claude 为其他模型

## 适用场景

- 把自己的笔记库变成邮件自动起草助手
- 学习 CrewAI + Qdrant 构建 agentic RAG 的参考实现
- 基于个人知识库自动处理 Gmail 收件箱

## 场景标签

`RAG` `AI 写作` · 领域:内容生成

## 证据(README 行号)

> L4: Qdrant](https://www.youtube.com/watch?v=soGB3UowTZ0)". It implements an agentic RAG system that uses your existing
> L9: The project is built using Python and integrates with external services through their APIs. **The agentic behaviors 

## 星数曲线

```mermaid
xychart-beta
    title "qdrant/webinar-crewai-qdrant-obsidian 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-28 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `711265b4dbac` · [字段定义](../../DATASET.md)*
