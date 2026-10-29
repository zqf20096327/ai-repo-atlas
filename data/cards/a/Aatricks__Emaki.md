# Aatricks/Emaki

⭐ 26 · Kotlin · GPL-3.0 · 推送 2026-09-04 · [GitHub](https://github.com/Aatricks/Emaki) · 个人维护

**Android 多格式阅读器，支持本地 LLM 离线章节摘要**

用 Kotlin 与 Jetpack Compose 构建的 Android 阅读器，支持网络小说、漫画、manhwa、EPUB、PDF 与 HTML。内置爬虫可从小说站点抽取章节文本，支持整部作品预取缓存离线阅读与跨多源统一搜索，所有数据存储在设备本地。提供 standard 与 ai 两个构建变体：ai 变体启用本地 AI 章节摘要并自动从 Maven Central 下载 llmedge 依赖；standard 变体不含该功能。需 JDK 17+ 与 Android Studio 从源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 内置爬虫从小说站点抽取文本与章节
- 整部作品预取缓存离线阅读
- 跨多源（MangaBat、NovelFire 等）统一搜索
- ai 构建变体通过 llmedge 本地 LLM 生成章节摘要

## 适用场景

- 在手机上离线阅读网络小说、漫画与本地 PDF/EPUB
- 跨多个来源一次性搜索想看的作品
- 阅读时长章节时获取本地生成的摘要

## 场景标签

`网页抓取` `AI 写作` · 领域:效率与自动化

## 证据(README 行号)

> L9: An Android reader for web novels, manga, manhwa, and local files (like PDFs and EPUBs). Built with Kotlin and Jetpac
> L21: - **Local AI**: Summarizes chapters on-device using a local LLM.
> L46: - **`standard` (default)**: Normal build. Doesn't need the local `llmedge` library. AI summarization is visible but

## 星数曲线

```mermaid
xychart-beta
    title "Aatricks/Emaki 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-29"]
    y-axis "stars" 24 --> 27
    line [25, 26, 26]
```

2026-10-18 25 → 2026-10-29 26（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `dc9b08d3c757` · [字段定义](../../DATASET.md)*
