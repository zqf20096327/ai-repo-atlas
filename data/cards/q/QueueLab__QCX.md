# QueueLab/QCX

⭐ 19 · TypeScript · Apache-2.0 · 推送 2026-10-18 · [GitHub](https://github.com/QueueLab/QCX) · [官网](https://www.core.queue.cx) · 组织维护

**面向情报分析师的行星 Copilot：对话式地理空间智能平台**

基于 Next.js 构建的云优化地理空间智能平台，提供对话式 Planetary Copilot：通过 Vercel AI SDK 在 xAI Grok、Google Gemini、AWS Bedrock、OpenAI 间按 key 配置路由请求，支持视觉任务自动切换视觉模型。集成 Mapbox 地图交互、SkyFi 卫星影像（OAuth 2.1+PKCE）、AlphaEarth Foundations 卫星嵌入 API（GCS 范围请求取单像素）、Tavily 实时新闻检索与反向地理编码。采用 Clerk+Supabase 双写同步与行级安全。以 Bun 为包管理器与运行时，提供 Docker Compose 与 Google Cloud Build 部署路径。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多模型统一路由（xAI Grok / Gemini / Bedrock / OpenAI），视觉任务自动切换视觉模型
- SkyFi 卫星影像任务下单：OAuth 2.1+PKCE、防误扣费的 dry-run 与幂等键
- AlphaEarth 64 维时序卫星嵌入：GCS 范围请求仅取所需单像素
- Clerk-Supabase 双写一致性与 8 表行级安全控制

## 适用场景

- 情报分析师通过对话查询卫星影像并关联本地时间与近期新闻
- 研究者按坐标获取全年多传感器卫星嵌入（2017-2024）
- 下载指定区域观测与影像的综合报告

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L15: **Quality Computer Experience (QCX)** is a production-ready, cloud-optimized **Planetary Copilot and Geospatial Int
> L21: - **Unified Provider Routing**: Seamlessly shifts requests between xAI (Grok-3-mini, Grok-2-vision), Google Gemini 

## 星数曲线

```mermaid
xychart-beta
    title "QueueLab/QCX 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `3864f5149da4` · [字段定义](../../DATASET.md)*
