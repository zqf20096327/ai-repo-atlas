# iamjameskeane/realpolitik

⭐ 41 · TypeScript · MIT · 推送 2026-02-21 · [GitHub](https://github.com/iamjameskeane/realpolitik) · [官网](https://realpolitik.world) · 个人维护

**实时地缘政治事件监测仪表盘，AI 增强分析配 3D 地球**

Next.js + Mapbox 构建的实时地缘政治事件监测仪表盘：聚合 NewsAPI/Tavily 等多源新闻，按军事、外交、经济、动乱四类以彩色标记在 3D 地球上展示，支持事件聚类、来源时间线、深链分享与移动端三视图。Python worker 调用 Gemini 做事件摘要与影响预测，经 GitHub Actions 每 15 分钟定时运行，结果存 Cloudflare R2。自部署需 Node.js 18+、Python 3.10+、Mapbox token 与 Gemini API key。

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

- 多源新闻聚合、去重与语义相似度聚类
- Gemini 生成事件摘要与 Fallout 影响预测
- Mapbox 3D 地球展示，按类别颜色与严重度标记
- GitHub Actions 定时 worker + Cloudflare R2 存储 + Vercel 前端的部署架构

## 适用场景

- 在全球地图上实时追踪地缘政治事件的发展
- 通过 AI 简报快速了解事件的摘要与潜在影响
- 按军事/外交/经济/动乱分类筛选关注的事件流

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L47: - Gemini AI integration for event summarization
> L48: - Fallout prediction: AI-generated impact analysis

## 星数曲线

```mermaid
xychart-beta
    title "iamjameskeane/realpolitik 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-26"]
    y-axis "stars" 39 --> 42
    line [40, 41, 41]
```

2026-10-18 40 → 2026-10-26 41（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `3baba2d55703` · [字段定义](../../DATASET.md)*
