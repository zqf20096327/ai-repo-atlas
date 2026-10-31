# foundation-model-stack/fms-model-optimizer

⭐ 21 · Python · Apache-2.0 · 推送 2026-10-08 · [GitHub](https://github.com/foundation-model-stack/fms-model-optimizer) · 组织维护

**神经网络模型量化压缩框架，面向开发低精度模型**

FMS Model Optimizer（fms-model-optimizer）是用于开发低精度神经网络的 Python 量化框架，支持 QAT、PTQ、GPTQ、FP8 等技术，内置 SmoothQuant、SAWB+、PACT+ 等量化方法，覆盖 Conv2d、Linear、LSTM、MM/BMM 等计算密集算子，已在视觉/语音/NLP/目标检测/LLM 上验证 INT 8/4-bit 量化。支持 Granite、Llama、Mixtral、BERT/Roberta 等模型。要求 Linux + NVIDIA GPU（V100/A100/H100）、Python 3.10-3.12、CUDA>=12；通过 pip 或源码安装，可选依赖按功能分组（fp8/gptq/mx 等）。由 foundation-model-stack 组织维护。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 QAT/PTQ/GPTQ/FP8 等量化技术与 SmoothQuant、SAWB+、PACT+ 方法
- 支持 Granite/Llama/Mixtral/BERT 等模型的量化（含支持矩阵）
- Python API，少量代码即可完成模块级/函数级算子替换
- 可选依赖分组安装（fp8/gptq/mx/data 等）并提供 Jupyter 教程与脚本示例

## 适用场景

- 对 LLM 做 GPTQ/FP8 后训练量化以压缩部署
- 在训练流程中加入量化感知训练（QAT）
- 通过 Python API 分析网络并做层级精度设置

## 场景标签

`模型量化` · 领域:训练与推理

## 证据(README 行号)

> L12: FMS Model Optimizer is a framework for developing reduced precision neural network models. Quantization techniques,
> L16: - **Python API to enable model quantization:** With the addition of a few lines of codes, module-level and/or funct

## 星数曲线

```mermaid
xychart-beta
    title "foundation-model-stack/fms-model-optimizer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-31 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `3d77841136ed` · [字段定义](../../DATASET.md)*
