# NocturnLabs/opencode-personal-knowledge

⭐ 16 · TypeScript · 推送 2025-12-15 · [GitHub](https://github.com/NocturnLabs/opencode-personal-knowledge) · [官网](https://nocturnlabs.github.io/docs/) · 组织维护

**为 Opencode 提供个人知识与会话记忆的本地 MCP 服务器**

面向 Opencode 生态的 Model Context Protocol 服务器：内置 LanceDB 向量库与 SQLite，提供知识条目的存储/语义检索/标签管理工具集，以及跨会话的日志记录与语义搜索工具。嵌入模型使用 BGE-small-en-v1.5（FastEmbed/ONNX Runtime），全部本地运行，无需外部 API key。数据默认存于 ~/.local/share/opencode-personal-knowledge/，可通过环境变量覆盖路径。以 Bun/Node.js 运行时实现，支持 Opencode 配置集成或源码方式运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 store/search/update 等 8 个知识管理 MCP 工具
- 7 个会话记忆工具：记录并语义检索整个会话
- 嵌入 100% 本地运行（BGE-small-en-v1.5 via FastEmbed），无需外部 API key
- LanceDB 嵌入式向量库 + SQLite 持久存储

## 适用场景

- 让 Opencode 编码代理记住并检索我的个人知识条目
- 记录调试会话并事后语义搜索历史对话
- 用标签组织知识并通过语义或关键词查找

## 场景标签

`知识库管理` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3:  A personal knowledge MCP server with vector database for the Opencode ecosystem
> L9: Store and retrieve knowledge using semantic search, powered by local embeddings. No external API keys required.

## 星数曲线

```mermaid
xychart-beta
    title "NocturnLabs/opencode-personal-knowledge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `c6eecd37a921` · [字段定义](../../DATASET.md)*
