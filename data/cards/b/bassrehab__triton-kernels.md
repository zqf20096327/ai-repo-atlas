# bassrehab/triton-kernels

⭐ 44 · Python · MIT · 推送 2026-07-22 · [GitHub](https://github.com/bassrehab/triton-kernels) · 个人维护

**面向 LLM 推理的 Triton GPU 算子集：融合/量化 kernel 与 roofline 分析**

以 OpenAI Triton 实现的 transformer 推理算子集合，涵盖 RMSNorm、融合 RMSNorm+残差、融合 SwiGLU、W8A16 INT8 GEMM、融合 MoE dispatch 与 W4A16 4-bit GEMM。每个 kernel 附带 roofline 分析说明优化原理，并在 NVIDIA A100 与 AMD MI300X 上给出基准数据；其中两个 kernel 发布于 Hugging Face Kernel Hub，可通过 kernels 库免安装直接加载。README 声明为教学用途、非生产就绪，生产场景建议 vLLM、FlashAttention 或 TensorRT-LLM。

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

- 6 个推理算子的 Triton 实现，附 roofline 分析与 A100/MI300X 基准
- 融合 MoE dispatch kernel 在小批量下相对 Megablocks 基线延迟更低
- 两个 kernel 发布于 Hugging Face Kernel Hub，get_kernel 直接加载
- 提供 TritonRMSNorm / SwiGLU / Int8Linear 可替换 torch.nn 模块

## 适用场景

- 学习 LLM 推理算子为何以及如何做融合与量化优化
- 在自己的模型中替换 RMSNorm/SwiGLU/线性层以减少显存占用与访存
- 在自有 GPU 上复现并运行各 kernel 的基准测试

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L11: High-performance GPU kernels for LLM inference, implemented in OpenAI Triton.
> L13: This repository provides educational, well-documented implementations of common transformer operations optimized fo

## 星数曲线

```mermaid
xychart-beta
    title "bassrehab/triton-kernels 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-28 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `1ee136d69dd1` · [字段定义](../../DATASET.md)*
