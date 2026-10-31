# pie-project/pie

⭐ 238 · Rust · Apache-2.0 · 推送 2026-10-30 · [GitHub](https://github.com/pie-project/pie) · [官网](https://pie-project.org) · 组织维护

**可编程高性能模型推理引擎，用 WebAssembly inferlet 驱动推理**

面向开发者的推理引擎：以运行在模型旁的 WebAssembly 程序（inferlet）驱动前向传播，可用 Python、JavaScript 或 Rust 编写解码、采样、KV 缓存等逻辑，并将 epilogue 编译为 GPU kernel。模型以 Poem 语言编写，覆盖语言、视觉、图像与视频；整个系统编译为约 60 MB 单一二进制，无 Python/PyTorch 运行时，支持 CUDA、ROCm、Metal、Vulkan、XLA(TPU) 与 WebGPU。提供 pie serve 服务与 OpenAI/Anthropic/Gemini 兼容 API，可从 Hugging Face 导入模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- inferlet 以 Python/JS/Rust 编写解码、采样、KV 淘汰等逻辑
- 单一约 60 MB 二进制，无 Python/PyTorch 运行时
- 支持 CUDA/ROCm/Metal/Vulkan/XLA(TPU)/WebGPU 多后端
- pie serve 提供 OpenAI/Anthropic/Gemini 兼容 API

## 适用场景

- 为应用定制解码与采样策略并部署高性能推理服务
- 用现有 OpenAI 兼容客户端接入本地模型服务
- 在浏览器中通过 WebGPU 运行推理（Playground/嵌入式 server）

## 场景标签

`推理引擎` `多模态` · 领域:感知与多模态

## 证据(README 行号)

> L7: Pie runs WebAssembly programs—*inferlets*—directly next to the
> L14: PyTorch runtime, running on CUDA, ROCm, Metal, Vulkan, XLA (TPUs), and WebGPU.
> L68: `pie serve` also speaks the


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `67b5ec99cbce` · [字段定义](../../DATASET.md)*
