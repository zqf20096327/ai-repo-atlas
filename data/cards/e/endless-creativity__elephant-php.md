# endless-creativity/elephant-php

⭐ 14 · PHP · NOASSERTION · 推送 2026-10-15 · [GitHub](https://github.com/endless-creativity/elephant-php) · 个人维护

**纯 PHP 的 .docx 转 Markdown/语义 HTML 转换库，供 RAG/索引管线用**

以标准 PHP 扩展（dom/libxml/mbstring/xmlreader/zip）实现的 .docx 文档转换库，无 LibreOffice/Pandoc/PHPWord 依赖，无 shell 调用。读取文档结构（标题、列表、表格、脚注、图片等）并输出 HTML 或 Markdown，二者共享同一中间模型；提供 extractRawText 纯文本输出面向索引/搜索管线。它是 mammoth.js 的独立 PHP 移植，采用其 style-mapping DSL；针对不可信输入设有默认安全行为（拒绝 DOCTYPE、不加载 r:link 图片、剥离危险协议链接）。需 PHP 8.2+，经 Composer 安装，附 CLI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 同一中间模型输出 HTML 与 Markdown，extractRawText 供索引/搜索管线使用
- 纯 PHP 实现，仅依赖标准扩展，无外部二进制
- Mammoth 兼容的 style-mapping DSL 与文档内嵌样式图读写
- 对不可信 .docx 输入的默认安全策略（XXE/SSRF/危险协议链接防护）

## 适用场景

- RAG 管线中把 Word 文档转成 Markdown 或纯文本入库
- 把用户上传的 .docx 安全地转为语义 HTML
- 用自定义样式映射规则定制转换输出

## 场景标签

`文档解析` · 领域:知识与检索

## 证据(README 行号)

> L51: - `extractRawText` for plain-text indexing pipelines.
> L94: // Paragraphs are separated by "\n\n", everything else just contributes
> L95: // its descendant text. Useful for indexing/search pipelines.

## 星数曲线

```mermaid
xychart-beta
    title "endless-creativity/elephant-php 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `be29d476dcd3` · [字段定义](../../DATASET.md)*
