# violet27chen/qiyuan-blog-template

⭐ 19 · TypeScript · MIT · 推送 2026-07-13 · [GitHub](https://github.com/violet27chen/qiyuan-blog-template) · [官网](https://www.qiyuan.icu) · 个人维护 · 中文 README

**带 RAG 站内 AI 问答的全功能 Astro 博客模板**

基于 Astro 5 的个人博客与技术资源站模板（衍生自 Koharu 主题），通过 GitHub Use this template 一键建仓，部署到 EdgeOne Makers 边缘函数。功能包括：博客文章（Markdown/MDX、Pagefind 搜索、三语）、站内 RAG AI 助手（Neon/Supabase 向量库 + 硅基流动嵌入重排 + 商汤/ModelScope/智谱多生成平台兜底）、评论、文章朗读（Edge TTS 本地预生成）、临时邮箱、网盘、短链与独立资源站。可选功能默认关闭，各功能在服务商免费额度内可零成本运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- RAG 站内问答：pgvector 余弦检索 + 混合检索 RRF 融合，多生成平台兜底
- 评论/图床/临时邮箱/短链/网盘等可选功能各依赖对应免费服务
- 文章朗读音频由 Edge TTS 本地预生成后存 R2
- 本地 dev 模式内置右键样式编辑器（仅 DEV 下挂载，不进生产）

## 适用场景

- 一键建仓搭建带 AI 问答与朗读的个人博客
- 在国内网络环境下用 EdgeOne 部署零成本博客及配套功能
- 搭建带网盘、短链与资源站的技术资源站点

## 场景标签

`RAG` `语音合成` · 领域:内容生成

## 证据(README 行号)

> L5: > 🚀 **带 AI 问答的 Astro 全功能博客模板** — 内置 RAG 站内问答、文章朗读、评论、网盘、短链与资源站，EdgeOne Makers 部署，开箱即用。
> L108: - **Astro 5**（SSG）+ 定制主题，支持中文 / English / 日本語 三语（`[lang]/` 镜像路由）。
> L118: - **站内 AI 助手（RAG）「就这篇文章问 AI」**：

## 星数曲线

```mermaid
xychart-beta
    title "violet27chen/qiyuan-blog-template 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `11f67bd4ac6f` · [字段定义](../../DATASET.md)*
