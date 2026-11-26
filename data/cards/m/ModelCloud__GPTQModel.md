# ModelCloud/GPTQModel

⭐ 1,296 · Python · NOASSERTION · 推送 2026-11-25 · [GitHub](https://github.com/ModelCloud/GPTQModel) · [官网](https://x.com/Qubitium) · 组织维护 · 中文 README

**面向开发者的 LLM 量化压缩工具包，含多硬件加速推理**

GPTQModel 是一个可扩展的 LLM 量化平台，将校准、量化、评估、转换与加速推理整合为统一工作流：从预训练模型出发，选择压缩配方，验证质量并保存检查点，供原生推理或兼容部署引擎使用。支持 GPTQ、AWQ、RTN、QQQ、FP8、EXL3、GGUF、MACaQ 等多种量化方法，覆盖稠密与 MoE 模型，并提供 `model.budget()` 内存预算估算、断点续跑的分布式量化作业、可自动定长的校准批配置等机制。模型产出可通过 Hugging Face、vLLM、SGLang 等通道部署。以 PyPI 包形式分发，带文档与量化指南。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一工作流覆盖校准、量化、评估、转换与加速推理
- 支持 GPTQ/AWQ/RTN/QQQ/FP8/EXL3/GGUF/MACaQ 等多种量化方法
- 硬件覆盖 NVIDIA CUDA、AMD ROCm、Intel XPU、Tenstorrent、华为昇腾 NPU 及 Intel/AMD/Apple CPU
- 支持 `model.budget()` 估算上下文长度与批次大小的内存预算

## 适用场景

- 把预训练 LLM 压缩到低比特以降低显存占用
- 为 vLLM/SGLang 等部署引擎生成量化检查点
- 在 AMD ROCm、昇腾 NPU 等非 CUDA 硬件上做量化推理
- 校准 MoE 与多模态模型并验证量化后质量

## 场景标签

`模型量化` `推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3:  An extensible platform for LLM quantization. Compress, evaluate, and run models across supported GPUs, accelerators
> L72: ## A unified quantization platform 🧩
> L74: GPT-QModel brings calibration, quantization, evaluation, conversion, and accelerated
> L77: compatible deployment engine.

## 星数曲线

```mermaid
xychart-beta
    title "ModelCloud/GPTQModel 星数(近 19 点)"
    x-axis ["2026-10-24", "2026-10-27", "2026-10-28", "2026-10-31", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-13", "2026-11-14", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-23", "2026-11-25", "2026-11-26"]
    y-axis "stars" 1276 --> 1297
    line [1277, 1279, 1281, 1283, 1284, 1277, 1288, 1289, 1290, 1289, 1290, 1291, 1292, 1293, 1295, 1294, 1295, 1296, 1296]
```

2026-10-24 1,277 → 2026-11-26 1,296（+19）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `d1c207f976ff` · [字段定义](../../DATASET.md)*
