# DemoMacro/office-open

⭐ 38 · TypeScript · MIT · 推送 2026-10-26 · [GitHub](https://github.com/DemoMacro/office-open) · [官网](https://www.office-open.com/) · 个人维护 · 中文 README

**面向 AI agent 的 Office 文档生成/解析/修补 TypeScript 库**

TypeScript/JavaScript 库集合，从纯 JSON 或全类型 API 生成 Word/Excel/PowerPoint、RTF 与 OpenDocument 文件，也可解析与修补 .docx/.xlsx/.pptx 及旧版 .doc/.xls/.ppt，无需安装 Microsoft Office。为 AI agent 与 LLM tool-calling 提供四种接入方式：Vercel AI SDK 工具定义、MCP server、可安装 Agent Skill、按需切片的 Draft-07 JSON Schema。实现覆盖 21 个 OOXML Transitional schema 的 2,273 个元素。主要版本仍为 0.x，API 会随 minor 版本变更。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 生成/解析/修补 .docx/.xlsx/.pptx，并读取旧版 .doc/.xls/.ppt、RTF、ODF
- 四种 AI 接入方式：Vercel AI SDK 工具、MCP server、Agent Skill、按上下文预算切片的 JSON Schema
- 声称覆盖全部 21 个 OOXML Transitional schema 的 2,273 元素与 1,969 属性，经 XSD 覆盖工具验证
- 跨 Node.js、浏览器、Deno、Bun 运行，无需服务器、可离线使用

## 适用场景

- 让 LLM agent 通过 tool-calling 生成规范的 Word/Excel/PowerPoint 文件
- 读取既有 Office 文档做往返编辑或按占位符修补模板
- 在无 Microsoft Office 的服务端或浏览器环境生成文档

## 场景标签

`文档解析` · 领域:知识与检索

## 证据(README 行号)

> L25: - 🤖 **AI Tooling** — Draft-07 JSON Schemas frozen from the TypeScript API, on-demand schema slicing for LLM context
> L127: Give AI agents first-class Office document abilities — four ways, no glue code:

## 星数曲线

```mermaid
xychart-beta
    title "DemoMacro/office-open 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-27 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `fbce48e7aa73` · [字段定义](../../DATASET.md)*
