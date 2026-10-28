# p10node/docflare-ai

⭐ 42 · TypeScript · MIT · 推送 2026-10-08 · [GitHub](https://github.com/p10node/docflare-ai) · 个人维护

**文档站一键嵌入的开源 AI 问答与站内搜索挂件**

面向文档站所有者的自托管 RAG 聊天挂件：在页面加一个 <script> 标签即获得带来源引用的流式问答。100% 运行在 Cloudflare 免费层上（Workers + Workers AI + Vectorize + D1），无需 OpenAI key 或外部向量库。机制上：sitemap 爬取与 boilerplate 剥离、按标题的 350 token 分块、两阶段检索（向量召回 20 条后经 bge-reranker-base 重排）、Llama 3.1-8b 生成 SSE 流式回答并记录于 D1。内置 /admin 管理页，支持多站点/多租户，需自行部署到 Cloudflare。

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

- 一个 <script> 标签嵌入，Shadow DOM 挂件 < 10 KB 零依赖
- 两阶段检索：向量召回 + bge-reranker-base 交叉编码器重排
- 100% Cloudflare 原生（Workers AI/Vectorize/D1），面向免费层设计
- 内置 /admin 管理 UI 与多站点/多租户隔离

## 适用场景

- 给我的开源项目文档站加一个带来源的 AI 问答挂件
- 不用付费 SaaS，在 Cloudflare 免费层自托管 docs 问答
- 通过 D1 中的提问记录发现文档覆盖缺口

## 场景标签

`聊天机器人` `RAG` `文档问答` · 领域:对话与助手

## 证据(README 行号)

> L5: Drop one `<script>` tag on your docs site and get a streaming RAG chatbot that answers from *your* content, with sou
> L28: |Embeddings + LLM|**Workers AI** (`bge-small-en-v1.5`, `bge-reranker-base`, `llama-3.1-8b-instruct-fp8`)|10k neuron

## 星数曲线

```mermaid
xychart-beta
    title "p10node/docflare-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-28 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `f72e1db45ab3` · [字段定义](../../DATASET.md)*
