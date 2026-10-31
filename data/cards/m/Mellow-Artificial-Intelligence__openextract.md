# Mellow-Artificial-Intelligence/openextract

⭐ 18 · Python · MIT · 推送 2026-10-25 · [GitHub](https://github.com/Mellow-Artificial-Intelligence/openextract) · [官网](https://mellow-artificial-intelligence.github.io/openextract/) · 组织维护

**Python 库：用 LLM 从文档/图像/音视频中抽取结构化数据**

提供单一 extract/extract_async 函数：输入 Pydantic schema、模型字符串与文件源（路径、URL 或 bytes），返回经校验的实例。媒体类型按扩展名、Content-Type 与文件首字节自动推断，支持 PDF、PNG/JPEG/GIF/WebP、MP3/WAV/FLAC/OGG、MP4 与 UTF-8 文本。模型通过 pydantic-ai 字符串接入 OpenAI/Anthropic/Google/Ollama 等，需 Python 3.12+ 与对应 API key；另有仅限 bool/Literal/Enum 字段的决策模型通道（OpenAI Decisions/OpenRouter），不支持 PDF、音视频与自由文本字段。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一 extract 函数：schema + 模型 + 文件 → 校验后的 Pydantic 实例
- 媒体类型三级自动推断（扩展名/Content-Type/首字节）
- 支持本地路径、URL、bytes 多种文件源
- 决策模型通道支持 1–400 个 bool/Literal/Enum 字段的确定性判定

## 适用场景

- 从发票、收据等 PDF 中抽取结构化字段
- 对图像或音视频文件做字段化数据提取
- 用布尔/枚举 schema 对文档做分类与判定

## 场景标签

`文档解析` · 领域:知识与检索

## 证据(README 行号)

> L3: **Extract structured data from documents, images, audio, and video using LLMs.**
> L12: One function: give it a Pydantic schema, a model, and a file. You get back a validated instance.

## 星数曲线

```mermaid
xychart-beta
    title "Mellow-Artificial-Intelligence/openextract 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `4e755dcfa9ed` · [字段定义](../../DATASET.md)*
