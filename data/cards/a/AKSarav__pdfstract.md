# AKSarav/pdfstract

⭐ 155 · Python · Apache-2.0 · 推送 2026-03-18 · [GitHub](https://github.com/AKSarav/pdfstract) · [官网](https://pdfstract.com) · 个人维护

**面向 RAG 流水线的 PDF 抽取/分块/嵌入统一层**

为 RAG 数据准备阶段提供统一 API 的 Python 库：将 10+ 种 PDF 抽取库（Docling、Marker、PyMuPDF4LLM、PaddleOCR、Unstructured 等）、10+ 种分块方法（token、semantic、recursive、code 等）与多种嵌入提供方（OpenAI、Azure、Google、Ollama、Sentence Transformers）聚合在单一接口下，通过参数切换组件。安装分 Base/Standard/Advanced/All 四档可选依赖，同时提供 CLI（convert-chunk-embed 一条命令跑完流水线）、Web UI 与 API，Web UI 需 git clone 后 make up 启动。面向构建 RAG 系统与文档智能流水线的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一 API 切换 10+ 抽取库、10+ 分块方法与多种嵌入提供方
- CLI 单命令完成 convert-chunk-embed 全流水线
- 分档可选依赖安装（Base/Standard/Advanced/All）
- 附带 Web UI（localhost:3000）与 API（localhost:8000）

## 适用场景

- 为 RAG 系统准备文档数据（抽取、分块、嵌入）
- 对比不同抽取库与分块策略的效果
- 构建文档智能或语义搜索流水线
- 准备 LLM 微调数据集

## 场景标签

`RAG` `文档解析` · 领域:知识与检索

## 证据(README 行号)

> L5: **One unified API.** Switch between 10+ extraction libraries, 10+ chunking methods, and multiple embedding providers
> L38: - **Extract**: 10+ libraries (Marker, Docling, PyMuPDF4LLM, PaddleOCR, Unstructured, and more)
> L40: - **Embed**: Multiple providers (OpenAI, Azure, Google, Ollama, Sentence Transformers)

## 星数曲线

```mermaid
xychart-beta
    title "AKSarav/pdfstract 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 154 --> 156
    line [155, 155]
```

2026-10-18 155 → 2026-10-25 155（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `125c4cfee70c` · [字段定义](../../DATASET.md)*
