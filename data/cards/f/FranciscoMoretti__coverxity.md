# FranciscoMoretti/coverxity

⭐ 14 · TypeScript · 推送 2026-04-02 · [GitHub](https://github.com/FranciscoMoretti/coverxity) · [官网](https://coverxity.vercel.app/) · 个人维护

**输入文章标题，AI 生成封面图建议并裁剪 OG 图**

基于 Next.js 14 的 Web 工具：用户输入文章标题，调用 OpenAI API 分析并生成相关图片类别建议，通过 Pexels API 检索图片供浏览。支持原图下载、一键复制 URL，内置 react-image-crop 裁剪工具生成 1200x630 的 OG 图。面向内容创作者部署使用，需自行配置 OPENAI_API_KEY 与 PEXELS_API_KEY，通过克隆仓库、npm 安装依赖后本地运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 根据文章标题由 AI 生成图片类别建议并检索 Pexels 图片
- 内置裁剪工具生成 1200x630 优化 OG 图
- 支持原图下载与一键复制图片 URL

## 适用场景

- 为我的文章快速找到并裁剪合适的封面图
- 生成适配社交分享的 OpenGraph 图片

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L5: Coverxity is an AI-powered tool that helps you find the perfect cover images for your content. Using advanced image 
> L9: - **AI-Powered Image Search**: Enter your article title and get AI-curated image suggestions

## 星数曲线

```mermaid
xychart-beta
    title "FranciscoMoretti/coverxity 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `b7ea318ca394` · [字段定义](../../DATASET.md)*
