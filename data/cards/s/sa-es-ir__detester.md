# sa-es-ir/detester

⭐ 28 · C# · MIT · 推送 2026-06-03 · [GitHub](https://github.com/sa-es-ir/detester) · 个人维护

**.NET 库：为 AI 应用编写确定性测试**

构建于 Microsoft.Extensions.AI 抽象之上的 .NET 测试库，提供流式 Builder API 对任意 IChatClient 实现（OpenAI、Azure OpenAI、Ollama 等）的 AI 响应做断言：文本包含与 OR 断言、函数/工具调用与参数核验、JSON 响应反序列化与类型安全校验。针对 LLM 非确定性提供 AssertReliablyAsync 多次运行并断言最低通过率，另支持延迟与 token 用量断言。通过 NuGet 以 dotnet add package 安装，失败时抛出 DetesterException 并附带细节。

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

- 流式 Builder API 链式组合多提示词与断言
- 兼容任意 IChatClient 实现（OpenAI/Azure OpenAI/Ollama 等）
- AssertReliablyAsync 多次运行断言最低通过率以处理 LLM 非确定性
- JSON 反序列化校验、函数调用核验、延迟与 token 断言

## 适用场景

- 给集成了 LLM 的 .NET 应用写自动化测试
- 验证模型的函数调用与参数是否正确
- 评估模型响应在多次运行下的通过率与延迟/token 预算

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L6: Detester is a .NET library that enables you to write deterministic tests for AI-powered applications. It provides a 
> L19: - **Extensible**: Build on Microsoft.Extensions.AI abstractions for maximum flexibility

## 星数曲线

```mermaid
xychart-beta
    title "sa-es-ir/detester 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-30 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `0f1b78334048` · [字段定义](../../DATASET.md)*
