# impel-intelligence/Minna

⭐ 18 · Swift · Apache-2.0 · 推送 2026-09-29 · [GitHub](https://github.com/impel-intelligence/Minna) · [官网](https://tryminna.com) · 组织维护

**Mac 上的本地优先文档搜索与 AI 问答助手**

面向 macOS 26.0+ 用户的原生应用：将 PDF、Markdown、TXT、HTML、XML、OPML 等文件在本地建索引，支持自然语言向量检索与 FTS5 精确匹配，索引为单个可迁移的 .irisdb 文件。问答功能中每个生成语句附数据库中的直接引文作为出处。支持多种 LLM 提供方：MLX 与 Apple Intelligence 端侧模型、Ollama 端侧/远程、以及 Anthropic/OpenAI/Gemini 密钥接入。文件不上传，密钥加密存于 macOS 钥匙串。以 dmg 安装包分发，也可从源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地索引 + 向量与 FTS5 双路检索，索引为单个可移植 .irisdb 文件
- 回答中每个生成语句附数据库直接引文出处
- 多 LLM 提供方：MLX/Apple Intelligence 端侧、Ollama、Anthropic/OpenAI/Gemini 密钥
- 支持 PDF/Markdown/TXT/HTML/XML/OPML 并可在应用内预览与提问

## 适用场景

- 在 Mac 上对个人文档库做自然语言搜索
- 对已索引文档提问并获得带引文出处的回答
- 本地离线运行 AI 问答，文件不上传

## 场景标签

`文档问答` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L3: Minna is a local-first search database and AI assistant for your documents. Files are indexed on **your** Mac, they 
> L27: - Search with natural language (vector) & exact match (FTS5) through all files added to Minna.
> L31: - Ask Minna about anything in any document.

## 星数曲线

```mermaid
xychart-beta
    title "impel-intelligence/Minna 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-30"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-30 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `44db74a6bf3e` · [字段定义](../../DATASET.md)*
