# yfedoseev/office_oxide

⭐ 155 · Rust · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/yfedoseev/office_oxide) · [官网](https://office.oxide.fyi) · 个人维护

**多语言 Office 文档解析库：6 种格式提取文本/Markdown**

以 Rust 为核心的 Office 文档处理库，提供 Python、Go、C#/.NET、Node.js（原生与 WASM）、C FFI 绑定及 CLI。支持 DOCX/XLSX/PPTX 读写编辑，DOC/XLS/PPT 旧格式可读取并转换为 OOXML，输出纯文本、Markdown、HTML 及格式无关中间表示。基准测试基于 6,062 个真实文档，对有效文件通过率 100%（97 个未通过文件均为无效输入）。渲染器对不可信输入设有每文档文本预算（默认 256 Mi 字符）并截断标注。另提供 MCP server 二进制，供 Claude、Cursor 等 AI 助手本地读取 Office 文档。MIT/Apache-2.0 双开源许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 6 种格式支持：DOCX/XLSX/PPTX 读写，DOC/XLS/PPT 读取并可转换为 OOXML
- 多语言绑定：Python/Go/C#/Node.js/WASM/C FFI，附 CLI 与 MCP server
- 对不可信输入设 256 Mi 字符文本预算并截断标注
- 基于 6,062 个真实文档的基准测试，有效文件通过率 100%

## 适用场景

- RAG/LLM 流水线中从 Office 文档提取干净文本或 Markdown
- 批量解析数千份文档做数据提取
- 将旧版 DOC/XLS/PPT 转换为现代 OOXML 格式
- 让 Claude/Cursor 等 AI 助手通过 MCP 本地读取 Office 文档

## 场景标签

`文档解析` · 领域:知识与检索

## 证据(README 行号)

> L1: # Office Oxide — The Fastest Native Office Document Library
> L335: `office-oxide-mcp` lets AI assistants (Claude, Cursor, etc.) read Office documents locally via the Model Context P
> L373: - **RAG / LLM pipelines** — Extract clean text or Markdown from Office documents for retrieval-augmented generatio

## 星数曲线

```mermaid
xychart-beta
    title "yfedoseev/office_oxide 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-26"]
    y-axis "stars" 153 --> 156
    line [154, 155, 155]
```

2026-10-18 154 → 2026-10-26 155（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `dc42a4cc430c` · [字段定义](../../DATASET.md)*
