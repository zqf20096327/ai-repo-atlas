# NVIDIA/Model-Optimizer

⭐ 5,655 · Python · Apache-2.0 · 推送 2026-11-24 · [GitHub](https://github.com/NVIDIA/Model-Optimizer) · [官网](https://nvidia.github.io/Model-Optimizer/) · 组织维护

**模型压缩优化库：量化/剪枝/蒸馏后导出部署**

NVIDIA 提供的 Python 库，输入支持 Hugging Face、PyTorch 或 ONNX 模型，通过 Python API 组合量化、剪枝、蒸馏、NAS、投机解码、稀疏化等技术，生成优化后的量化检查点，并可导出至 TensorRT-LLM、TensorRT、vLLM、SGLang 等推理框架部署。同时提供预量化检查点下载、各技术支持矩阵与 deprecation 政策，并附带 Claude Code/Codex 可安装的 agent 技能。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 支持 PTQ、QAT/蒸馏、剪枝、NAS、投机解码、稀疏化六类优化技术
- 输入支持 Hugging Face、PyTorch、ONNX 模型，统一 HF 导出 API 覆盖 transformers 与 diffusers
- 量化检查点可导出至 TensorRT-LLM、TensorRT、vLLM、SGLang 部署
- 提供预量化检查点合集与各技术支持矩阵

## 适用场景

- 部署前将大模型量化压缩以减小体积并提升推理速度
- 通过剪枝与蒸馏训练更小的部署模型
- 生成 FP8/NVFP4 检查点供 vLLM 或 TensorRT-LLM 加载

## 场景标签

`模型量化` · 领域:训练与推理

## 证据(README 行号)

> L13: **NVIDIA Model Optimizer** (referred to as **Model Optimizer**, or **ModelOpt**) is a library comprising state-of-t
> L17: **[Optimize]** Model Optimizer provides Python APIs for users to easily compose the above model optimization techni
> L20: **[Export for deployment]** Seamlessly integrated within the NVIDIA AI software ecosystem, the quantized checkpoint

## 星数曲线

```mermaid
xychart-beta
    title "NVIDIA/Model-Optimizer 星数(近 28 点)"
    x-axis ["2026-10-21", "2026-10-22", "2026-10-23", "2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-24"]
    y-axis "stars" 5342 --> 5679
    line [5370, 5394, 5413, 5425, 5428, 5435, 5444, 5453, 5461, 5466, 5472, 5477, 5489, 5428, 5557, 5590, 5596, 5601, 5604, 5609, 5612, 5618, 5629, 5637, 5643, 5646, 5651, 5651]
```

2026-10-21 5,370 → 2026-11-24 5,651（+281）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `97a273bd6947` · [字段定义](../../DATASET.md)*
