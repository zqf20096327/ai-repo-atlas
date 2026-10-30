# open-metadata/ai-sdk

⭐ 15 · Python · NOASSERTION · 推送 2026-10-29 · [GitHub](https://github.com/open-metadata/ai-sdk) · 组织维护

**给数据团队的 SDK：把 OpenMetadata/Collate 元数据接入 AI agent**

OpenMetadata 官方多语言 SDK（Python/TypeScript/Java/CLI/n8n 节点），通过两条路径访问 OpenMetadata 与 Collate：一是 MCP 工具，向任意 LLM 暴露语义搜索、血缘遍历、术语与分类读写及元数据变更能力，并提供 LangChain 与 OpenAI function calling 适配器；二是调用 Collate AI Studio 中预构建 agent（支持流式、多轮、异步）。另含 Context Memories 混合检索与 evals 命令，以 CSV/JSON 定义用例并判定 AI Chat 回答与 SQL 的正确性。需连接 OpenMetadata/Collate 服务使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MCP 工具暴露语义搜索、血缘遍历、术语/PII 分类读写
- LangChain 与 OpenAI function calling 框架适配器（含 include/exclude 过滤）
- Context Memories 混合检索（向量相似度+关键词排序）
- evals 用例定义与 exact/LLM 两种判定模式，可对比上下文变更前后结果

## 适用场景

- 用任意 LLM 构建基于数据目录语义的检索与治理应用
- 调用 Collate AI Studio 预构建 agent 做数据问答
- 在 CI 中评测 AI Chat 回答与 SQL 的正确性并追踪上下文变更影响

## 场景标签

`Agent 框架` `语义搜索` `模型评测` · 领域:Agent 开发

## 证据(README 行号)

> L3: Bring AI to your metadata. The OpenMetadata AI SDK gives you programmatic access OpenMetadata and Collate through tw
> L17: OpenMetadata exposes an MCP server at `/mcp` that turns your data management platform into a set of tools any LLM c
> L23: - **Framework adapters** — First-class integration with LangChain and OpenAI function calling. Convert MCP tools wi

## 星数曲线

```mermaid
xychart-beta
    title "open-metadata/ai-sdk 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `2b7de5c20d64` · [字段定义](../../DATASET.md)*
