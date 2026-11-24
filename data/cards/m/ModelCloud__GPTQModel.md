# ModelCloud/GPTQModel

⭐ 1,296 · Python · NOASSERTION · 推送 2026-11-24 · [GitHub](https://github.com/ModelCloud/GPTQModel) · [官网](https://x.com/Qubitium) · 组织维护

**面向 LLM 开发者的多后端量化压缩与推理工具包**

将校准、量化、评估、转换与加速推理整合为统一工作流的量化平台：从预训练模型出发选择压缩配方，验证质量后保存可原生推理或部署到兼容引擎的 checkpoint。支持 GPTQ、AWQ、RTN、QQQ、EXL3、GGUF、FP8 等多种量化方法，覆盖 NVIDIA CUDA、AMD ROCm、Apple silicon、Intel XPU、Tenstorrent 与华为昇腾等硬件路径。以 PyPI 包形式发布，版本更新频繁并附详细变更日志。

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

- 支持 GPTQ/AWQ/RTN/QQQ/EXL3/GGUF/FP8/MACaQ 等多种量化方法
- 覆盖 CUDA、ROCm、MLX/Metal、XPU、Tenstorrent、昇腾 NPU 与 CPU 的硬件加速路径
- 校准、量化、评估、转换、加速推理一体化工作流
- Quantization accuracy：SmoothMSE 等校准算法持续迭代

## 适用场景

- 将大模型压缩为低比特 checkpoint 以降低显存占用
- 为不同硬件平台（NVIDIA/AMD/Apple/NPU）生成对应量化格式
- 量化前用校准数据集评估模型质量损失

## 场景标签

`模型量化` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3:  An extensible platform for LLM quantization. Compress, evaluate, and run models across supported GPUs, accelerators
> L74: GPT-QModel brings calibration, quantization, evaluation, conversion, and accelerated

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
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `66930204ef0b` · [字段定义](../../DATASET.md)*
