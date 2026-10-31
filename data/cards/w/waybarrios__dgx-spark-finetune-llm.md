# waybarrios/dgx-spark-finetune-llm

⭐ 22 · Python · MIT · 推送 2025-12-22 · [GitHub](https://github.com/waybarrios/dgx-spark-finetune-llm) · 个人维护

**在 DGX Spark/Blackwell 上用 LoRA+NVFP4/MXFP8 微调 LLM 的训练流程**

面向 NVIDIA DGX Spark（Blackwell GB10）的 LLM LoRA 微调工具集：提供三种量化后端——bitsandbytes FP4（任意 CUDA GPU）、Transformer Engine NVFP4 与 MXFP8（Blackwell），3B 模型显存占用约 41-50GB；训练后可合并 LoRA 适配器、经 nvidia-modelopt 导出 NVFP4 格式，并用 TensorRT-LLM 容器以 OpenAI API 形式部署。通过 Docker 脚本（基于 NVIDIA PyTorch 容器）或 conda 环境运行，支持 /think /no_think 推理模式与 TensorBoard 监控。项目自述为进行中（work in progress）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-24g` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 三种量化微调后端：bitsandbytes FP4 / Transformer Engine NVFP4 / MXFP8
- 一条命令完成 LoRA 合并、NVFP4 量化导出与 TensorRT-LLM 部署
- LoRA 适配器输出约 240MB，NVFP4 导出约 1.5GB
- 支持 /think /no_think 扩展思考推理模式

## 适用场景

- 在 DGX Spark 上对 3B 级模型做低显存的 LoRA 微调
- 训练后导出 NVFP4 模型并用 TensorRT-LLM 提供 OpenAI 兼容 API
- 在非 Blackwell 的 CUDA GPU 上先用 bitsandbytes FP4 快速迭代

## 场景标签

`微调` `模型量化` · 领域:训练与推理

## 证据(README 行号)

> L12: Fine-tune large language models using LoRA adapters with 4-bit/8-bit quantization optimized for **NVIDIA DGX Spark*
> L16: - **NVFP4 (4-bit)**: Native Blackwell FP4 training via Transformer Engine
> L67: # Step 1: Train with NVFP4 (Blackwell optimized)

## 星数曲线

```mermaid
xychart-beta
    title "waybarrios/dgx-spark-finetune-llm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-31 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `b464e337cbb8` · [字段定义](../../DATASET.md)*
