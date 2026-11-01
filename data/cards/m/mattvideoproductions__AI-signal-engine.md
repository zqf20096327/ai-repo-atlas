# mattvideoproductions/AI-signal-engine

⭐ 23 · TypeScript · Apache-2.0 · 推送 2026-10-30 · [GitHub](https://github.com/mattvideoproductions/AI-signal-engine) · [官网](https://www.youtube.com/@MattVidPro) · 个人维护

**自托管 AI 新闻情报仪表盘：agent 扫描新闻并可视化成关系图谱与简报**

面向内容创作者（如 AI 新闻 YouTuber）的自托管 Next.js 仪表盘。自主 agent（默认 Nous Hermes，也接受任何可浏览并 POST 的 agent）扫描信息源、评分风险，将结构化事件推送到仪表盘，以 React Flow 实时关系图谱展示故事关联，并生成含验证清单与'勿夸大'警示的创作者简报。仪表盘本身无需 LLM key，简报引擎为确定性 v1。支持演示模式、RSS 真实源扫描、密码与令牌防护。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- React Flow 实时关系图谱：节点按类别着色、关系线分类（竞争/支持/风险等）
- 创作者简报：摘要、标题/缩略图创意、验证清单与风险声明列表，支持 markdown 导出
- 任何可浏览并 POST 的 agent 均可接入，仪表盘本身无需 LLM key
- 一键演示模式模拟 10 个事件流，另有 RSS 真实源扫描

## 适用场景

- AI 新闻创作者追踪动态并整理成节目选题与简报
- 以可视化图谱形式观看 agent 实时研究发现（适合录屏）
- 任意主题研究工作流的事件监测与关联分析

## 场景标签

`知识图谱` · 领域:知识与检索

## 证据(README 行号)

> L8: creator-first for AI news, useful for any research workflow. An autonomous agent (built around
> L11: structured events into this dashboard, which visualizes them as a living relationship map and
> L12: turns them into an actionable **brief**: angles, story bundles, talking points, and (critically)


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `79b710f26e72` · [字段定义](../../DATASET.md)*
