# edgett/PalmHill.BlazorChat

⭐ 72 · C# · 推送 2026-02-07 · [GitHub](https://github.com/edgett/PalmHill.BlazorChat) · [官网](https://palmhillai.com/) · 个人维护

**面向用户的本地 LLM 聊天 Web 应用（C# Blazor）**

用 C# 编写的 Blazor WebAssembly + SignalR + WebAPI 聊天应用与 API，通过 LlamaSharp 封装运行 Llama 2/3 类 GGUF 本地模型，提供实时流式对话、Markdown 渲染、温度/top P 等聊天参数设置，以及针对上传文档的 RAG 问答（早期版本）。需要 .NET 8 与 CUDA 12，用户自行下载 GGUF 模型并在 appsettings.json 中配置路径，从源码构建运行。项目自称为 Alpha 发布版本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- SignalR IAsyncEnumerable 流式实时聊天
- 支持 Llama 2/3 类 GGUF 本地模型（经 LlamaSharp）
- 上传文档的 RAG 问答（Early version）
- 聊天参数可调（温度、max length、top P 等）

## 适用场景

- 我在本地 GPU 上运行 LLM 并通过网页聊天
- 我想和自己的文档对话（RAG）
- 需要一个可自托管、全 C# 的 ChatGPT 式界面

## 场景标签

`聊天机器人` `RAG` · 领域:对话与助手

## 证据(README 行号)

> L34: 🧠 **Choose Your Language Model - Powered by Llama 2**
> L71: - Llama: This is a wrapper for LlamaSharp. Contains the code related to the Llama models.
> L5:  - Use SignalR IAsyncEnumerable streaming for chat messages.

## 星数曲线

```mermaid
xychart-beta
    title "edgett/PalmHill.BlazorChat 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 71 --> 73
    line [72, 72]
```

2026-10-18 72 → 2026-10-25 72（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `50f8635be121` · [字段定义](../../DATASET.md)*
