# ranfysvalle02/Interactive-RAG

⭐ 43 · JavaScript · Apache-2.0 · 推送 2025-12-19 · [GitHub](https://github.com/ranfysvalle02/Interactive-RAG) · 个人维护

**基于 MongoDB Atlas 的交互式 RAG agent，可对话式管理知识库**

用 LangChain 与 MongoDB Atlas 构建的交互式检索增强生成 agent：以统一文档模型将文本块、多模型向量嵌入与元数据存于同一 JSON 文档；通过 Firecrawl 将网站转为 Markdown 后用 RecursiveCharacterTextSplitter 分块；对话界面中可切换嵌入模型、调整 min_rel_score 与 num_sources(k) 等检索参数；agent 经工具对知识块执行更新/删除等数据库操作，并以 session 隔离不同工作区。README 以架构说明为主，未给出安装运行命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一文档模型：文本、多模型向量与元数据存于同一文档，支持同库 A/B 测试嵌入模型
- 对话界面实时切换嵌入模型与调整检索参数（min_rel_score、num_sources）
- agent 可通过工具按 chunk_id 更新/删除知识块
- session 工作区隔离各项目的知识与聊天历史

## 适用场景

- 在对话中管理并更新自己的知识库并获得有出处的回答
- 按会话隔离不同项目的知识库进行问答
- 在不迁移数据的情况下试验不同的嵌入模型

## 场景标签

`RAG` `聊天机器人` `知识库管理` · 领域:对话与助手

## 证据(README 行号)

> L5: Large Language Models (LLMs) are transforming our world, but they have a fundamental limitation: they only know what
> L88: `update_chunk(chunk_id='...', new_content='The new policy takes effect on Jan 1, 2026.')`
> L135: def search_knowledge_base(query: str, embedding_model: str, num_sources: int = 3) -> str:

## 星数曲线

```mermaid
xychart-beta
    title "ranfysvalle02/Interactive-RAG 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-25 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `6e3ae9dfc006` · [字段定义](../../DATASET.md)*
