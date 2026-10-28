# AOSSIE-Org/Perspective

⭐ 55 · TypeScript · MIT · 推送 2026-10-27 · [GitHub](https://github.com/AOSSIE-Org/Perspective) · [官网](https://perspective-aossie.vercel.app/) · 组织维护

**分析新闻/社媒内容并生成可信反向叙事的 Web 应用**

面向阅读新闻、博客与社交媒体内容的用户：分析当前内容的主导叙事与偏见，从可信来源检索并生成反向叙事与论证分析，实时呈现以打破信息茧房。架构为 Next.js 前端 + FastAPI 后端，用 LangChain/Langgraph 编排推理链，LLM 服务生成反方论证（如 Groq API），向量库（Pinecone）存储语义嵌入，Google 自定义搜索拉取来源。需自行部署前后端并配置多项 API key，未提供打包安装或托管版本说明。

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

- 识别内容主导叙事与偏见并生成反向论证
- chain-of-thought 提示与事实关联分析
- 从可信来源持续拉取数据更新事实
- LangChain/Langgraph 编排推理链与工作流

## 适用场景

- 阅读新闻时查看对立视角的论证
- 对比事实与反事实以减少单一叙事偏见
- 在讨论前获取平衡、多维度的信息

## 场景标签

 · 领域:媒体/信息消费

## 证据(README 行号)

> L8: Perspective-AI is designed to combat the echo chambers created by personalized content algorithms. It actively curat
> L24: - **LLM Service**: Leverages large language models (e.g., OpenAI, custom models) to generate detailed counterargume
> L50: - **What It Does**: Instantly displays counterarguments to the main narrative.

## 星数曲线

```mermaid
xychart-beta
    title "AOSSIE-Org/Perspective 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-28"]
    y-axis "stars" 53 --> 56
    line [54, 55, 55]
```

2026-10-18 54 → 2026-10-28 55（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `27845d160939` · [字段定义](../../DATASET.md)*
