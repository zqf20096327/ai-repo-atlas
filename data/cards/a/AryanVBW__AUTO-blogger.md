# AryanVBW/AUTO-blogger

⭐ 21 · Python · NOASSERTION · 推送 2026-03-23 · [GitHub](https://github.com/AryanVBW/AUTO-blogger) · [官网](https://auto-blogger.netlify.app) · 个人维护

**自动化采集改写并发布 WordPress 文章的 AI 工具**

面向 WordPress 站长的内容自动化工具：从源站抓取文章链接与正文（Selenium），用 Gemini AI 改写内容、生成 SEO 标题/meta 描述与关键词组，用 OpenAI DALL-E 或 Getty Images 生成/配图，注入内外链并自动分类打标，最终通过 WordPress REST API 以草稿发布。提供 GUI 与 CLI，支持多域名配置档案与自更新。运行需 Python 3.8+、Chrome/Chromium、WordPress REST API 与 Gemini API key，OpenAI key 可选。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 13 步流水线：抓取→Gemini 改写→SEO 元数据→配图→WordPress 发布
- OpenAI DALL-E 2/3 图像生成与 Getty Images 编辑内容集成
- 多域名配置档案与单界面多站点管理
- GUI 与 CLI 双模式，跨平台（Windows/macOS/Linux）

## 适用场景

- 批量将源站文章改写为 SEO 优化内容并发布到 WordPress
- 自动为文章生成特色图与文内配图
- 多 WordPress 站点的统一内容管理

## 场景标签

`网页抓取` `AI 写作` `图像生成` · 领域:效率与自动化

## 证据(README 行号)

> L54: ### AI-Powered Content Generation
> L213: 3. **AI Paraphrasing** - Use Gemini AI to rewrite and optimize content

## 星数曲线

```mermaid
xychart-beta
    title "AryanVBW/AUTO-blogger 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-29 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `fd6319b4bd8f` · [字段定义](../../DATASET.md)*
