# MakiDevelop/knowledge-pipeline

⭐ 16 · Python · MIT · 推送 2026-09-11 · [GitHub](https://github.com/MakiDevelop/knowledge-pipeline) · [官网](https://github.com/MakiDevelop/knowledge-pipeline) · 个人维护 · 中文 README

**为 AI 代理提供评分与路由的 6 层确定性知识管线**

纯 Python（stdlib + numpy）实现的个人知识处理管线：从 URL 摄入内容，做全文抽取与 LLM 摘要，按 8 个维度（知识密度、新颖性、证据强度等）打分合成 0-100 signal 分数，并自动路由到 write/research/validate/action/archive 五种去向；用 bge-m3 做稠密+稀疏混合向量嵌入，SQLite 存储，经 stdlib HTTP 服务提供搜索 API，可注册为 MCP 工具供 Claude/GPT 等代理查询。LLM 后端兼容任意 OpenAI 兼容 API（本地 Ollama 推荐，无需 key）。本仓库是私有系统 mk-brain 的公开摘录版，不与私有版同步更新。

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

- 8 维 LLM 评分 + signal score + 5 种自动路由
- 零框架：Python stdlib + numpy，仅两个第三方依赖
- bge-m3 稠密+稀疏混合检索，可选 bge-reranker-v2-m3 重排
- 任意 OpenAI 兼容 LLM 后端（Ollama/OpenAI/Anthropic 等），支持 MCP 工具接入

## 适用场景

- 把收藏的 URL 自动评分、归档，避免书签堆积
- 给多个 AI 代理提供共享的、已评分的持久知识层
- 以 MCP 工具或 HTTP API 形式让代理查询个人知识库

## 场景标签

`知识库管理` `语义搜索` `RAG` · 领域:知识与检索

## 证据(README 行号)

> L19: `knowledge-pipeline` is different. It's a **6-layer deterministic pipeline** that automatically:
> L26: 6. **Serves** a search API that any AI agent can query

## 星数曲线

```mermaid
xychart-beta
    title "MakiDevelop/knowledge-pipeline 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `7783f9a05684` · [字段定义](../../DATASET.md)*
