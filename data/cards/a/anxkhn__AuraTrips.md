# anxkhn/AuraTrips

⭐ 25 · JavaScript · GPL-3.0 · 推送 2026-06-18 · [GitHub](https://github.com/anxkhn/AuraTrips) · [官网](https://auratrips.vercel.app/) · 个人维护

**面向旅行者的个性化行程生成 Web 应用（RAG+LLM）**

全栈 Web 应用：用户输入目的地、预算、兴趣与行程天数，系统从本地 CSV（Kaggle 来源，300+ 目的地与评分）检索相关目的地信息，经 RAG 流水线结合 LLaMA 3（通过 Groq API 访问）生成个性化行程，并集成 Google Maps 可视化。后端 FastAPI + SQLite，前端 React/Vite + TailwindCSS。支持用户认证与行程保存，行程可导出 PDF 或经链接分享；对相同请求的 LLM 响应做缓存以降低调用成本。需自备 Groq API key 与 Google Maps API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- RAG 检索本地 CSV 目的地数据（300+ 条目与评分）引导 LLaMA 3 生成行程
- LLM 响应按哈希缓存，重复请求免再调用
- 行程可导出 PDF/打印，并生成可经邮件分享的唯一链接
- 用户认证与行程保存，Google Maps 位置可视化

## 适用场景

- 按预算和兴趣生成旅行行程
- 保存并管理与朋友分享已生成的行程
- 在地图上查看行程中的目的地

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L13: AuraTrips is an innovative, **AI-powered travel itinerary generator** designed to create personalized travel experi
> L20: - 🤖 AI-powered itinerary generation using **RAG** and LLM technologies
> L167: 1. **Data Ingestion**: We process a CSV file containing verified travel destination data sourced from Kaggle. This

## 星数曲线

```mermaid
xychart-beta
    title "anxkhn/AuraTrips 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-30 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `ccbe6852abc0` · [字段定义](../../DATASET.md)*
