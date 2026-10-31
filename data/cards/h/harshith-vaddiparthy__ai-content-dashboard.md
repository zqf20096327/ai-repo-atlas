# harshith-vaddiparthy/ai-content-dashboard

⭐ 15 · TypeScript · MIT · 推送 2026-10-04 · [GitHub](https://github.com/harshith-vaddiparthy/ai-content-dashboard) · [官网](https://ai-content-dashboard-murex.vercel.app) · 个人维护

**面向创作者的单用户 AI 内容生成与追踪仪表盘**

基于 Next.js 16 + shadcn/ui 的单用户 Web 应用，供创作者在一个仪表盘内完成博客、newsletter 的 AI 起草、AI 视频概念生成（OpenRouter 出文案概念，Higgsfield 渲染为规划项）、内容库管理、状态流转与表现追踪；顶栏含 AI Agent 侧边聊天，可读库但不改库。无 API key 与数据库时以 sample mode 运行；PostgreSQL/Prisma 与 Higgsfield 渲染、视频生成均为规划中尚未实现，三个环境变量全部可选。定位为可 fork 的干净基础，供独立开发者套品牌发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- OpenRouter 驱动的流式长文与 newsletter 生成，支持六种写作模型选择
- AI Agent 侧边栏聊天：出创意/标题/大纲，读取内容库但不可修改
- 无 key 无数据库的 sample mode 可完整试用
- 内容库含 draft/ready/published/archived 状态、类型筛选与表现看板

## 适用场景

- 独立创作者从简报生成博客与 newsletter 草稿并管理发布状态
- 追踪已发布内容的浏览/打开数据与平均表现对比
- fork 后套自有品牌快速搭建内容产品

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L27: - ✍️ **Write** long-form blog posts and newsletters with AI
> L38: |**Blog Post Generation**|Write from a short brief: topic, audience, tone and length. The draft streams in word by 
> L44: |**AI Agent**|An **AI Agent** button in the top bar opens a chat in a right sidebar on every page. Ask for ideas, t

## 星数曲线

```mermaid
xychart-beta
    title "harshith-vaddiparthy/ai-content-dashboard 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-31 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `b5f5bc7315d5` · [字段定义](../../DATASET.md)*
