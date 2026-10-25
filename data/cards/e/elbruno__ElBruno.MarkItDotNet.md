# elbruno/ElBruno.MarkItDotNet

⭐ 56 · C# · MIT · 推送 2026-10-19 · [GitHub](https://github.com/elbruno/ElBruno.MarkItDotNet) · 个人维护

**面向 AI 管线的 .NET 文件转 Markdown 库（15+ 格式）**

以多个 NuGet 包分发的 .NET 转换库：核心包含 12 个内置转换器，处理文本、JSON、HTML、URL、DOCX、PDF、RTF、EPUB、图片、CSV、XML、YAML；卫星包扩展 Excel、PowerPoint、AI 驱动的 OCR/图像描述/音频转录（依赖 Microsoft.Extensions.AI 的 IChatClient）、基于 Whisper ONNX 的本地离线转录，以及安全扫描与转换质量评估助手。另提供 CLI 工具 markitdown-dotnet 支持批量转换，支持流式分块处理大文件。目标框架为 .NET 8.0 与 10.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 核心包含 12 个内置转换器，覆盖 15+ 文件格式含 URL 网页
- Whisper ONNX 本地离线音频转录，无需云 API
- AI 卫星包经 IChatClient 提供 LLM 视觉 OCR 与音频转录
- 流式 API 分块处理大文件，CLI 支持批量与目录转换

## 适用场景

- 为 RAG/AI 内容管线把混合格式文档统一转为 Markdown
- 批量转换目录中的 PDF/Office 文件供文档系统使用
- 离线转录音频文件生成文本（无需云 API）

## 场景标签

`文档解析` · 领域:知识与检索

## 证据(README 行号)

> L6: **.NET library that converts 15+ file formats to Markdown** for AI pipelines, documentation workflows, and developer
> L25: ElBruno.MarkItDotNet provides a unified interface to convert 15+ file formats into clean, structured Markdown. The 

## 星数曲线

```mermaid
xychart-beta
    title "elbruno/ElBruno.MarkItDotNet 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 55 --> 57
    line [56, 56]
```

2026-10-18 56 → 2026-10-25 56（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `275a0ee4bfdc` · [字段定义](../../DATASET.md)*
