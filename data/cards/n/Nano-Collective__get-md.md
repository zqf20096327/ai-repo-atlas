# Nano-Collective/get-md

⭐ 96 · TypeScript · NOASSERTION · 推送 2026-10-27 · [GitHub](https://github.com/Nano-Collective/get-md) · [官网](https://docs.nanocollective.org/get-md/) · 组织维护

**HTML/PDF/DOCX 转 Markdown 库，为 LLM 输入优化**

面向 LLM 数据准备的格式转换工具：读取 HTML、PDF、DOCX、Markdown 文件或 URL，输出结构化 Markdown，提供 npm 库 API 与 npx CLI 两种用法。核心机制包括内容抽取与噪声过滤、Mermaid 图表四层处理（保留/恢复/重建/校验），其中图表重建可选用远程视觉模型，另支持可选的本地 LLM 增强转换（文档位于 docs.nanocollective.org，含 React Native 指南）。由社区集体 Nano Collective 维护。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- HTML/PDF/DOCX/Markdown/URL 转 Markdown，库与 CLI 两种形式
- Mermaid 图表保留、SVG 恢复、视觉模型重建、语法校验四种处理方式
- 可选本地 LLM 驱动的 AI 转换模式
- Mermaid 校验与 PDF 图表重建为可选功能，需额外依赖

## 适用场景

- 把网页或文档转成干净 Markdown 喂给 LLM
- 构建 RAG 数据管道时批量预处理文档
- 在转换中保留并校验 Mermaid 图表

## 场景标签

`文档解析` · 领域:知识与检索

## 证据(README 行号)

> L3: A fast, lightweight HTML, PDF, DOCX, and Markdown to Markdown converter optimized for LLM consumption — built by the
> L5: Lightning-fast (<100ms) with optional AI-powered conversion using a local LLM model. Pass in HTML, PDF, DOCX, Markdo

## 星数曲线

```mermaid
xychart-beta
    title "Nano-Collective/get-md 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-28"]
    y-axis "stars" 94 --> 97
    line [95, 96, 96]
```

2026-10-18 95 → 2026-10-28 96（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `0b5475c760de` · [字段定义](../../DATASET.md)*
