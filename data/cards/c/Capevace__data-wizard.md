# Capevace/data-wizard

⭐ 74 · JavaScript · AGPL-3.0 · 推送 2025-10-29 · [GitHub](https://github.com/Capevace/data-wizard) · [官网](https://docs.data-wizard.ai) · 个人维护

**用 LLM 从 PDF/Word/图片提取结构化 JSON 的自托管工具**

基于 Laravel 的自托管文档数据提取应用：用户用 JSON Schema 定义输出结构，选择 LLM（OpenAI/Anthropic/Gemini/Mistral，或经 Ollama/LMStudio/OpenRouter 接入本地及其他模型）与提取策略（Simple/Sequential/Parallel/Auto-Merging/Double-Pass/自定义），从 PDF（含扫描件 OCR）、DOCX、XLSX、图片等文件提取数据并按 Schema 校验后输出 JSON。可通过 iFrame/JS API 嵌入或 REST/GraphQL API 调用，Docker 部署。手动安装需 Laravel 环境、uv 与 LibreOffice。为 Leuphana 大学 2025 本科论文项目，AGPL-3.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- JSON Schema 定义结构，输出经 Schema 校验
- 多种提取策略（Simple/Sequential/Parallel/Auto-Merging/Double-Pass/自定义）
- 支持 PDF（含 OCR）、DOCX、XLSX、图片，并利用页面截图提供视觉上下文
- iFrame/JS API 嵌入或 REST/GraphQL API 编程调用，Docker 自托管

## 适用场景

- 把发票、收据、表单数据自动录入 ERP/财务系统
- 让 SaaS/CRM 用户上传文档智能导入数据
- 批量把 PDF/扫描件转为结构化 JSON/CSV
- 用其 API 作为自有文档处理平台的提取引擎

## 场景标签

`文档解析` · 领域:知识与检索

## 证据(README 行号)

> L3:  Extract Structured Data from Any Document with LLMs
> L40: 3. **Get Structured Data:** The chosen strategy directs the LLM interaction. The AI extracts the data, which is the

## 星数曲线

```mermaid
xychart-beta
    title "Capevace/data-wizard 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 73 --> 75
    line [74, 74]
```

2026-10-18 74 → 2026-10-24 74（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `57df00147fdf` · [字段定义](../../DATASET.md)*
