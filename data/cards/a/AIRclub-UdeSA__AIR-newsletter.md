# AIRclub-UdeSA/AIR-newsletter

⭐ 10 · TypeScript · 推送 2026-11-24 · [GitHub](https://github.com/AIRclub-UdeSA/AIR-newsletter) · 个人维护

**大学 AI/机器人社的自动化新闻通讯流水线**

为 UdeSA 的 AIR Club（AI 与机器人社团）构建的自动化新闻通讯系统：GitHub Actions 每周一抓取 sources.yaml 定义的 RSS 源与竞赛页面，打分去重后提交每周精选；手动触发月度构建时汇总最近 4–5 期周摘要、选出前 10 篇，可选调用 Gemini 生成编辑导语，用 React Email 渲染 HTML 邮件并上传为 artifact，人工审阅后经 Gmail 发送。AI 步骤可关闭，无 API key 也能完整构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- GitHub Actions 周度 RSS 抓取、打分与去重，自动提交每周精选
- 月度构建汇总周摘要并渲染 HTML 邮件 artifact
- 可选 Gemini/NVIDIA 的 AI 编辑导语（NEWSLETTER_AI_PROVIDER 控制）
- 支持 content/manual/ 下 Markdown 投稿（DEL CLUB 栏目）

## 适用场景

- 社团/组织定期聚合 AI 新闻并发送邮件通讯
- 按 research/tooling/competition 分类组织内容
- 在 CI 中定时采集与策展 RSS 源内容

## 场景标签

`工作流自动化` `网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L3: Automated newsletter system for AIR Club UdeSA, the AI and robotics club at Universidad de San Andrés. It scrapes AI
> L15: 2. **Monthly build** — Triggered manually from the Actions tab. Pulls the last 4–5 weekly digests, picks the top 10
> L89: Both are optional. Without them the newsletter still builds, just without the AI-generated intro paragraph.

## 星数曲线

```mermaid
xychart-beta
    title "AIRclub-UdeSA/AIR-newsletter 星数(近 2 点)"
    x-axis ["2026-10-30", "2026-11-24"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-30 10 → 2026-11-24 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 mid · 依据 README sha `f8c8c8a4b67e` · [字段定义](../../DATASET.md)*
