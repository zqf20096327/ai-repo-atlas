# AJ-comp/Mythosia.AI

⭐ 20 · C# · MIT · 推送 2026-10-16 · [GitHub](https://github.com/AJ-comp/Mythosia.AI) · 个人维护 · 中文 README

**.NET 统一多模型接入库：一套 API 调用各家 LLM 并附 RAG 扩展**

模块化 .NET AI 库，以统一 API 支持 OpenAI、Anthropic、Google、Grok、DeepSeek、Perplexity 等服务商的补全、流式、函数调用、结构化输出与图像生成/编辑；另提供可选 RAG 包（文本切分、嵌入、关键词/语义/混合检索、重排序、InMemory 向量存储及文档加载）与 Postgres/Qdrant/Pinecone 生产级向量库集成。请求设置独立可复用，含 Playground Chat UI 示例，通过 NuGet 分发，需 .NET 运行环境。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一 API 覆盖补全/流式/函数调用/结构化输出/图像生成
- 可选 RAG 包：混合检索、重排序、Word/Excel/PPT/PDF 加载
- Postgres/Qdrant/Pinecone 生产级向量存储可选集成
- 附带 Playground Chat UI 本地示例（dotnet run）

## 适用场景

- 在 .NET 应用中不换代码切换不同 LLM 服务商
- 基于自有文档（PDF/Word/Excel/PPT）构建检索问答
- 用强类型 POCO 直接反序列化模型结构化输出

## 场景标签

`模型网关` `RAG` `图像生成` · 领域:Agent 开发

## 证据(README 行号)

> L7: ### A modular .NET AI library for building intelligent applications.
> L44: - **Switch AI providers through one API** for chat, streaming, tool calls and structured responses.
> L52: dotnet add package Mythosia.AI                    # start here (this is all you need)

## 星数曲线

```mermaid
xychart-beta
    title "AJ-comp/Mythosia.AI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `2229912a1983` · [字段定义](../../DATASET.md)*
