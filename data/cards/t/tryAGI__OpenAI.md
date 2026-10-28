# tryAGI/OpenAI

⭐ 37 · C# · MIT · 推送 2026-10-27 · [GitHub](https://github.com/tryAGI/OpenAI) · [官网](https://tryagi.github.io/OpenAI/) · 组织维护

**基于官方 OpenAPI 规范生成的 OpenAI C#/.NET SDK**

由 AutoSDK 从 OpenAI 官方 OpenAPI 规范自动生成的 C# SDK，覆盖全部 OpenAI API 端点（chat、embeddings、图像、语音、moderation 等），支持 .NET Framework/.NET Standard 2.0、nullability、trimming 与 NativeAOT。实现 Microsoft.Extensions.AI 的 IChatClient 与 IEmbeddingGenerator 接口，附别名路由 chat client 与 429 冷却跟踪；定期测试与 OpenRouter/DeepSeek/Ollama/LM Studio 等自定义 provider 的兼容性；仓库内含 FreeLLM 独立包做免费优先路由。以 NuGet 包分发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从官方 OpenAPI 规范全量生成，新特性当日更新
- 原生实现 Microsoft.Extensions.AI IChatClient / IEmbeddingGenerator
- CustomProviders 支持 GitHub Models、Inception Mercury 3 等自定义端点
- FreeLLM 包跨 OpenAI 兼容 provider 与 Gemini 做路由

## 适用场景

- 在 .NET 项目中调用 OpenAI 的 chat/embeddings/图像/语音等 API
- 通过统一 IChatClient 接口接入 40+ provider
- 在 OpenRouter/DeepSeek/Ollama 等 OpenAI 兼容端点间做别名路由与降级

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L9: - Fully generated C# SDK based on official OpenAI OpenAPI specification using AutoSDK
> L19: - Microsoft.Extensions.AI `IChatClient` and `IEmbeddingGenerator` support for OpenAI and all CustomProviders
> L117: The client natively implements `IChatClient` and `IEmbeddingGenerator<string, Embedding<float>>` from Microsoft.Ex

## 星数曲线

```mermaid
xychart-beta
    title "tryAGI/OpenAI 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-28"]
    y-axis "stars" 35 --> 38
    line [36, 37, 37]
```

2026-10-18 36 → 2026-10-28 37（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `d0d0913a03aa` · [字段定义](../../DATASET.md)*
