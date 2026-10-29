# julienlucas/agentic-rag-with-tools

⭐ 19 · Python · NOASSERTION · 推送 2026-10-12 · [GitHub](https://github.com/julienlucas/agentic-rag-with-tools) · [官网](https://agentic-rag-search.vercel.app) · 个人维护

**多智能体 RAG 系统：带文档导航工具的金融问答，SaaS 化交付**

面向财务报告问答的多智能体 RAG 系统：混合检索（BM25+向量存 Qdrant、Cohere 重排、按文档路由），生成模型配备 search/grep/read_page/open_doc/navigate 五个文件系统式工具，可检索整页 OCR 内容；含相关性校验 Agent 与受约束生成（逐条引用，无依据则拒答）。在 FinanceBench 84 份 SEC 报告、12 000 页上测得 88.1% 正确率。模型走 Amazon Bedrock 或 Anthropic/Cohere 直连 API，OCR 用 Mistral。附带 Django 前后端的自助服务产品代码：账户、多格式文档摄取、按积分计费（Stripe）、Railway Docker 部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 生成模型配备 search/grep/read_page/open_doc/navigate 五个文档导航工具
- FinanceBench 上 12 000 页单索引，88.1% 正确率，逐题结果存于 LangSmith 实验
- 受约束生成：每个论断带 [n] 引用，无依据时拒答
- 附带 SaaS 产品代码：账户/工作区隔离、积分计费、Railway Docker 部署

## 适用场景

- 对长篇财务报告（10-K/10-Q）做有引用依据的问答
- 搭建多文档索引、按文档路由的检索问答服务
- 以 SaaS 形式向用户提供按量计费的文档问答

## 场景标签

`RAG` `文档问答` `多智能体` `金融量化` · 领域:Agent 开发

## 证据(README 行号)

> L6: Ce système RAG combine un récupérateur hybride (BM25 + embeddings dans Qdrant, reranking Cohere), un routage
> L29: ### 2. **Agent de Recherche et de réponse, avec outils**
> L130: Le RAG est servi en libre-service, payé au crédit (plan : `docs/plan-produit.md`, contrat d'API :

## 星数曲线

```mermaid
xychart-beta
    title "julienlucas/agentic-rag-with-tools 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `78ed93b113b8` · [字段定义](../../DATASET.md)*
