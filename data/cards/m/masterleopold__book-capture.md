# masterleopold/book-capture

⭐ 14 · JavaScript · MIT · 推送 2026-07-26 · [GitHub](https://github.com/masterleopold/book-capture) · [官网](https://github.com/masterleopold/book-capture) · 个人维护

**Claude Code 插件：从 Kindle/Apple Books/PDF 截图取书并生成结构化 Markdown**

运行于 Claude Code 的插件，将书籍页面从 5 种来源（Mac Kindle、Apple Books、Kindle Cloud Reader、PDF、纸质书照片）截取为图片，用 macOS Vision OCR 提取文本，低置信度页面交由 Claude Code agent 以多模态方式重读，最终生成 8-14 个主题化 Markdown 文件及带 wikilinks 的中枢文件，面向 Obsidian 知识库。整条流水线本地运行，无需外部 API key；限 macOS，需 Node.js 20+、Xcode 命令行工具与辅助功能权限。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 5 种捕获来源：Mac Kindle/Apple Books/Cloud Reader/PDF/纸质书照片
- macOS Vision OCR + Claude agent 重读低置信度页面
- 生成 8-14 个主题文件与带 wikilinks 的中枢文件
- 页面图存为 WebP（2000px q85），并提供旧库压缩转换脚本

## 适用场景

- 把 Kindle/Apple Books 里买的电子书转成 Obsidian 笔记
- 将扫描版 PDF 或拍照的纸质书整理成主题化 Markdown
- 批量建立个人读书知识库并跨主题互链

## 场景标签

`知识库管理` `OCR` `文档解析` · 领域:知识与检索

## 证据(README 行号)

> L7: A Claude Code plugin that captures book pages as screenshots, extracts text via OCR, and generates thematically orga
> L16: The entire pipeline runs locally with no external API keys — OCR and content generation use Claude Code's built-in 

## 星数曲线

```mermaid
xychart-beta
    title "masterleopold/book-capture 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `fc1ad1a36ba5` · [字段定义](../../DATASET.md)*
