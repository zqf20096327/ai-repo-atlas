# laurentkempe/aiPlayground

⭐ 83 · C# · 推送 2026-04-30 · [GitHub](https://github.com/laurentkempe/aiPlayground) · [官网](https://laurentkempe.com/) · 个人维护

**.NET/C# AI 实验项目集合：MCP 服务端与本地 LLM 工具调用示例**

个人学习性质的 .NET C# AI 实验代码合集：包含多个基于 modelcontextprotocol/csharp-sdk 的 MCP Server/Client 示例（SSE 传输、AOT 发布为单个 Windows exe、Docker 镜像发布）、Microsoft.Extensions.AI 与 Semantic Kernel 配合 Ollama 运行本地 SLM（phi4、llama3.2、Phi-3、DeepSeek-R1 蒸馏版）的 Agent 与工具/函数调用示例，以及 Blazor 网页应用与本地 LLM 文章摘要应用。面向想在 .NET 技术栈中接入本地模型的开发者参考学习。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多个基于 csharp-sdk 的 MCP Server/Client 示例（SSE 传输、AOT 单文件 exe）
- Semantic Kernel Agent 配合 Ollama 运行本地 SLM（phi4/llama3.2）
- AI 工具/函数调用示例（Microsoft.Extensions.AI、源码生成器标注、OpenAPI 插件）
- .NET Aspire + Ollama 本地运行 DeepSeek-R1 蒸馏模型

## 适用场景

- 参考示例学习在 C# 中构建 MCP Server 与 Client
- 了解 Semantic Kernel / Microsoft.Extensions.AI 接入 Ollama 本地模型的方式
- 学习 AI 工具/函数调用的实现方法

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L7: - MCPSSEServer Simple .NET C# MCP Server using SSE transport using modelcontextprotocol / csharp-sdk published using
> L9: - MCPServer Two simple console applications using modelcontextprotocol / csharp-sdk, Microsoft.Extensions.AI with Ol
> L11: - SKOllamaAgentWithFunction demonstrates the way to create a Semantic Kernel Agent with function in C# using Ollama

## 星数曲线

```mermaid
xychart-beta
    title "laurentkempe/aiPlayground 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 82 --> 84
    line [83, 83]
```

2026-10-18 83 → 2026-10-26 83（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `bdb7b0184b3c` · [字段定义](../../DATASET.md)*
