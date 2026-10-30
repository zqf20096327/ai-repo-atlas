# realspqrk/autorename-pdf

⭐ 123 · Python · MIT · 推送 2026-09-10 · [GitHub](https://github.com/realspqrk/autorename-pdf) · 个人维护

**用 LLM 按内容批量重命名发票与论文 PDF 的工具**

面向需要整理发票、扫描件和学术论文的用户，提供 Windows 拖放 GUI、Explorer 右键菜单和跨平台 Python CLI 三种入口，按 Business/Academic/德国 ER-AR 三种预设模板将 PDF 内容生成为规范文件名（日期、交易方、AP/AR、总额或作者、期刊、标题）。文本提取默认走 pdfplumber，扫描件可启用 PaddleOCR 或 vision。支持 OpenAI、Anthropic、Gemini、xAI 云端模型及 Ollama 本地离线方案；GUI 与右键菜单仅限 Windows，macOS/Linux 只有 CLI。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三种预设档案（business/academic/ER-AR）生成结构化文件名
- 支持 OpenAI/Anthropic/Gemini/xAI 云端及 Ollama 本地离线（含 OCR）
- 预览、dry-run 与按批次撤销重命名
- Jaro-Winkler 模糊匹配统一供应商名称别名

## 适用场景

- 把成堆的电子/扫描发票批量重命名为统一记账格式
- 整理论文 PDF 为 日期-作者-期刊-标题 命名
- 离线环境用 Ollama+PaddleOCR 完成重命名，不出网、无 API 费用

## 场景标签

`文档解析` · 领域:知识与检索

## 证据(README 行号)

> L2:  AI PDF renamer for invoices, scanned documents, and academic papers.
> L18: Use OpenAI, Anthropic (Claude), Google Gemini, xAI (Grok), or a local LLM through Ollama. Text extraction, PaddleOC
> L52: **Digital, scanned, and image PDFs?** Yes. pdfplumber always runs. Turn on `pdf.ocr` and/or `pdf.vision` (`false` /

## 星数曲线

```mermaid
xychart-beta
    title "realspqrk/autorename-pdf 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-29", "2026-10-30"]
    y-axis "stars" 121 --> 124
    line [122, 123, 123]
```

2026-10-18 122 → 2026-10-30 123（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `68e5cce68a41` · [字段定义](../../DATASET.md)*
