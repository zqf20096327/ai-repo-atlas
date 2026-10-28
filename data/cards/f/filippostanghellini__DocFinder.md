# filippostanghellini/DocFinder

⭐ 35 · Python · NOASSERTION · 推送 2026-10-07 · [GitHub](https://github.com/filippostanghellini/DocFinder) · [官网](https://filippostanghellini.github.io/DocFinder/) · 个人维护

**本地优先的文档语义搜索与问答桌面应用**

面向个人用户的桌面应用：将 PDF、Word、PowerPoint、EPUB、Markdown 等文档建立语义索引，嵌入存储在 SQLite，全部在本机运行，无需云服务或账号。支持语义搜索与基于本地 Qwen3.5 模型的文档问答，自动按硬件选择运行时（Metal/CUDA/ROCm）；可通过设置连接本地或远程 Ollama 服务器自选嵌入与对话模型。提供隐私模式：标记为私有的文件强制本地嵌入并拒绝远程 LLM。提供 macOS/Windows/Linux 安装包，也可从 Python 源码运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 多种格式文档的本地语义索引与搜索（嵌入存于 SQLite）
- AI 文档问答，内置本地 Qwen3.5 模型并按硬件自动选择
- 可接入 Ollama 服务器自选嵌入与对话模型
- 隐私模式：私有文件强制本地处理、屏蔽远程 LLM

## 适用场景

- 在本机离线搜索自己的 PDF、Word、EPUB 等文档
- 对文档提问并获得带上下文的回答而不上传文件
- 配合自有 Ollama 服务器使用自定义模型

## 场景标签

`文档问答` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L12:  Local-first semantic search for your documents.
> L21: - **AI chat** — ask questions about any document and get precise answers, powered by local Qwen3.5 models (automati

## 星数曲线

```mermaid
xychart-beta
    title "filippostanghellini/DocFinder 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-28"]
    y-axis "stars" 33 --> 36
    line [34, 35, 35]
```

2026-10-18 34 → 2026-10-28 35（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `5ccacc774408` · [字段定义](../../DATASET.md)*
