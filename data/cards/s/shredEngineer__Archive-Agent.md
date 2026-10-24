# shredEngineer/Archive-Agent

⭐ 63 · Python · GPL-3.0 · 推送 2026-10-07 · [GitHub](https://github.com/shredEngineer/Archive-Agent) · [官网](https://wilhelm.dev) · 个人维护

**本地文件 AI 索引与 RAG 检索工具，附带 MCP 服务器接口**

面向个人用户/开发者的命令行文件索引器：按通配符模式跟踪本地文件，将 PDF、图片、Markdown、docx 等解码为文本，经 AI 智能分块（含上下文头）生成向量并存入本地 Qdrant 数据库，支持语义搜索与提问。OCR 部分实验性，PDF 提供 strict/relaxed/auto 三种 OCR 策略；可选用 OpenAI/OpenRouter 远程 API 或 Ollama/LM Studio 本地模型，内置 MCP 服务器接入工作流。安装需 Docker（运行 Qdrant）与 Python>=3.10，在 Ubuntu 上经 install.sh 源码安装，GUI/MCP/Qdrant 由统一密码保护。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 按文件模式自动跟踪并同步到本地 Qdrant 向量数据库
- AI 智能分块（上下文头+块边界衔接）与 rerank/扩展检索
- 图像 OCR 与实体提取，PDF 三种 OCR 策略可选
- 支持 OpenAI/OpenRouter/Ollama/LM Studio 并内置 MCP 服务器

## 适用场景

- 用自然语言搜索本地的 PDF、图片和文档
- 把本地文件库接入 MCP 客户端进行问答
- 在离线环境用 Ollama/LM Studio 索引和检索文件

## 场景标签

`RAG` `语义搜索` `文档解析` · 领域:知识与检索

## 证据(README 行号)

> L5: *An intelligent file indexer with powerful AI search (RAG engine), automatic OCR, and a seamless MCP interface.*
> L19: - **Unlock your documents with semantic AI search & query**
> L35: - **Supports many AI providers and MCP**

## 星数曲线

```mermaid
xychart-beta
    title "shredEngineer/Archive-Agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 62 --> 64
    line [63, 63]
```

2026-10-18 63 → 2026-10-24 63（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `e7208bb1a551` · [字段定义](../../DATASET.md)*
