# vllm-project/vllm-xpu-kernels

⭐ 79 · C++ · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/vllm-project/vllm-xpu-kernels) · 组织维护

**为 Intel GPU 提供 vLLM 定制算子与内核的加速库**

vLLM 项目的组件，用 SYCL/DPC++ 编写并基于 oneDNN 实现 Intel XPU（GPU）后端的定制 Torch 算子，覆盖归一化、激活、Flash Attention、RoPE、MoE、LoRA、FP8/MxFP4 量化与分组 GEMM 等类别。启动时 vLLM 通过 import 注册算子到 PyTorch dispatcher，自动调度到 XPU，无需改动 vLLM 代码；最新 vLLM XPU 版本会作为 wheel 依赖自动安装。提供 PyPI 安装、源码构建、Dockerfile.xpu 开发镜像，要求 Python 3.12、PyTorch 2.14.0+xpu、oneAPI 2026.1。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SYCL/DPC++ 实现的 XPU 定制算子，覆盖注意力、MoE、量化、LoRA 等
- 通过 PyTorch custom op 注册机制随 vLLM 启动自动加载
- 支持 Docker（Dockerfile.xpu）与裸机两种构建环境
- 默认为 Llama、Qwen、DeepSeek 等常见模型编译内核，可通过环境变量定制

## 适用场景

- 在 Intel GPU 上运行 vLLM 高吞吐 LLM 推理
- 开发与调试 Intel XPU 后端的定制算子
- 对单个内核做基准测试与验证

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: A vLLM component that provides optimized custom kernels for Intel GPUs (XPU) to accelerate LLM inference.
> L9: vLLM defines and implements many custom Torch ops and kernels. This repository provides custom implementations for t
> L39: vLLM calls `import vllm_xpu_kernels._C` at startup, which registers all custom ops into the PyTorch dispatcher. Fro

## 星数曲线

```mermaid
xychart-beta
    title "vllm-project/vllm-xpu-kernels 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-26", "2026-10-27"]
    y-axis "stars" 75 --> 80
    line [76, 77, 79, 79]
```

2026-10-18 76 → 2026-10-27 79（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `e1d31a446cc7` · [字段定义](../../DATASET.md)*
