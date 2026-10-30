# jolibrain/colette

⭐ 302 · HTML · NOASSERTION · 推送 2026-10-01 · [GitHub](https://github.com/jolibrain/colette) · [官网](https://www.colette.chat) · 组织维护

**自托管多模态 RAG 软件：本地检索与问答技术文档**

面向不便于将文档发送到外部 API 的场景，提供开源自托管的 RAG 与 LLM 服务软件。核心机制为 Vision-RAG（V-RAG）：将文档页面作为图像处理，保留表格、图表与版式，配合视觉嵌入模型（如 gme-Qwen2-VL）与 VLM（如 Qwen3-VL）；检索支持向量+BM25 混合检索与可选 HyDE。推理后端支持 huggingface、vllm、ollama 等。默认配置需 24GB VRAM GPU，通过 Docker 部署，另提供 CLI、Python API 与示例 Notebook。由 Jolibrain、CNES 与 Airbus 共同资助。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `gpu-24g` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Vision-RAG 将文档页面按图像处理，保留表格/图表/版式
- 向量嵌入 + BM25（Tantivy）混合检索，支持 HyDE
- 多推理后端：huggingface / vllm / ollama / vllm_client
- Docker 部署，提供 CLI、Python API 与调试 Notebook

## 适用场景

- 在本地对不可外泄的技术文档做检索与问答
- 对含大量图表与产品编号的技术文档库进行多模态检索
- 自建多模态 RAG 服务并按 JSON 配置定制检索策略

## 场景标签

`RAG` `文档问答` `多模态` · 领域:知识与检索

## 证据(README 行号)

> L9: Colette is an open-source self-hosted RAG and LLM serving software. It is well-suited for searching and interacting 
> L11: As the main core feature, Colette embeds a Vision-RAG (V-RAG) that transforms and analyzes all documents as images.
> L21: - 📊 **Vision RAG (V-RAG)** — treats every document page as an image; preserves tables, figures, diagrams and spatia

## 星数曲线

```mermaid
xychart-beta
    title "jolibrain/colette 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 300 --> 303
    line [301, 302, 302]
```

2026-10-18 301 → 2026-10-30 302（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `209a274f7657` · [字段定义](../../DATASET.md)*
