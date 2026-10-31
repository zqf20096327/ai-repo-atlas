# edilma/RAG-App-HackTogether

⭐ 14 · C# · 推送 2026-09-06 · [GitHub](https://github.com/edilma/RAG-App-HackTogether) · 个人维护

**.NET 8 的多语言 RAG 文档问答应用：基于私有 PDF 集合回答**

用 .NET 8、Semantic Kernel、Azure OpenAI、Qdrant 与 PdfPig 实现的检索增强问答应用：启动时用 PdfPig 解析 data/ 目录 PDF，切块生成嵌入存入 Qdrant；用户提问后经语义检索取回片段，由 Semantic Kernel 组合上下文交 Azure OpenAI 生成回答，支持多语言问答。仅从提供的文档作答，超出范围返回无回答；分块为固定大小，无自动评测。为 Microsoft .NET Hack Together 而建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PdfPig 解析 PDF → 固定分块 → 嵌入存储于 Qdrant 的 RAG 流水线
- Semantic Kernel 编排检索上下文与对话，Azure OpenAI 生成回答
- 多语言提问与回答，仅基于提供文档作答（范围外返回无回答）
- Qdrant 通过 Docker 本地部署，索引每集合仅运行一次

## 适用场景

- 基于官方 PDF 文档集合做多语言问答
- 在 .NET 技术栈内实现 RAG 应用
- 为文档范围外的提问返回无回答以保证可靠性

## 场景标签

`文档问答` · 领域:知识与检索

## 证据(README 行号)

> L11: The application lets users ask questions in multiple languages and receive responses grounded in a private collecti
> L31: 7. **Azure OpenAI** generates a response grounded in the retrieved documents.
> L119: 3. Semantic Kernel sends the question and supporting context to the language model.

## 星数曲线

```mermaid
xychart-beta
    title "edilma/RAG-App-HackTogether 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `6d0a10bc5c77` · [字段定义](../../DATASET.md)*
