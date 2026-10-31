# PSPDFKit-labs/nutrient-skills

⭐ 18 · Python · 推送 2026-10-19 · [GitHub](https://github.com/PSPDFKit-labs/nutrient-skills) · [官网](https://www.nutrient.io/) · 组织维护

**面向 AI agent 的 Nutrient 文档处理技能包：转换/OCR/解析 PDF**

Nutrient（原 PSPDFKit）官方实验室维护的 agent 技能仓库：提供十余个 SKILL.md 技能，让 Claude Code、Codex、Cursor、Gemini CLI、Pi 等 agent 通过本地 Nutrient CLI 调用文档 API，覆盖 PDF 转换、OCR、结构化提取、PDF/UA 修复、PDF 生成、带溯源信息的 RAG 分块及查看器会话等。标准转换免费无需账号；Vision 模式需账号/API key/许可证。CLI 在本地处理文件，不上传文档内容，运行于 macOS 13+/Apple Silicon、glibc 2.38+ Linux 与 Windows。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 十余个文档处理技能：转换、OCR、提取、签名、修复、PDF 生成
- grounded-rag-ingestion 技能输出带页码/bbox/置信度的 JSONL 分块
- 标准转换免费且 CLI 本地处理，不上传 PDF 内容
- 支持 npx skills、插件市场、Codex MCP、Pi 等多种安装方式

## 适用场景

- 让 Claude Code/Codex 等 agent 在本机完成 PDF 转换与 OCR
- 为 RAG 管道生成可溯源的结构化文档分块
- 用 agent 生成符合 PDF/UA、PDF/A 标准的 PDF

## 场景标签

`RAG` `OCR` `文档解析` · 领域:知识与检索

## 证据(README 行号)

> L3: AI agent skills for Nutrient APIs and SDKs. Works with Claude Code, Codex, Pi, Cursor, Gemini CLI, and other agents.
> L24: |`nutrient-dws-mcp`|`nutrient-dws-mcp`|MCP-only Codex plugin for converting, OCRing, signing, redacting, parsing, a
> L44: npx skills add pspdfkit-labs/nutrient-skills --skill document-processor-api

## 星数曲线

```mermaid
xychart-beta
    title "PSPDFKit-labs/nutrient-skills 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `fbbed6dff8b0` · [字段定义](../../DATASET.md)*
