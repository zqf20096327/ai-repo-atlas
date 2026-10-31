# jdevalk/ask-endpoint

⭐ 13 · JavaScript · MIT · 推送 2026-03-26 · [GitHub](https://github.com/jdevalk/ask-endpoint) · [官网](https://joost.blog/ask-joost/) · 个人维护

**给 Cloudflare Pages 静态站加 AI 问答端点的工具**

面向部署在 Cloudflare Pages 上的 markdown 静态站点，提供 /ask 端点实现问答功能：混合搜索（关键词打分加语义嵌入）、经 Workers AI（Llama 3.3 70B）生成自然语言回答并支持 SSE 流式输出、来源过滤、多轮对话上下文与提示缓存。构建时用 node 脚本生成索引，无数据库与向量存储，嵌入可选，缺失时退化为纯关键词搜索。兼容 NLWeb 协议，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 关键词+语义嵌入的混合搜索，索引构建时嵌入可选
- LLM 生成回答，支持 SSE 流式输出与多轮上下文
- 无数据库、无向量存储，运行于 Cloudflare 免费层
- 兼容 NLWeb 协议，可供支持该协议的 AI agent 调用

## 适用场景

- 给自己的静态博客/文档站添加自然语言问答功能
- 让 NLWeb 兼容的 AI agent 直接查询站点内容
- 以低成本在 Cloudflare 上运行带来源的站点问答

## 场景标签

`RAG` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L6: An AI-powered `/ask` endpoint for static sites on Cloudflare Pages. Adds Q&A to any markdown-based site using Cloudf
> L11: - **LLM answers**: generates natural language answers grounded in your content, with streaming support

## 星数曲线

```mermaid
xychart-beta
    title "jdevalk/ask-endpoint 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `496ff7a0d549` · [字段定义](../../DATASET.md)*
