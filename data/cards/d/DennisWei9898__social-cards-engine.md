# DennisWei9898/social-cards-engine

⭐ 35 · Python · MIT · 推送 2026-07-07 · [GitHub](https://github.com/DennisWei9898/social-cards-engine) · 个人维护 · 中文 README

**Claude Code skill：把文章一键生成 IG 轮播图卡，内建 AI 审稿员**

以 Claude Code skill 形式提供的社群图卡生成引擎：用户对话指定主题或文章，引擎按可替换的 brand pack（配色/字体/语气）渲染 8–10 张 1080×1350 轮播卡（HTML+CSS → Chrome headless → PNG）。内建两个独立 AI 审稿员（carousel-joker 知识型、meme-joker 迷因型）逐卡打分、不合格退回；硬性指标由脚本检查。附带版权优先的自动找图管线（Openverse/Wikimedia 免 key，可选 Unsplash/Pexels）、去背 QA 管线与设计对焦闸。渲染需 macOS + Chrome + Python 3；伴生 skill huashu-design/social-post 为可选。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一引擎多 brand pack，换风格文件即换品牌视觉
- 两个独立 AI 审稿员逐卡打分，不合格退回重改
- 版权优先自动找图，每张记录来源与授权，不静默采用
- 去背 QA 管线（零白晕机器验证）与量产前设计对焦闸

## 适用场景

- 把文章或教学转成可发布的 IG 轮播图卡
- 个人 KOL 或品牌小编维护多品牌一致视觉
- 出图前用 AI 审稿员检查封面钩子、CTA 与迷因可读性

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L126: > This is a **Claude Code skill** — you chat with Claude and it makes the cards. Python 3 + Chrome are just the re
> L82: |**Card engine**|topic / article → a carousel of cards (HTML+CSS → Chrome headless → PNG)|
> L90: |**Two AI reviewers**|`carousel-joker` (knowledge posts), `meme-joker` (memes — turns "funny" into checkable criter

## 星数曲线

```mermaid
xychart-beta
    title "DennisWei9898/social-cards-engine 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-28 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `349f406bd6be` · [字段定义](../../DATASET.md)*
