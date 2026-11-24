# ModelCloud/GPTQModel

⭐ 1,295 · Python · NOASSERTION · 推送 2026-11-22 · [GitHub](https://github.com/ModelCloud/GPTQModel) · [官网](https://x.com/Qubitium) · 组织维护

**面向开发者的 LLM 量化压缩与加速推理工具包**

GPTQModel 将校准、量化、评估、转换与加速推理整合为统一工作流：从预训练模型出发选择压缩方案（GPTQ、AWQ、RTN、EXL3、QQQ、GGUF、FP8、VPTQ 等十余种方法），验证质量后保存 checkpoint，用于原生推理或兼容部署引擎。README 描述其覆盖 NVIDIA CUDA、AMD ROCm、Apple Metal/MLX、Intel XPU、Tenstorrent 等硬件路径，模型可经 Hugging Face、vLLM、SGLang 加载，并通过 PyPI 分发。

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
- 支持 GPTQ/AWQ/EXL3/QQQ/GGUF/FP8/VPTQ 等多种量化方法
- 覆盖 CUDA、ROCm、XPU、Tenstorrent、Metal/MLX、CPU 等硬件后端
- checkpoint 可经 HF、vLLM、SGLang 加载

## 适用场景

- 在有限显存上部署压缩后的 LLM
- 对量化 checkpoint 做质量评估与格式转换
- 在多种 GPU/NPU 硬件上运行量化模型

## 场景标签

`模型量化` `推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3:  An extensible platform for LLM quantization. Compress, evaluate, and run models across supported GPUs, accelerators
> L74: GPT-QModel brings calibration, quantization, evaluation, conversion, and accelerated
> L75: inference into one workflow. Start from a pretrained model, choose a compression

## 星数曲线

```mermaid
xychart-beta
    title "ModelCloud/GPTQModel 星数(近 20 点)"
    x-axis ["2026-10-22", "2026-10-23", "2026-10-24", "2026-10-27", "2026-10-28", "2026-10-31", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-13", "2026-11-14", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-23", "2026-11-24"]
    y-axis "stars" 1272 --> 1297
    line [1274, 1276, 1277, 1279, 1281, 1283, 1284, 1277, 1288, 1289, 1290, 1289, 1290, 1291, 1292, 1293, 1295, 1294, 1295, 1295]
```

2026-10-22 1,274 → 2026-11-24 1,295（+21）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `2c07cbc92ec3` · [字段定义](../../DATASET.md)*
