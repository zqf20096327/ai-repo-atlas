# kbhujbal/Multi-Agent-AI-Travel-Advisor

⭐ 58 · Python · MIT · 推送 2026-04-12 · [GitHub](https://github.com/kbhujbal/Multi-Agent-AI-Travel-Advisor) · 个人维护

**多智能体 AI 旅行规划系统：生成含机票酒店活动的行程**

基于 CrewAI 的旅行规划系统，含 3 个 AI 智能体（请求解析、文化知识、行程编排）与 4 个 API 服务（航班、住宿、活动、物流）及 ChromaDB RAG 知识库。AI 仅负责分析与编排，行程数据均来自 Amadeus、Booking、Google Places 等 11 个外部 API。LLM 使用 Google Gemini（经 LiteLLM），RAG 嵌入可选 OpenAI。提供 FastAPI 后端与 React 前端，亦支持 CLI 模式运行；需配置多个第三方 API key，未配置的服务会被跳过。

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

- 3 个 CrewAI 智能体 + 4 个 API 服务 + RAG 知识库的编排流水线
- 行程数据全部来自实时 API，AI 仅做分析不做编造
- 支持 FastAPI/WebSocket 后端、React 前端与 CLI 三种运行方式
- 通过向 data/travel_knowledge/ 添加 .txt 文件扩充 RAG 知识

## 适用场景

- 输入自然语言需求生成逐日个性化旅行行程
- 查询目的地文化习俗、签证与实用信息
- 整合航班、住宿、景点与交通天气数据做行程决策

## 场景标签

`多智能体` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L3: An AI travel planning system that combines **real-time API data** with **AI-powered analysis** to create personalize
> L7: - **3 AI Agents** handle reasoning: parsing requests, cultural knowledge, and itinerary compilation
> L10: - **AI only does analysis** — all travel data comes from real APIs, not hallucinated by the LLM

## 星数曲线

```mermaid
xychart-beta
    title "kbhujbal/Multi-Agent-AI-Travel-Advisor 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 57 --> 59
    line [58, 58]
```

2026-10-18 58 → 2026-10-26 58（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `ea03a11166e0` · [字段定义](../../DATASET.md)*
