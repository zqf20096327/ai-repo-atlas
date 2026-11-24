# afshinm/cactus-needle

⭐ — · [GitHub]() · 个人维护

**JS/TS 本地推理库：浏览器/Node.js 运行模型做工具调用与转录**

JavaScript/TypeScript 库，封装 Needle 与 Whistle 两个本地模型，在 Node.js 与浏览器的 WebAssembly CPU worker 中运行。提供工具调用、结构化抽取、文本嵌入、语音转录与实时转录等能力，推理无需 API key、服务器或 GPU。默认权重从 Hugging Face 下载并缓存（Needle 35.3 MB、Whistle 16.9 MB）。可选集成 Vercel AI SDK provider，支持 AI SDK 6/7；非通用聊天模型，面向工具与结构化数据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 浏览器与 Node.js 均可在 CPU WebAssembly worker 中运行，无需 API key、服务器或 GPU
- 能力覆盖工具调用、结构化抽取、文本嵌入、语音转录与实时转录
- 可选 Vercel AI SDK provider，支持 AI SDK 6 与 7
- 默认权重按需从 Hugging Face 下载并缓存，仅加载所用模型

## 适用场景

- 在浏览器端为应用添加本地工具调用与结构化数据抽取
- 对音频做本地语音转录或实时流式转录
- 生成文本嵌入并向 AI SDK 应用提供本地模型后端

## 场景标签

`推理引擎` `语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L28: Local tool calling, structured extraction, embeddings, and speech transcription
> L32: Both models run in Node.js and browsers, on the CPU in WebAssembly workers.
> L61: |Tool calling|Needle|`complete()`, `generate()`, `run()`|

## 星数曲线

```mermaid
xychart-beta
    title "afshinm/cactus-needle 星数(近 3 点)"
    x-axis ["2026-10-30", "2026-11-20", "2026-11-24"]
    y-axis "stars" 3 --> 6
    line [4, 5, 5]
```

2026-10-30 4 → 2026-11-24 5（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `f57d3758de9b` · [字段定义](../../DATASET.md)*
