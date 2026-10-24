# DocumentAtom/DocumentAtom

⭐ 54 · C# · MIT · 推送 2026-10-03 · [GitHub](https://github.com/DocumentAtom/DocumentAtom) · 组织维护

**将多格式文档解析为原子并分块的 C# 库/服务器，服务 RAG**

DocumentAtom 是一套 .NET 库与服务器：把 CSV、JSON、XML、HTML、Markdown、Word、Excel、PowerPoint、PDF 及图片等输入解析为原子（atoms）及其层级子结构（quarks），并通过 Tesseract OCR 处理文档内嵌图片。v3 起采用 JSON envelope API，支持按请求配置解析参数与 11 种分块策略（含 3 种重叠模式），输出可直接用于嵌入与检索的 chunks。提供 C#/TypeScript/Python SDK、REST 与 MCP 服务器，DataIngestion 包集成 Microsoft.Extensions.AI 用于 RAG。运行要求宿主机安装 Tesseract v5.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持十余种文档格式的原子化解析与层级结构（quarks）提取
- 11 种服务器端分块策略与 3 种重叠策略，按请求 JSON envelope 配置
- Tesseract OCR 处理文档内嵌图片
- 提供 C#/TypeScript/Python SDK、REST/MCP 服务器与 OpenTelemetry 诊断

## 适用场景

- RAG 管线中将 PDF、Office、HTML 等文档解析并分块后送入嵌入与向量存储
- 通过 MCP 服务器让 LLM 客户端调用文档解析工具
- 表格、列表等结构化数据的分块与抽取

## 场景标签

`文档解析` · 领域:知识与检索

## 证据(README 行号)

> L3: DocumentAtom provides a light, fast library for breaking input documents into constituent parts (atoms), useful for 
> L15: |`DocumentAtom.DataIngestion`|Microsoft.Extensions.AI integration for RAG|NuGet Version|
> L71: - **Enable and configure chunking on the fly.** Choose from 11 chunking strategies, set token budgets, pick an over

## 星数曲线

```mermaid
xychart-beta
    title "DocumentAtom/DocumentAtom 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 53 --> 55
    line [54, 54]
```

2026-10-18 54 → 2026-10-24 54（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `6113eafb3c2c` · [字段定义](../../DATASET.md)*
