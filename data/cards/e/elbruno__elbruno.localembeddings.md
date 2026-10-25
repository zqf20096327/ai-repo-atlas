# elbruno/elbruno.localembeddings

⭐ 42 · C# · MIT · 推送 2026-10-25 · [GitHub](https://github.com/elbruno/elbruno.localembeddings) · 个人维护

**.NET 本地文本嵌入生成库，基于 ONNX Runtime 离线运行**

面向 .NET 开发者的本地嵌入生成库：通过 ONNX Runtime 在本机运行推理生成文本与图像嵌入，无需外部 API 调用。实现 Microsoft.Extensions.AI 的 IEmbeddingGenerator 接口，支持 HuggingFace sentence-transformer 模型、Microsoft Harrier-OSS-v1、Google EmbeddingGemma 2（仅文本）及 CLIP 图像嵌入，模型自动下载缓存。提供 Kernel Memory、VectorData、Blazor 组件等伴随包及 NPU 加速包（DirectML/OpenVINO/QNN）。要求 .NET 8.0 或 10.0 SDK。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ONNX Runtime 本机推理，实现 IEmbeddingGenerator 接口
- 支持 HuggingFace、Harrier、EmbeddingGemma 2、CLIP 等多种模型
- 内置内存向量存储与余弦相似度/语义搜索辅助 API
- 提供 Kernel Memory / VectorData / Blazor 组件及 NPU 加速伴随包

## 适用场景

- 在 .NET 应用中离线生成文本嵌入构建 RAG
- 本地语义搜索与相似度比较
- 为 Kernel Memory 或 VectorData 管道提供本地嵌入后端

## 场景标签

`RAG` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L10: A .NET library for generating text embeddings locally using ONNX Runtime and Microsoft.Extensions.AI abstractions —
> L22: - **Local Embedding Generation** — Run inference entirely on your machine using ONNX Runtime

## 星数曲线

```mermaid
xychart-beta
    title "elbruno/elbruno.localembeddings 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-25 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `0df073162068` · [字段定义](../../DATASET.md)*
