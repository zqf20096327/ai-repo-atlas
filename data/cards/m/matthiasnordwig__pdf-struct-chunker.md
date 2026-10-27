# matthiasnordwig/pdf-struct-chunker

⭐ 24 · Rust · MIT · 推送 2026-06-29 · [GitHub](https://github.com/matthiasnordwig/pdf-struct-chunker) · [官网](https://programmiere.de) · 个人维护

**纯 Rust 的无 LLM 版面感知 PDF 分块库，服务 RAG**

面向 RAG 管线的 PDF 分块工具：基于 pdf_oxide 提取字符级 X/Y 坐标与字体大小，重建行并按可配置的正则模式（或字体大小启发式回退）分类，生成带 section/heading/page 元数据的语义分块。无需 LLM、API 或网络，纯 CPU 运行，100 页 PDF 处理耗时声明低于 1 秒。提供 CLI 与 Rust 库 API，支持自定义 JSON 正则 profile（heading_l1/definition/ignore 三种角色），内置默认规则面向法律与法规类文档。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 X/Y 坐标与字体大小的版面分析，无需 LLM 与 API，可离线运行
- 每个分块携带 section/heading/page 结构化元数据
- 可配置 JSON 正则 profile，内置面向法律/法规文档的默认规则
- 纯内存处理，提供 CLI 与 Rust 库两种使用方式

## 适用场景

- RAG 管线中按文档结构切分 PDF 以保留上下文
- 法规类文档按条款（§/Article/Chapter）分块后做向量检索
- 离线/边缘环境处理 PDF 而不依赖外部 API

## 场景标签

`文档解析` · 领域:知识与检索

## 证据(README 行号)

> L8: **Split PDFs into semantically meaningful chunks — without LLMs, without APIs, without cloud dependencies.**
> L18: **pdf-struct-chunker** solves this by analyzing the actual *layout* of a PDF: X/Y coordinates, font sizes, and bold

## 星数曲线

```mermaid
xychart-beta
    title "matthiasnordwig/pdf-struct-chunker 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-27 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `59441328482c` · [字段定义](../../DATASET.md)*
