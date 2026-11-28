# Simonstorms/slidelot

⭐ 10 · TypeScript · 推送 2026-11-11 · [GitHub](https://github.com/Simonstorms/slidelot) · 个人维护

**TikTok 轮播图内容生成器：自动产出文案与幻灯片草稿**

以 Web 应用形式运行的 TikTok 轮播图（carousel）内容生成流水线：用 Claude 生成钩子文案，每条钩子转成 6 页幻灯片（AI 生成图片加文字叠加），经人工审核队列批准后通过 Postiz 推送为 TikTok 草稿，并将发布后的互动数据回流用于跟踪表现。技术栈为 React 19、Hono、tRPC、Drizzle、SQLite、Bun、Turborepo，通过 bun install 与 bun run dev 启动，Web UI 在 localhost:3001、API 在 localhost:3000，需自行填入 API keys。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Claude 生成钩子文案并转化为 6 页轮播幻灯片
- FAL.ai 支持多模型图片生成（FLUX、Recraft、GPT Image、Imagen）
- 人工审核队列：编辑/拒绝/批准后经 Postiz 推送为 TikTok 草稿
- 分析数据回流，跟踪胜负内容

## 适用场景

- 批量生成 TikTok 轮播帖草稿并人工把关后发布
- 为特定内容领域自动产出钩子文案与配图
- 根据发布后的分析数据筛选表现好的内容模式

## 场景标签

`AI 写作` `图像生成` · 领域:内容生成

## 证据(README 行号)

> L9: 1. **Generate hooks** — Claude generates scroll-stopping hook texts based on your niche
> L10: 2. **Create slides** — Each hook becomes a 6-slide carousel (AI images + text overlays)
> L23: **AI services:** Claude Sonnet (hooks/captions) · FAL.ai (image generation — FLUX, Recraft, GPT Image, Imagen) · Sh


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `faba575680b1` · [字段定义](../../DATASET.md)*
