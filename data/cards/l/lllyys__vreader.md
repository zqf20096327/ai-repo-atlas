# lllyys/vreader

⭐ 45 · Swift · 推送 2026-08-06 · [GitHub](https://github.com/lllyys/vreader) · 个人维护 · 中文 README

**iOS 阅读 App：多格式电子书阅读，附带 AI 助手与标注**

面向 iPhone/iPad 的阅读应用，支持 EPUB、AZW3/MOBI、PDF、TXT、Markdown，用 Swift 6/SwiftUI/SwiftData 构建，代码由 AI agent 编写、人类指导。核心功能含标注、SQLite FTS5 全文检索、TTS、OPDS 目录、Legado 兼容书源、WebDAV 备份。AI 部分为自带 API key 的阅读内助手：多轮对话、摘要、双语逐行翻译、整书后台翻译、可选的工具调用与来源披露；可配置多个提供商（Anthropic、OpenAI 兼容或本地）。Android 原生版本开发中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 多格式阅读（EPUB/AZW3/PDF/TXT/MD）与全格式标注 CRUD
- 自带 LLM key 的阅读内 AI：聊天、摘要、翻译、整书后台翻译
- 多提供商配置（Anthropic/OpenAI 兼容/本地），keychain 存密钥
- WebDAV 备份含 AI 对话历史，SQLite FTS5 全文检索（CJK 分词）

## 适用场景

- 在 iPhone/iPad 上阅读多格式电子书并做高亮笔记
- 阅读时向 AI 助手提问、获取章节摘要或逐行双语翻译
- 通过 OPDS 与 Legado 兼容书源获取书籍，用 WebDAV 跨设备同步

## 场景标签

`文档问答` `语音合成` · 领域:内容生成

## 证据(README 行号)

> L7: An iOS reader for EPUB, AZW3/MOBI (Kindle), PDF, TXT, and Markdown — built entirely by AI coding agents, with Swift 
> L31: 1. **In-reader AI assistant, bring-your-own-LLM** — chat, summarize, and translate against *your* OpenAI-compatible

## 星数曲线

```mermaid
xychart-beta
    title "lllyys/vreader 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-30"]
    y-axis "stars" 43 --> 46
    line [44, 45, 45]
```

2026-10-18 44 → 2026-10-30 45（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `7de347ef42eb` · [字段定义](../../DATASET.md)*
