# kessler/gemma

⭐ 14 · TypeScript · 推送 2026-05-08 · [GitHub](https://github.com/kessler/gemma) · 个人维护

**在 Node.js 进程内本地运行 Gemma 4 模型的多模态库**

基于 @huggingface/transformers 与 ONNX Runtime 的 Node.js 库，在进程内运行 Google Gemma 4（E2B/E4B，ONNX 量化格式），输入支持文本、图像与音频，输出文本；模型首次使用时下载并缓存于 ~/.cache/huggingface/。提供 128K 上下文、流式输出、thinking 模式、GPU 后端自动选择（CoreML/CUDA/DirectML，可回退 CPU）及带工具调用循环的 Agent 类。给需要在 Node.js 中做本地推理、无 API key 与云端依赖的开发者使用。硬件要求按 q4f16 估算，未在真实设备基准测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 文本/图像/音频多模态输入，统一 API 输出文本
- 内置 Agent 系统：自主工具调用循环、截断恢复、中止支持
- 128K 上下文与 chain-of-thought thinking 模式
- GPU 后端自动检测（CoreML/CUDA/DirectML），可回退 CPU

## 适用场景

- 在 Node.js 应用中本地运行 Gemma 4 做多模态推理
- 无需 API key 与网络的离线文本生成、图像/音频理解
- 构建带工具调用的本地 agent 工作流

## 场景标签

`多模态` `推理引擎` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: Run Google's Gemma 4 models entirely on-device, embedded in a Node.js process. Text, image, and audio in — text out.
> L5: Built on `@huggingface/transformers` + ONNX Runtime. Ships with a built-in agent system for tool-calling workflows.

## 星数曲线

```mermaid
xychart-beta
    title "kessler/gemma 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `7db7f9d1d811` · [字段定义](../../DATASET.md)*
