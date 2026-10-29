# elbruno/ElBruno.LocalLLMs

⭐ 24 · C# · MIT · 推送 2026-10-22 · [GitHub](https://github.com/elbruno/ElBruno.LocalLLMs) · 个人维护

**.NET 本地 LLM 聊天库：经 IChatClient 运行 ONNX 模型**

基于 ONNX Runtime GenAI 的 C# 库，实现 Microsoft.Extensions.AI 的 IChatClient 接口，让 .NET 应用以与 Azure OpenAI/Ollama 相同的接口在本地运行 LLM。支持 CPU/CUDA/DirectML 多硬件、首次使用自动从 HuggingFace 下载模型、流式输出、DI 注册；附 Blazor 组件、RAG 管道、BitNet 1.58-bit 模型与返回带概率分布的决策模型等子包。限制：CUDA 需 13.* 与 cuDNN 9.*，Laya 决策模型置信度未校准。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 实现 IChatClient，兼容 Microsoft.Extensions.AI 生态
- CPU/CUDA/DirectML 多执行提供者并自动回退
- 首次使用自动从 HuggingFace 下载模型并本地缓存
- 子包覆盖 Blazor 组件、RAG、BitNet 1.58-bit 与类型化决策模型

## 适用场景

- 在 .NET 应用中离线运行 Phi/Qwen/Llama 等本地模型
- 以统一 IChatClient 接口在本地与云端提供者间切换
- 用类型化决策模型快速产出带概率的选择/评分/是 否答案

## 场景标签

`推理引擎` `RAG` · 领域:知识与检索

## 证据(README 行号)

> L14: Run local LLMs in .NET through `IChatClient` — the same interface you'd use for Azure OpenAI, Ollama, or any other 
> L22: - 🔌 **`IChatClient` implementation** — seamless integration with Microsoft.Extensions.AI

## 星数曲线

```mermaid
xychart-beta
    title "elbruno/ElBruno.LocalLLMs 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-29"]
    y-axis "stars" 22 --> 25
    line [23, 24, 24]
```

2026-10-18 23 → 2026-10-29 24（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `ce57ba018c97` · [字段定义](../../DATASET.md)*
