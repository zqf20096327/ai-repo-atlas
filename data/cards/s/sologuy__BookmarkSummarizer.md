# sologuy/BookmarkSummarizer

⭐ 30 · Python · Apache-2.0 · 推送 2025-12-01 · [GitHub](https://github.com/sologuy/BookmarkSummarizer) · 个人维护 · 中文 README

**把浏览器书签抓取并生成 AI 摘要，构建可搜索的个人知识库**

Python 命令行工具，从 Chrome/Firefox/Edge/Safari 等浏览器读取书签，多线程抓取网页内容（动态页自动切换 Selenium），调用 LLM 为每个书签生成摘要，存入 LMDB 数据库，并通过 Whoosh 构建离线全文模糊搜索索引，以本地 Web 服务提供检索。支持 OpenAI/Deepseek/Qwen/Ollama 后端，含增量更新与断点恢复、自定义解析器（如 YouTube 字幕提取）。需 Python 3.6+ 与网络连接，提供 PyPI、预编译二进制与源码三种安装方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多浏览器书签抓取 + LLM 摘要生成，存入 LMDB
- Whoosh 离线全文模糊搜索，本地 Web 界面检索
- 增量更新与检查点恢复，可扩展至百万级书签
- 支持 OpenAI/Deepseek/Qwen/Ollama（含 100% 离线生成）

## 适用场景

- 把多年积攒的书签变成可全文搜索的知识库
- 用本地 Ollama 模型离线生成摘要保护隐私
- 增量式持续整理新增书签

## 场景标签

`知识库管理` `网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L11: BookmarkSummarizer is a powerful tool that crawls your browsers' bookmarks, generates summaries using large languag
> L18: - 🤖 **AI Summary Generation**: Create high-quality summaries for each bookmark using large language models
> L21: - 🌐 **Multiple Model Support**: Compatible with OpenAI, Deepseek, Qwen, and Ollama offline models

## 星数曲线

```mermaid
xychart-beta
    title "sologuy/BookmarkSummarizer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-28 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `75fa0a3bab95` · [字段定义](../../DATASET.md)*
