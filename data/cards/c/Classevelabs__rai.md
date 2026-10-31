# Classevelabs/rai

⭐ 14 · Rust · Apache-2.0 · 推送 2026-09-19 · [GitHub](https://github.com/Classevelabs/rai) · [官网](https://classeve.com/public/rai) · 组织维护

**纯 Rust 的 CPU-only LLM 推理引擎，4-bit 量化，自带 HTTP/MCP 服务**

面向开发者的 CPU-only LLM 推理引擎：以 Rust 编写，用手写 AVX2/FMA/F16C 内核运行 4-bit 量化模型，不依赖 GPU、CUDA、Python 运行时、PyTorch、GGML 或 BLAS。支持将 Llama/Mistral/Qwen/Gemma/Phi-3/OLMo/MoE 等 .safetensors 检查点转换为自有 .raimodel 格式（rai convert，流式读取，峰值内存不随模型增长），支持投机解码（draft-model 与 prompt-lookup 两种模式）与测试时计算策略。提供 rai run CLI 与 rai serve 本地 HTTP 聊天服务（内置 Web UI），以及 REST+MCP 服务供 Claude Desktop/Claude Code 等 agent 工具接入。限制：不支持的架构在转换时按名拒绝（如 Falcon、GPT-NeoX、MPT、GPT-2、Phi-2）；pytorch_model.bin 不读取；MoE 之外的 Llama 形之外的模块树不支持。构建需 Rust 1.87+，通过 cargo 构建或取预编译二进制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 纯 Rust 实现，无 GPU/CUDA/Python 运行时/PyTorch/GGML/BLAS 依赖
- 手写 AVX2+FMA+F16C 内核，4-bit 权重在寄存器内反量化，无 fp32 权重副本
- 投机解码双模式：draft-model 与 prompt-lookup，均以目标模型分布验证
- rai serve 提供内置 Web UI 的 HTTP 聊天服务及 REST+MCP 接口

## 适用场景

- 在无 GPU 的 x86-64 机器上本地运行量化 LLM
- 把 HuggingFace .safetensors 检查点转换为单一 .raimodel 文件并生成文本
- 通过 MCP 让 Claude Desktop/Claude Code 等 agent 工具把 RAI 用作推理后端
- 在低内存设备上流式转换大模型（7B 模型在 16 GB 笔记本上可转换）

## 场景标签

`推理引擎` `模型量化` · 领域:训练与推理

## 证据(README 行号)

> L5: **A CPU-only LLM inference engine written in Rust.** RAI runs 4-bit quantized
> L127: |`rai-infer`|The inference engine: `.raimodel` loader and writer, AVX2 W4A8 GEMM kernels, transformer layers (RMSN
> L119: - **Local serving.** An HTTP chat server with a built-in web UI, plus a REST +

## 星数曲线

```mermaid
xychart-beta
    title "Classevelabs/rai 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `27ee95e57fe9` · [字段定义](../../DATASET.md)*
