# MuhammadTanveerAbbas/kanbi

⭐ 15 · TypeScript · MIT · 推送 2026-10-18 · [GitHub](https://github.com/MuhammadTanveerAbbas/kanbi) · [官网](https://kanbi.vercel.app) · 个人维护

**AI 看板工具：把笔记/PDF/网址自动抽取为任务并分组看板**

基于 Next.js + Supabase + Stripe 的开源看板 Web 应用，面向独立开发者、自由职业者与小团队。粘贴文本、上传 PDF 或提供公开 URL，由语言模型抽取行动项生成看板；工作负载健康分、倦怠风险、截止日期聚类、自动排程等由确定性 TypeScript 代码计算并有单元测试。AI 层通过 OpenAI 兼容运行时提供（如 Groq 或本地 Ollama），支持按请求发现模型、缓存目录与降级回退；AI 不可用时回退到要点解析与规则回复。含 Stripe 免费/Premium 订阅分层与 RLS 行级安全。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 文本/PDF/URL 三种输入的任务抽取生成看板
- 工作负载健康分、倦怠风险、自动排程为确定性计算，AI 不可用时降级运行
- AI 层抽象为 OpenAI 兼容运行时，模型按请求从 /v1/models 目录动态发现与轮换
- Stripe 订阅分层与 Supabase RLS 行级安全，支持 DOCX/PDF 导出

## 适用场景

- 把会议记录、PDF 或网页要点整理成可执行的任务看板
- 查看每周工作负载健康分与倦怠风险提示
- 用对话式助手规划与调整看板任务优先级

## 场景标签

`文档解析` · 领域:知识与检索

## 证据(README 行号)

> L19: Kanbi turns raw, unstructured notes into an actionable task board. Paste text, upload a PDF, or give it a public we
> L31: This means the product still works, in a degraded but honest way, when the AI

## 星数曲线

```mermaid
xychart-beta
    title "MuhammadTanveerAbbas/kanbi 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `dadaf857caac` · [字段定义](../../DATASET.md)*
