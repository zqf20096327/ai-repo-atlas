# phanxuanquang/EmbeddingGemma.NET

⭐ 15 · C# · 推送 2026-04-04 · [GitHub](https://github.com/phanxuanquang/EmbeddingGemma.NET) · [官网](https://www.nuget.org/packages/EmbeddingGemma.NET) · 个人维护

**.NET 库：本地离线运行 EmbeddingGemma-300m 生成文本嵌入**

为 Google DeepMind 的 EmbeddingGemma-300m 提供 .NET 绑定，通过 ONNX Runtime 在本地离线推理生成文本嵌入，无需 API key 与云服务，支持 100+ 语言。以单个 NuGet 包提供，同时兼容 IServiceCollection（ASP.NET Core/通用主机）与 Microsoft Semantic Kernel 的 IKernelBuilder；内置 15 种任务类型自动附加对应 prompt 前缀。需先手动下载或用脚本拉取 Hugging Face 上的 ONNX 模型与 tokenizer 文件（约 1.23 GB）。仓库另含一个演示本地语义搜索浏览器历史的 Windows 应用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 ONNX Runtime 的完全本地嵌入生成，无 API key、无数据外传
- 同时支持 IServiceCollection 与 Semantic Kernel IKernelBuilder 注册
- 15 种内置任务类型自动附加 prompt 前缀
- 可在无 GPU、4 GB 内存的低端设备上运行

## 适用场景

- 在 .NET/RAG 项目中本地生成查询与文档嵌入
- 构建无云端依赖、保护隐私的语义搜索
- 为 Semantic Kernel 流水线接入本地嵌入服务

## 场景标签

 · 领域:LLM 基础设施/嵌入模型

## 证据(README 行号)

> L7: **EmbeddingGemma.NET** provides .NET bindings for Google DeepMind's EmbeddingGemma-300m model, enabling fully local,
> L87: Resolve `IEmbeddingGenerator<string, Embedding<float>>` from the DI container and call `GenerateAsync`.

## 星数曲线

```mermaid
xychart-beta
    title "phanxuanquang/EmbeddingGemma.NET 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `2cf08a146920` · [字段定义](../../DATASET.md)*
