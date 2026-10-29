# xigh/herbert-rs

⭐ 44 · Rust · MIT · 推送 2026-03-18 · [GitHub](https://github.com/xigh/herbert-rs) · [官网](https://philippe-anel.fr/en/blog/2026/03/15/herbert-comprendre-avant-optimiser/) · 个人维护

**Rust 从零实现的本地 LLM 推理引擎，含 CPU/GPU 内核与 CLI/服务器**

用 Rust 从零编写的本地大模型推理引擎，不依赖 GGML 或 llama.cpp：矩阵乘、注意力与量化例程均为直接实现。CPU 侧提供手写 AVX-512 汇编内核（BF16/INT8 VNNI/Q4），GPU 侧提供 Metal（macOS，92 个计算着色器）与 Vulkan（Linux，31 个 GLSL 着色器）后端。支持 Qwen3 系列文本/视觉语言/MoE 与 Mistral3 系列模型，量化格式为 BF16/INT8/Q4（可混合精度），KV 缓存支持 INT8 量化。以 herbert-cli（交互与单次推理）、herbert-server（Anthropic Messages 兼容 HTTP API）与 herbert-desktop（Tauri 2 + Vue 3 桌面应用）三种形态提供，通过 cargo 从源码构建。设计上以解码阶段的内存带宽为优化目标，长上下文解码吞吐相对较高，稠密模型 prefill 目前落后于 llama.cpp。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CPU：手写 x86-64 汇编内核（BF16 AVX-512、INT8 VNNI、Q4 预交错），GPU：Metal 与 Vulkan 计算着色器
- BF16/INT8/Q4 量化，支持同模型混合精度与 INT8 KV 缓存量化
- 支持 Qwen3 文本/VL/MoE 与 Mistral3 系列模型，含多图视觉语言输入
- 提供 CLI、Anthropic Messages 兼容 HTTP 服务器与 Tauri 桌面应用三种形态

## 适用场景

- 在本地 CPU 或 GPU 上运行 Qwen3/Mistral3 系列模型进行对话推理
- 通过 Anthropic Messages 兼容 API 将本地模型接入现有客户端
- 在长上下文场景下以 INT8 KV 缓存降低内存带宽开销

## 场景标签

`推理引擎` `模型量化` · 领域:训练与推理

## 证据(README 行号)

> L3: A local LLM inference engine written from scratch in Rust, with hand-written SIMD kernels and GPU compute shaders. N
> L123: ### `herbert-server` — HTTP API
> L225: cargo build --release

## 星数曲线

```mermaid
xychart-beta
    title "xigh/herbert-rs 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-29"]
    y-axis "stars" 42 --> 45
    line [43, 44, 44]
```

2026-10-18 43 → 2026-10-29 44（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `d562a7ea2f95` · [字段定义](../../DATASET.md)*
