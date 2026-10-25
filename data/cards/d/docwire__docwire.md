# docwire/docwire

⭐ 117 · C++ · NOASSERTION · 推送 2026-10-02 · [GitHub](https://github.com/docwire/docwire) · [官网](https://docwire.io) · 组织维护

**本地优先的 C++20 数据处理 SDK：构建可审计的文档/AI 流水线**

可嵌入自身应用的 C++20 软件开发包，提供以 operator| 组合的数据处理流水线组件：摄取 100+ 种文件格式（Office/PDF/邮件/图像 OCR/归档等），做格式检测、解析、结构化与转换（过滤、翻译、分类、情感分析、实体抽取、嵌入），导出为文本/HTML/CSV 或通过 HTTP 输出。默认本地运行，云 AI 仅作为显式流水线步骤；可选集成 llama.cpp 本地模型与 IBM Granite 4.0 1B（CPU 推理）。面向需要在受监管或边缘环境构建确定性、可审计数据处理管道的开发者与企业。部分功能（数据库/ERP 连接器、注入式审计接口等）仍在路线图中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- operator| 组合流水线，嵌入自有 C++20 应用
- 100+ 输入格式解析与 100+ 语言 OCR
- 解析、OCR、本地文档 AI 与本地文本嵌入可完全离线运行
- 可选 llama.cpp 集成与 IBM Granite 4.0 1B 模型（CPU 推理）

## 适用场景

- 把脏 PDF、邮件归档、旧版 Office 文件规范化为可嵌入/分块的 LLM 就绪数据
- 在本地构建不外发数据的文档抽取与 OCR 流水线
- 为合规或审计场景搭建确定性、可审计的数据处理管道

## 场景标签

`文档解析` `OCR` · 领域:知识与检索

## 证据(README 行号)

> L9: DocWire SDK is an embeddable software development kit (SDK): a set of reusable C++ building blocks for building data
> L17: - **Transform** data with filters, translations, summaries, classification, entity extraction, sentiment analysis, 
> L81: **The layer your AI pipeline is missing:** Raw documents are rarely LLM-ready. Dirty PDFs, malformed email archives

## 星数曲线

```mermaid
xychart-beta
    title "docwire/docwire 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 116 --> 118
    line [117, 117]
```

2026-10-18 117 → 2026-10-25 117（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `13decc4fa837` · [字段定义](../../DATASET.md)*
