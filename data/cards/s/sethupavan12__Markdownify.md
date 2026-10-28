# sethupavan12/Markdownify

⭐ 21 · Python · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/sethupavan12/Markdownify) · [官网](https://clickpy.clickhouse.com/dashboard/llm-markdownify) · 个人维护

**用视觉 LLM 把 PDF/扫描件/图片转成 Markdown 的工具库**

面向 RAG 数据摄取管线的文档转换 Python 库：把 PDF、扫描件和图片逐页交给视觉 LLM，输出保留阅读顺序、去除页眉页脚、含 LaTeX 公式与 Markdown/HTML 表格的文本，并支持跨页表格拼接、图表数据描述与手写转录。经 LiteLLM 支持百余家模型提供方（OpenAI、Anthropic、Gemini、DeepSeek 等）及 Ollama/vLLM 等本地端点，提供 CLI、Python API、异步接口、MCP server 与批量模式。失败页可标记跳过，结果按页缓存于磁盘。

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

- 逐页送视觉 LLM，保留阅读顺序、去页眉页脚、LaTeX 公式与跨页表格拼接
- 经 LiteLLM 支持 100+ 提供方及 Ollama/LM Studio/vLLM/llama.cpp 本地端点
- 提供 CLI、Python/异步 API、MCP server（document_info/convert_document 两工具）
- 磁盘缓存按页去重，失败页以 HTML 注释标记并列入 failed_pages

## 适用场景

- 为 RAG 管线把 PDF 与扫描文档转成干净 Markdown
- 通过 MCP 让 Claude Code/Cursor 等 agent 直接调用文档转换
- 用本地视觉模型离线批量转换大量文档

## 场景标签

`文档解析` · 领域:知识与检索

## 证据(README 行号)

> L7: Turn PDFs, scans and images into clean Markdown with the vision model you already pay for.
> L15: Each page goes to a vision LLM with a prompt we measure on a public benchmark, so the Markdown comes
> L26: It works with any provider: OpenAI, Anthropic, Gemini, DeepSeek, Azure, OpenRouter, or a model running

## 星数曲线

```mermaid
xychart-beta
    title "sethupavan12/Markdownify 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `a734754eff8a` · [字段定义](../../DATASET.md)*
