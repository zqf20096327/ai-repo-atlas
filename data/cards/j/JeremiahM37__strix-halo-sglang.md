# JeremiahM37/strix-halo-sglang

⭐ 42 · Python · NOASSERTION · 推送 2026-09-17 · [GitHub](https://github.com/JeremiahM37/strix-halo-sglang) · 个人维护

**面向 AMD Strix Halo 的 SGLang Docker 推理镜像**

为 AMD Ryzen AI Max+ 395 / Radeon 8060S（gfx1151）构建的 SGLang 服务 Docker 镜像。AMD 官方 rocm/sgl-dev 镜像仅面向 MI300/MI350 数据中心 GPU，本仓库通过 9+ 个补丁（sgl-kernel 架构白名单、AWQ MoE Triton 路径、RDNA int4 稠密层与 lm_head 量化、MXFP4 等）使 SGLang 在消费级 Strix Halo 上运行。镜像基于 TheRock nightly 的 PyTorch 2.13 + ROCm 7.13，提供 docker build、start-sglang.sh 脚本与 Docker Compose 两种启动方式，支持 chat completion、tool calling、RadixAttention 前缀缓存与连续批处理。README 附多模型测试表与并发吞吐基准；限制包括无 aiter Flash Attention（回退 Triton 注意力）、GPTQ MoE 生成结果数值错误且默认不启用、基准中单流对 Ollama 优势极小且未做质量评估。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 9+ 个补丁使 SGLang 与 sgl-kernel 支持 gfx1151 消费级 GPU
- 补丁 7+8 解锁 RDNA 上 int4 稠密层与 lm_head 量化（上游 Marlin 仅 CUDA）
- 支持 AWQ-MoE 与 Quark/MXFP4 检查点端到端推理
- 默认启用 TunableOp 自动调优（需挂载持久化卷）

## 适用场景

- 在 Strix Halo 迷你主机/准系统上本地部署 SGLang 推理服务
- 多用户/多 agent 并发访问同一模型的家庭实验室 AI 服务器
- 在 RDNA iGPU 上运行 Qwen3.5 系列 MoE 量化模型

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: SGLang Docker image for **AMD Ryzen AI Max+ 395 / Radeon 8060S** (gfx1151, "Strix Halo").
> L82: - SGLang pinned to a verified commit (see `SGL_BRANCH` in the Dockerfile), built from source

## 星数曲线

```mermaid
xychart-beta
    title "JeremiahM37/strix-halo-sglang 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-28"]
    y-axis "stars" 40 --> 43
    line [41, 42, 42]
```

2026-10-18 41 → 2026-10-28 42（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `5e1be45f4dd6` · [字段定义](../../DATASET.md)*
