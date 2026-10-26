# GregorBiswanger/SemanticChunker.NET

⭐ 43 · C# · Apache-2.0 · 推送 2026-02-09 · [GitHub](https://github.com/GregorBiswanger/SemanticChunker.NET) · 个人维护

**.NET 语义分块库：为 RAG 生成检索就绪的文本块**

面向 .NET 开发者的 C# 库，通过 CreateChunksAsync 一次调用将长文档切分为语义连贯、适配 LLM 上下文窗口的块，每块含 ID、文本与 embedding。基于 Microsoft.Extensions.AI 的 embedding 生成器，模型无关，兼容 Semantic Kernel。提供 Percentile/StandardDeviation/InterQuartile/Gradient 四种断点策略、跨句上下文缓冲窗口、目标块数、ICU4N 多语言（70+ 语言）分句与 token 上限 10% 安全边距。以 NuGet 包分发，作者为独立开发者（Microsoft MVP）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四种断点策略（Percentile/StandardDeviation/InterQuartile/Gradient）
- 兼容任意 Microsoft.Extensions.AI 支持的 embedding 生成器，无框架锁定
- ICU4N 支持 70+ 语言的句子边界切分
- targetChunkCount 选项可精确控制输出块数

## 适用场景

- 为 .NET RAG 流水线准备检索就绪的文本块
- 在 Semantic Kernel 应用中做文档预处理
- 针对特定语料按校准指南调参分块策略

## 场景标签

 · 领域:LLM 基础设施/RAG

## 证据(README 行号)

> L6: Transforms long texts into coherent, retrieval ready chunks with a single call - powered by embeddings and fully com
> L16: - **Model‑agnostic** – Works with any embedding generator supported by `Microsoft.Extensions.AI`; no framework lock

## 星数曲线

```mermaid
xychart-beta
    title "GregorBiswanger/SemanticChunker.NET 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-26"]
    y-axis "stars" 41 --> 44
    line [42, 43, 43]
```

2026-10-18 42 → 2026-10-26 43（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `0094c44076f0` · [字段定义](../../DATASET.md)*
