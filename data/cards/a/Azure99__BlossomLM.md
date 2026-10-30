# Azure99/BlossomLM

⭐ 183 · Apache-2.0 · 推送 2026-09-12 · [GitHub](https://github.com/Azure99/BlossomLM) · 个人维护 · 中文 README

**开源权重多模态大模型家族，面向本地部署**

Blossom-V7.1 是一组开放权重（Apache 2.0）的通用多模态模型，基于 Qwen 系列基座后训练而成，含 27B、35B-A3B、9B 三个变体。功能包括 medium/max 两档思考模式、带交错思考的工具调用、图像理解与最长 262K 上下文，通过 MTP 支持 vLLM 与 llama.cpp 中的投机解码。提供 Transformers、vLLM、llama.cpp (GGUF) 三种运行方式，需使用自带 chat template；README 明确 Ollama 当前不被推荐。训练数据使用 BlossomData 管线处理，V7.1 数据承诺未来开源，当前公开数据集为 V6.3 版本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- medium/max 两档思考模式，默认 max，medium 推理轨迹长度约为 Qwen3.5 的四分之一
- 工具调用前进行交错思考推理，支持 agentic 工作流
- 最长 262,144 tokens 上下文（推荐 128K）
- 通过 MTP 在 vLLM 与 llama.cpp 中支持投机解码加速推理

## 适用场景

- 在本地 GPU 或 CPU/混合环境下部署多模态对话模型
- 执行数学推理、编码、Web 开发与数据可视化任务
- 通过工具调用构建 agentic 工作流

## 场景标签

`多模态` · 领域:感知与多模态

## 证据(README 行号)

> L9: Blossom-V7.1 is a family of open-weight, general-purpose multimodal models designed for local deployment. It combine
> L25: |Blossom-V7.1-27B|Demo GGUF|Qwen3.8-27B|
> L26: |Blossom-V7.1-35B-A3B|Demo GGUF|Qwen3.6-35B-A3B|
> L27: |Blossom-V7.1-9B|Demo GGUF|Qwen3.5-9B|

## 星数曲线

```mermaid
xychart-beta
    title "Azure99/BlossomLM 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 182 --> 184
    line [183, 183]
```

2026-10-18 183 → 2026-10-30 183（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `6a92a21d82cb` · [字段定义](../../DATASET.md)*
