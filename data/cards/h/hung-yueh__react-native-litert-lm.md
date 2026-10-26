# hung-yueh/react-native-litert-lm

⭐ 63 · TypeScript · MIT · 推送 2026-10-24 · [GitHub](https://github.com/hung-yueh/react-native-litert-lm) · [官网](https://litert.dev) · 个人维护

**React Native 端侧 LLM 推理库：手机上运行 Gemma 等模型**

基于 Google LiteRT-LM 引擎与 Nitro Modules（JSI）的 React Native 库，供开发者在 iOS/Android 应用内运行 .litertlm 格式模型（Gemma 4/3n/3、Qwen、Phi-4 Mini、LFM2.5），支持文本/图像/音频多模态输入、流式 token/toolCall/thinking 事件、JSON Schema/正则约束解码、工具调用、端侧嵌入（RAG/语义检索）。核心机制是三层内存管理（预加载评估、实时 RSS 跟踪、OS 压力告警）以避免 2–4 GB 模型触发 OOM；仅支持 ARM 设备，iOS 15.1+/Android API 26+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 预加载内存评估、实时跟踪与确定性 unload() 的防 OOM 内存管理
- 约束解码：输出限定为 JSON Schema 或正则
- 端侧嵌入（EmbeddingGemma 2）支持文本/图像/音频向量化用于搜索与 RAG
- GPU（Metal/OpenCL）、Android NPU 加速与 CPU 回退；流式 token/toolCall/thinking 类型化事件

## 适用场景

- 在手机 App 中集成离线聊天/助手（2–4 GB 模型不被系统杀死）
- 离线结构化抽取：把收据、表单、分类结果约束到自有 schema
- 带工具调用与推理过程展示的 Agentic 应用
- 应用内内容的端侧语义搜索与 RAG

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: **Gemma 4 on iPhone and Android from React Native.** On-device inference with LiteRT-LM and Nitro Modules, with firs
> L14: import { createLLM, GEMMA_4_E2B_IT } from "react-native-litert-lm";
> L75: |Engine|Google LiteRT-LM|PyTorch ExecuTorch|llama.cpp|

## 星数曲线

```mermaid
xychart-beta
    title "hung-yueh/react-native-litert-lm 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-26"]
    y-axis "stars" 61 --> 64
    line [62, 63, 63]
```

2026-10-18 62 → 2026-10-26 63（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `fdf571fb3908` · [字段定义](../../DATASET.md)*
