# sgl-project/sgl-kernel-npu

⭐ 196 · C++ · MIT · 推送 2026-10-22 · [GitHub](https://github.com/sgl-project/sgl-kernel-npu) · 组织维护 · 中文 README

**SGLang 框架面向昇腾 NPU 的推理算子库**

SGLang 框架官方的 Ascend NPU 算子库，由 DeepEP-Ascend（MoE 专家并行的 all-to-all 通信算子，支持 Normal 与 Low-Latency 两种模式、INT8/FP8/BF16 量化）与 SGLang-Kernel-NPU（MLA/GQA 注意力、RMSNorm、SwiGLU、LoRA、投机解码树验证、Mamba Causal Conv1D、Paged KV Cache 等推理算子）两部分组成。面向在昇腾硬件上运行 LLM 推理的开发者，从源码构建（含 git submodule 初始化），CI 覆盖 CANN 9.0.0/9.1.0，CANN 8.5.0 兼容性已不再验证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- DeepEP-Ascend 提供 MoE 专家并行 all-to-all 通信算子（Normal/Low-Latency 模式）
- 覆盖 MLA/GQA 注意力、RMSNorm、SwiGLU、LoRA、投机解码等推理算子
- INT8/FP8/BF16 量化支持
- README 给出 A3 384 SuperPOD 上按 DeepSeek-V3/R1 设置的实测带宽与延迟数据

## 适用场景

- 在昇腾 NPU 上运行 SGLang LLM 推理
- 为 MoE 模型部署专家并行通信算子
- 昇腾平台 LLM 推理算子的开发与测试（可申请 HiDevLab 免费资源）

## 场景标签

 · 领域:LLM 推理基础设施

## 证据(README 行号)

> L5: **SGLang-Kernel-NPU** is the official kernel library of the SGLang framework for Ascend NPU. It delivers high-perfor
> L11: - **SGLang-Kernel-NPU**: A comprehensive collection of optimized inference kernels including attention mechanisms, 

## 星数曲线

```mermaid
xychart-beta
    title "sgl-project/sgl-kernel-npu 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 192 --> 196
    line [193, 194, 195]
```

2026-10-18 193 → 2026-10-22 195（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `2ebed8e8d03e` · [字段定义](../../DATASET.md)*
