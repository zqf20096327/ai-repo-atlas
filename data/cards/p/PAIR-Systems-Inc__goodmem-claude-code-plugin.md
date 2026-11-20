# PAIR-Systems-Inc/goodmem-claude-code-plugin

⭐ 10 · Python · MIT · 推送 2026-11-07 · [GitHub](https://github.com/PAIR-Systems-Inc/goodmem-claude-code-plugin) · [官网](https://goodmem.ai) · 组织维护

**用自然语言操作 GoodMem 记忆基础设施的 Claude Code 插件**

该插件为 Claude Code 提供连接 GoodMem 记忆基础设施的 Skills 与 MCP server。包含两个 MCP server：goodmem 连接自建实例并暴露全部 API 工具（spaces、memories、embedders、rerankers、LLMs、users、apikeys 等），goodmem-gateway 通过浏览器登录连接 GoodMem Cloud 实例。支持从文件、base64、纯文本摄取记忆，检索时自动用实例首个 reranker 重排，并由首个 LLM 生成答案；内置模型注册表实现配置自动推断，对 SaaS 模型端点做凭据校验。需已有 GoodMem 实例及 gm_ API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 两个 MCP server：自建实例全工具与 GoodMem Cloud 网关
- 内置模型注册表自动推断 provider、endpoint、dimensions 等字段
- 检索时自动 rerank，可由实例首个 LLM 生成回答
- 含 Python 与 Java SDK 参考 Skills 及 OCR 文本提取工具

## 适用场景

- 摄取研究论文与文档后做跨知识库的检索问答
- 为 RAG 流水线配置 embedder、reranker 与 LLM
- 摄取历史工单并迭代存储新解法，沉淀支持知识库

## 场景标签

`Agent 记忆` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L3: A Claude Code plugin for GoodMem — memory infrastructure for AI agents.
> L40: Runs `npx @pairsystems/goodmem-mcp`, the GoodMem MCP server, which exposes the full GoodMem API as tools. Give it a
> L98: The `goodmem` server exposes all GoodMem API operations as tools:


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 mid · 依据 README sha `a95d691acb75` · [字段定义](../../DATASET.md)*
