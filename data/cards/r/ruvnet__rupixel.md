# ruvnet/rupixel

⭐ 45 · Rust · MIT · 推送 2026-06-26 · [GitHub](https://github.com/ruvnet/rupixel) · 个人维护 · 中文 README

**面向开发者的像素级视觉 RAG 检索引擎（Rust 版 PixelRAG）**

用 Rust 在 ruvector（HNSW + IVF-Flat）向量引擎之上重建 PixelRAG 的文档检索工具：把每页文档渲染为截图后用 CLIP 生成视觉嵌入，或用 MiniLM 做文本嵌入，在浏览器或 CLI 中按语义检索页面；另提供实时视频关键帧搜索与可选的视觉 LLM 字幕（Qwen3-VL，经 OpenRouter 自带 key）。管线拆为 pixelrag-core/encoder/cli 三个 Rust 包，模型经 Node.js sidecar 在 CPU 上运行。README 自述为早期阶段，更强视觉模型（ColPali/Qwen3-VL）与更难测试集列为未完成项；Rust 代码需从 ruvector checkout 自行编译。

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

- 截图→CLIP 嵌入的 OCR-free 视觉文档检索
- 基于 ruvector 的 HNSW 与 IVF-Flat 双索引可切换
- 浏览器内全离线运行（transformers.js，WebGPU/WASM 回退）
- 实时视频关键帧搜索与可选流式视觉字幕（Qwen3-VL）

## 适用场景

- 在扫描件、图表、截图等文本搜索覆盖不了的文档里按语义找页面
- 浏览器内无服务器做文本/视觉双路语义检索
- 为 RAG 系统提供检索（find）半部分的管线与基准

## 场景标签

`RAG` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L85: > **"RAG"?** It stands for *Retrieval-Augmented Generation*: first **find** the
> L145: The pipeline is simple: **turn each page into numbers → store them → find the

## 星数曲线

```mermaid
xychart-beta
    title "ruvnet/rupixel 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 43 --> 46
    line [44, 45]
```

2026-10-18 44 → 2026-10-25 45（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `30c40521fed9` · [字段定义](../../DATASET.md)*
