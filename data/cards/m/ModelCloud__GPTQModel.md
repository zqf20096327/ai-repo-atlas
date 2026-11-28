# ModelCloud/GPTQModel

⭐ 1,296 · Python · NOASSERTION · 推送 2026-11-27 · [GitHub](https://github.com/ModelCloud/GPTQModel) · [官网](https://x.com/Qubitium) · 组织维护

**面向 LLM 研究者的模型量化压缩与推理工具包**

GPTQModel 是一个 LLM 量化平台，将校准、量化、评估、格式转换与加速推理整合到同一工作流：从预训练模型出发，选择压缩配方（GPTQ/AWQ/EXL3/GGUF/FP8/MACaQ/QQQ 等十余种方法），验证质量并导出检查点，用于原生推理或兼容部署引擎。支持 NVIDIA CUDA、AMD ROCm/HIP、Intel XPU、Apple Metal/MLX、Tenstorrent、华为昇腾等多类硬件后端，并兼容 Transformers、vLLM、SGLang。通过 PyPI 分发，按版本更新量化精度、显存占用与模型覆盖。

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

- 提供 GPTQ、AWQ、EXL3、GGUF、FP8、MACaQ、QQQ 等多种量化方法
- 支持 CUDA/ROCm/XPU/Metal/MLX/Tenstorrent/昇腾等多硬件后端
- 量化、评估、转换与加速推理统一在一个工作流
- 兼容 Transformers、vLLM、SGLang 及 GGUF/llama.cpp 生态

## 适用场景

- 把大模型压缩到低比特以便在有限显存上部署
- 对比不同量化方法的校准质量与困惑度
- 为 vLLM/SGLang 等推理引擎准备量化检查点
- 在 Apple silicon 或国产 NPU 上运行量化模型

## 场景标签

`模型量化` `推理引擎` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3:  An extensible platform for LLM quantization. Compress, evaluate, and run models across supported GPUs, accelerators
> L74: GPT-QModel brings calibration, quantization, evaluation, conversion, and accelerated
> L75: inference into one workflow. Start from a pretrained model, choose a compression

## 星数曲线

```mermaid
xychart-beta
    title "ModelCloud/GPTQModel 星数(近 19 点)"
    x-axis ["2026-10-26", "2026-10-27", "2026-10-28", "2026-10-31", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-13", "2026-11-14", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-23", "2026-11-25", "2026-11-28"]
    y-axis "stars" 1276 --> 1297
    line [1277, 1279, 1281, 1283, 1284, 1277, 1288, 1289, 1290, 1289, 1290, 1291, 1292, 1293, 1295, 1294, 1295, 1296, 1296]
```

2026-10-26 1,277 → 2026-11-28 1,296（+19）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `6441cce292df` · [字段定义](../../DATASET.md)*
