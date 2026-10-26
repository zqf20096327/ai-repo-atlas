# Llaminar/llaminar

⭐ 45 · C++ · AGPL-3.0 · 推送 2026-10-25 · [GitHub](https://github.com/Llaminar/llaminar) · [官网](https://llaminar.ai) · 组织维护

**C++ 编写的 LLM 推理引擎，CPU/NVIDIA/AMD 混合并行**

用 C++ 实现并自带量化模型内核的 LLM 推理引擎：读取 GGUF 模型文件，在 x86-64 CPU（AVX512-VNNI/AVX2）、NVIDIA CUDA、AMD ROCm 硬件或三者的混合上运行，支持单机或跨集群共享负载。核心机制是自动规划器：给定模型与上下文长度后自动选择设备布局，支持张量并行、流水线并行与 MoE 专家分布（ExpertOverlay），计划可保存为 JSON 复用。以 Docker 镜像分发，起 OpenAI 兼容 HTTP 服务，默认开启前缀缓存，可选多 token 预测（MTP）。项目自述处于 alpha 阶段。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 自动规划器按硬件选择设备布局，计划可保存为 JSON 检查复用
- CPU/NVIDIA/AMD 可在同一部署中混合使用，含 MoE ExpertOverlay 专家分布
- 自带量化内核的 C++ 实现，支持张量并行与流水线并行
- OpenAI 兼容 HTTP 服务，默认前缀缓存，可选 MTP 多 token 预测

## 适用场景

- 在 CPU 与多厂商 GPU 混合的机器上本地部署 GGUF 模型
- 让推理引擎自动决定张量/流水线/专家并行的设备布局
- 用 OpenAI 兼容接口从已有应用调用本地模型服务

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: Llaminar runs large language models on CPUs, NVIDIA GPUs, AMD GPUs, or a mix of
> L4: all three. It is written in C++ and includes its own kernels for quantised models.
> L76: The three steps below start an OpenAI-compatible HTTP server. Run the setup

## 星数曲线

```mermaid
xychart-beta
    title "Llaminar/llaminar 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-26 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `234f69eb086c` · [字段定义](../../DATASET.md)*
