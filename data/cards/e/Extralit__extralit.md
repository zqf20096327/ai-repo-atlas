# Extralit/extralit

⭐ 48 · Python · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/Extralit/extralit) · [官网](https://extralit.ai/) · 组织维护

**LLM 辅助的科学文献结构化数据提取与人机协同标注平台**

面向科研用户的数据提取工作流系统：基于 schema 定义从科学文献（含扫描版 PDF，AI 驱动 OCR 识别复杂表格）中提取结构化数据，内置数据校验、团队协同标注与人工反馈闭环，用于持续修正 LLM 输出并构建微调数据集。提供 Python SDK、CLI 与 Web UI（Vue 3/Nuxt 4），服务端为 FastAPI + PostgreSQL，向量库支持 ElasticSearch 与 AWS OpenSearch。基于 Argilla（Apache-2.0）代码库延续开发，起源于盖茨基金会疾病建模研究所。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Schema 驱动的科学文献结构化数据提取
- AI OCR 识别数字与扫描 PDF 中的复杂表格结构
- 内置校验与团队协同标注、人工反馈闭环
- 提供 Python SDK、CLI 与 Web UI 三种使用形态

## 适用场景

- 从大量科学论文中提取结构化证据数据
- 团队协同审核并校正 LLM 提取结果
- 积累人工标注构建模型微调数据集

## 场景标签

`科研工具` `文档解析` `OCR` · 领域:知识与检索

## 证据(README 行号)

> L9: Extralit (EXTRAct LITerature) is a data extraction workflow with user-friendly UI, designed for **LLM-assisted scien
> L19: - Schema-Driven Extraction – Define structured schemas for context-aware, high-accuracy data extraction across scie

## 星数曲线

```mermaid
xychart-beta
    title "Extralit/extralit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 47 --> 49
    line [48, 48]
```

2026-10-18 48 → 2026-10-30 48（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `ef402ead5c3a` · [字段定义](../../DATASET.md)*
