# hoangsonww/FRED-Data-Analysis

⭐ 18 · TypeScript · MIT · 推送 2026-09-27 · [GitHub](https://github.com/hoangsonww/FRED-Data-Analysis) · [官网](https://fred-data-analysis.vercel.app) · 个人维护

**美国经济数据的全栈分析应用：RAG 聊天问答与回归分析**

TypeScript/Express/React 全栈应用：从 FRED API 拉取美国宏观经济数据，清洗后存入 MongoDB，用 Google 文本嵌入模型向量化并写入 Pinecone，提供基于 RAG 的聊天机器人，可用 Gemini、OpenAI、Claude、Azure OpenAI 回答数据问题；另含线性/多项式/对数等回归分析与图表报告。运行需 Node.js v18+、MongoDB、Pinecone 及多项 API key，本地按分析→向量化→聊天→API→前端的顺序执行 npm 脚本，也提供 Vercel 部署。作者声明为作品集性质的 mockup 项目。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- FRED 数据 ETL + MongoDB 存储 + Pinecone 向量化
- RAG 聊天机器人，支持 Gemini/OpenAI/Claude/Azure 多模型并对比
- 线性、多项式（1-10 阶）、对数、日百分比变化回归分析
- Express API + Swagger 文档 + React/Recharts 可视化前端

## 适用场景

- 用自然语言查询美国宏观经济指标数据
- 对 CPI、失业率、GDP 等序列做回归分析并查看图表
- 学习 RAG 数据管道（FRED→MongoDB→Pinecone→聊天）的参考实现

## 场景标签

`数据分析` `聊天机器人` `RAG` · 领域:效率与自动化

## 证据(README 行号)

> L5: This repository contains a mockup full-stack application that fetches a wide range of U.S. economic data from the FR
> L12:  - It also vectorizes the data using Pinecone and provides a chatbot with RAG (retrieval-augmented generation) capa
> L77: 3. The chatbot queries the vectorized data from Pinecone and uses RAG to provide answers. This allows the chatbot t

## 星数曲线

```mermaid
xychart-beta
    title "hoangsonww/FRED-Data-Analysis 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `ce5f99b54927` · [字段定义](../../DATASET.md)*
