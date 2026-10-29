# sizzlecar/ferrum-infer-rs

⭐ 21 · Rust · MIT · 推送 2026-10-28 · [GitHub](https://github.com/sizzlecar/ferrum-infer-rs) · [官网](https://ferrum.pandaailabs.com/) · 组织维护 · 中文 README

**单二进制 Rust LLM/图像推理服务引擎，OpenAI 兼容 API**

以单一 Rust 二进制提供文本与图像推理服务，不依赖 Python 运行时。文本侧支持 Llama、Mistral、Qwen2/Qwen3（含 MoE）、Gemma 3 等架构，读取 GGUF 与 SafeTensors 权重（部分 CUDA 路径支持 GPTQ INT4/压缩 INT4/FP8）；图像侧支持 Qwen-Image-2.1-Turbo 的生成与单 PNG 编辑，CUDA 与 Metal（GGUF DiT）均可运行。提供 CLI 与 OpenAI 兼容 API，安装为 curl/PowerShell 脚本下载二进制并校验和。目标为满足 TTFT/TPOT/ITL SLO 约束下最大化输出吞吐；README 提供与 vLLM、llama.cpp 的对比测量数据，并声明内部 API 可能变化、硬件支持有限。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 单 Rust 二进制，同时提供 CLI 与 OpenAI 兼容 API
- 文本支持 Llama/Mistral/Qwen2/Qwen3 MoE/Gemma 3，GGUF 与 SafeTensors 权重
- Qwen-Image-2.1-Turbo 生成与单 PNG 编辑（CUDA FP8 与 Metal GGUF DiT 路径）
- macOS Metal / Linux / Windows CUDA(sm89, sm120) 安装脚本带校验和验证

## 适用场景

- 本地运行 Qwen/Llama 等文本模型并通过 OpenAI 兼容 API 提供服务
- 在 Apple Silicon 上用 GGUF DiT 本地生成与编辑图像
- 在延迟 SLO 约束下追求输出吞吐的推理部署

## 场景标签

`推理引擎` `图像生成` · 领域:内容生成

## 证据(README 行号)

> L9: Text and image inference in one Rust binary, with CLI and OpenAI-compatible APIs.
> L51: ferrum serve --model qwen3.5:4b-q4_k_m --served-model-name ferrum --disable-thinking --port 8000

## 星数曲线

```mermaid
xychart-beta
    title "sizzlecar/ferrum-infer-rs 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-29"]
    y-axis "stars" 19 --> 22
    line [20, 21, 21]
```

2026-10-18 20 → 2026-10-29 21（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `fcdb3f7df9e0` · [字段定义](../../DATASET.md)*
