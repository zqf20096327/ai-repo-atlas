# RustingStudio/RustingStrata

⭐ 495 · Rust · NOASSERTION · 推送 2026-11-26 · [GitHub](https://github.com/RustingStudio/RustingStrata) · 组织维护

**纯 Rust 的 GGUF LLM 推理引擎：让超出显存的 MoE 模型在本地运行**

纯 Rust 编写的 GGUF 模型推理引擎，面向放不进显存的 MoE 模型：CUDA 内核通过 NVRTC 运行时编译，同一套内核可在 Vulkan 上运行，装不进显存的专家在 CPU 上与 GPU 并行执行，专家放置随路由自适应。支持 Qwen3 系列、DeepSeek-V4.1-Flash、GLM-5.3-Flash、Gemma 4 等架构，提供聊天页面、OpenAI 与 Anthropic 兼容 API、并行批量解码和 MCP 工具，README 以与 llama.cpp 的对比数据展示解码速度。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CUDA 内核 NVRTC 运行时编译，同一内核运行于 Vulkan，无 C++ 构建步骤
- 放不进显存的专家在 CPU 上并行执行，专家放置随路由自适应
- serve --parallel N 批量解码支持多用户并发
- 提供 OpenAI 与 Anthropic 兼容 API 及聊天页面

## 适用场景

- 在 12 GB 显卡上本地运行 27 GB 级别的 MoE 模型
- 为 Open WebUI、SillyTavern、代码编辑器等提供本地 OpenAI 兼容接口
- 同时托管 API 服务给多人使用

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L5: A pure-Rust inference engine for GGUF models, built for MoE models that do not fit in VRAM. The CUDA kernels are
> L6: compiled at run time with NVRTC, and the same kernels run on Vulkan: no C++ build step, no ggml. Experts that do not
> L94: your models folder. Any app that takes an OpenAI-compatible address (Open WebUI, Jan, SillyTavern, code editors) ca

## 星数曲线

```mermaid
xychart-beta
    title "RustingStudio/RustingStrata 星数(近 19 点)"
    x-axis ["2026-11-01", "2026-11-02", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-27"]
    y-axis "stars" 0 --> 544
    line [3, 10, 145, 195, 214, 226, 228, 230, 249, 260, 267, 285, 292, 310, 330, 360, 395, 443, 495]
```

2026-11-01 3 → 2026-11-27 495（+492）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `dede2478e963` · [字段定义](../../DATASET.md)*
