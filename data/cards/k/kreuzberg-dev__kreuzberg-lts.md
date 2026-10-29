# kreuzberg-dev/kreuzberg-lts

⭐ 18 · Rust · MIT · 推送 2026-10-16 · [GitHub](https://github.com/kreuzberg-dev/kreuzberg-lts) · [官网](https://kreuzberg.dev) · 组织维护

**多语言文档文本提取库：97+格式解析、OCR 与代码结构分析**

Rust 核心的文档解析库，从 PDF、Office、图像、HTML、邮件、归档、学术格式等 91+ 格式中提取文本、元数据与表格，并通过 tree-sitter 对 248 种编程语言抽取函数/类/导入等代码结构与语义分块。OCR 支持 Tesseract、PaddleOCR、EasyOCR 与 VLM OCR，另提供跨 146 个 LLM 提供商的 JSON 抽取与嵌入接口（via liter-llm）。以 11 种语言绑定、CLI、REST API、Docker 及 MCP server 形式发布。本仓库为 v4 LTS 长期支持线，新功能已移至后继项目 Xberg，仅提供缺陷与安全修复至 2026 年底。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 91+ 文件格式文本/元数据提取，8 大类别
- tree-sitter 支持 248 种语言的代码结构与语义分块
- Tesseract/PaddleOCR/EasyOCR/VLM 四类 OCR 后端，插件 API 可扩展
- Rust/Python/Node/Go/Java/C# 等 11 种语言绑定，预编译二进制覆盖 x86_64 与 aarch64

## 适用场景

- 为 RAG 管线批量解析 PDF、Office 等文档为 Markdown
- 提取源码中的函数、类与文档字符串做代码分析
- 通过 CLI、REST API 或 Docker 部署文档提取服务

## 场景标签

`文档解析` `OCR` · 领域:知识与检索

## 证据(README 行号)

> L70: Extract text, metadata, and code intelligence from 97+ file formats and 300+ programming languages at native speeds
> L74: - **Code intelligence** – Functions, classes, imports, symbols, and docstrings from 248 programming languages via t
> L77: - **LLM intelligence** – VLM OCR, schema-constrained JSON extraction, and provider-hosted embeddings across 146 LLM
> L115: - **Docker** – Official images with API, CLI, and MCP server modes (Core: ~1.0-1.3GB, Full: ~1.0-1.3GB with OCR + 

## 星数曲线

```mermaid
xychart-beta
    title "kreuzberg-dev/kreuzberg-lts 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `7a40d1d6daaf` · [字段定义](../../DATASET.md)*
