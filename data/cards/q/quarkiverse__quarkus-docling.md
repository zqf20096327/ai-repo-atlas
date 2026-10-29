# quarkiverse/quarkus-docling

⭐ 22 · Java · Apache-2.0 · 推送 2026-10-22 · [GitHub](https://github.com/quarkiverse/quarkus-docling) · [官网](https://docs.quarkiverse.io/quarkus-docling/dev) · 组织维护

**Quarkus 的 Docling 文档解析扩展，接入 RAG 数据摄取**

Quarkiverse 维护的 Quarkus 扩展，封装 Docling Java 项目，通过 REST API 与 Docling Serve 实例通信，将 Docling 的多格式文档解析能力（PDF/DOCX/HTML/图片、OCR、表格结构等）引入 Quarkus 应用；同时提供 Dev Service 与 Dev UI 集成。README 声明目标是把 DoclingDocument 格式与 LangChain4j 的 Document 抽象统一，使 Docling 可用于 LangChain4j RAG 管道的数据摄取。面向 Java/Quarkus 开发者，依赖外部 Docling Serve 实例运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 封装 docling-java，经 REST API 与 Docling Serve 通信
- 提供 Dev Service 与 Dev UI 集成
- 目标对接 LangChain4j Document 抽象以用于 RAG 摄取

## 适用场景

- 在 Quarkus 应用中解析 PDF/DOCX 等文档用于 RAG 数据摄取
- 开发期通过 Dev Service 快速启动 Docling 实例调试文档解析

## 场景标签

`文档解析` · 领域:知识与检索

## 证据(README 行号)

> L27: Currently, this extension is a set of wrappers around the Docling Java project, which communicates with a Docling S
> L29: The eventual goal is to unify the [DoclingDocument][docling_document] format with LangChain4j's `Document` abstract

## 星数曲线

```mermaid
xychart-beta
    title "quarkiverse/quarkus-docling 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-29 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `d57fe0676147` · [字段定义](../../DATASET.md)*
