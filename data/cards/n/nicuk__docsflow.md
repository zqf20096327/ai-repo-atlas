# nicuk/docsflow

⭐ 19 · TypeScript · MIT · 推送 2026-09-30 · [GitHub](https://github.com/nicuk/docsflow) · [官网](https://docsflow.app/?utm_source=github&utm_medium=social&utm_campaign=readme_link) · 个人维护

**多租户 RAG 文档问答平台：每团队独立工作区与带引用的回答**

基于 Next.js 15 + Supabase + Pinecone 的多租户 RAG 应用：每个团队获得独立子域名工作区，上传 PDF/Word/Excel/PPT/图片等文档后用自然语言提问，回答附带置信度评分与可点击的文档来源引用。机制上采用四层租户隔离（Supabase RLS、Pinecone namespace、Clerk 租户令牌、边缘路由）、向量+BM25 混合检索（RRF 融合）、分层检索与阈值弃答、四级 LLM 故障切换链（Llama 3.3 → GPT-4o-mini → Mixtral → Gemini），并集成 Stripe 订阅计费与 Vercel 部署。提供 Live Demo，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四层多租户隔离（数据库 RLS / 向量 namespace / 会话令牌 / 边缘路由）
- 向量相似度 + BM25 混合检索并以 RRF 融合
- 回答附带置信度评分、阈值弃答与逐条来源引用
- 四级 LLM 故障切换链（Llama 3.3 → GPT-4o-mini → Mixtral → Gemini）

## 适用场景

- 团队搭建私有的带来源引用的文档问答工作区
- 按部门/客户隔离文档并控制 5 级访问权限
- 作为多租户 RAG SaaS 的参考架构进行二次开发

## 场景标签

`文档问答` `RAG` · 领域:知识与检索

## 证据(README 行号)

> L18: 3. **Ask questions in plain English** — The AI searches across all your documents and returns answers with exact so
> L21: Every answer includes a confidence score and clickable source links. No hallucinated claims — if the AI can't find 

## 星数曲线

```mermaid
xychart-beta
    title "nicuk/docsflow 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `6bc0f16826cf` · [字段定义](../../DATASET.md)*
