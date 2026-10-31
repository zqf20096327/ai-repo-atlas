# pras-ops/udemy-transcript-extractor

⭐ 24 · TypeScript · MIT · 推送 2026-10-07 · [GitHub](https://github.com/pras-ops/udemy-transcript-extractor) · 组织维护

**离线提取网课字幕转笔记的浏览器扩展，含高亮/搜索/导出**

Chrome 扩展，从 Udemy、Coursera、YouTube 及通用 HTML5 播放器（Panopto、Kaltura、Echo360 等）提取字幕并整理为可读笔记：清理口癖与乱序字幕、按语义分章、提取关键概念与讲师定义、跨课程语义搜索（返回带时间戳的原文段落而非生成答案）、时间戳跳回视频、高亮/笔记/截图，导出 Markdown、SRT、Anki 等 10 种格式。全部本地运行、无网络请求、无账号。语义搜索用 Model2Vec 静态嵌入查表实现；文字识别与摘要依赖 Chrome 内置 Gemini Nano，多数机器不可用。库无备份同步，站点改版可能破坏提取。

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

- 专用于 Udemy/Coursera/YouTube 的提取器 + 基于 TextTrack API 的通用提取器
- 语义搜索用 Model2Vec potion-base-8M 静态嵌入查表，模型随包内置（约 30MB），无推理运行时
- 理解功能（分章/概念/定义/关键句）全部为抽取式统计方法，不生成内容
- 时间戳双向联动：高亮、笔记、搜索结果均可跳回视频对应时刻

## 适用场景

- 边看网课边记笔记，不用暂停切换应用
- 把整门课程的字幕整理成可搜索的笔记库并导出 Markdown
- 为 NotebookLM/Obsidian/Anki 等工具准备预分块的转录材料

## 场景标签

`知识库管理` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L33: - **One click, any lecture.** Dedicated extractors for Udemy, Coursera and YouTube, plus a generic
> L116: Search uses **Model2Vec `potion-base-8M` static embeddings**, which is a lookup table rather than a
> L127: Two features genuinely need generation: prose summaries, and reading text off a captured frame.

## 星数曲线

```mermaid
xychart-beta
    title "pras-ops/udemy-transcript-extractor 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-31 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `5485fecb1f2f` · [字段定义](../../DATASET.md)*
