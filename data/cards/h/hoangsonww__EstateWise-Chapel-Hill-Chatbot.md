# hoangsonww/EstateWise-Chapel-Hill-Chatbot

⭐ 41 · TypeScript · MIT · 推送 2026-09-27 · [GitHub](https://github.com/hoangsonww/EstateWise-Chapel-Hill-Chatbot) · [官网](https://estatewise.vercel.app) · 个人维护

**北卡教堂山地区房产 AI 聊天助手与数据分析全栈应用**

面向 Chapel Hill 及周边城市购房者的全栈 monorepo AI 房产助手：通过聊天界面提供个性化房源推荐，核心机制包括混合 RAG（Pinecone kNN 向量检索 + Neo4j 图谱增强）、Mixture-of-Experts 多专家路由、CoT 推理、k-Means 聚类与 kNN 相似检索，用户点赞/点踩反馈调整专家权重。另含 JWT 与 Passkeys 认证、会话分支编辑、地图页、交易分析器（Deal Analyzer）与社区论坛。部署于 Vercel，可直接在线使用或本地运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 混合 RAG：Pinecone 向量检索 + Neo4j 图增强并融合结果
- MoE 专家路由（数据分析/生活方式/财务/社区/聚类 5 类专家）+ 用户反馈调整权重
- AI 生成 Chart.js 实时图表嵌入聊天消息
- Deal Analyzer 评估房产交易质量（评分卡+敏感性分析）

## 适用场景

- 通过对话获取符合偏好的房源推荐并查看推荐理由
- 分析某房产是否值得购买（评分、月度拆解、风险与行动计划）
- 在地图上浏览房源并查看社区统计数据
- 管理多轮会话并编辑历史消息生成分支回答

## 场景标签

`聊天机器人` `RAG` `数据分析` `推荐系统` · 领域:效率与自动化

## 证据(README 行号)

> L3: **EstateWise** is a **full‑stack, monorepo AI/ML** **chatbot & data analytics project** built for real estates in _C
> L107: - **Hybrid RAG (Vector + Graph):** Uses Pinecone for kNN‑based vector retrieval and Neo4j for graph enrichment bef
> L145: - **Intelligent Property Recommendations:** Get tailored property suggestions powered by AI and Retrieval‑Augmente

## 星数曲线

```mermaid
xychart-beta
    title "hoangsonww/EstateWise-Chapel-Hill-Chatbot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-31 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `2232d8642043` · [字段定义](../../DATASET.md)*
