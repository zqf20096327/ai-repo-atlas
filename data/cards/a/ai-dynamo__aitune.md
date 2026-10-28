# ai-dynamo/aitune

⭐ 289 · Python · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/ai-dynamo/aitune) · [官网](https://docs.nvidia.com/aitune) · 组织维护

**为 PyTorch 模型自动调优推理后端的 NVIDIA GPU 工具包**

NVIDIA 维护的推理调优工具包：针对 PyTorch 模型与流水线，在各 nn.Module 级别评估多种后端候选（含 PTQ、kernel 选择、CUDA graphs 等加速技术），做数值校验与性能测量后按吞吐/延迟/延迟预算策略选实现。提供 JIT 推理中调优与 AOT 生成 .ait 制品两种工作流，可复用于 Python、生成 Triton 模型仓库或经 Dynamo workers 部署。要求 Linux + NVIDIA GPU + 兼容 PyTorch/CUDA，附模型配方目录。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- nn.Module 级后端评估、数值校验与性能测量一体化工作流
- JIT 推理时调优与 AOT 可复用 .ait 制品两种模式
- 支持 PTQ、kernel 选择、CUDA graphs 等加速技术
- 可生成 Triton 模型仓库或经 Dynamo workers 部署

## 适用场景

- 为部署前的 PyTorch 模型自动选择推理后端与加速配置
- 在现有应用中开启 JIT 调优加速推理
- 生成可复用的调优制品并部署到 Triton/Dynamo

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L7: **NVIDIA AITune automates inference tuning for PyTorch models and pipelines on NVIDIA GPUs.**
> L8: It brings inference engines and acceleration techniques together under a single, extensible API. AITune combines
> L9: backend evaluation, numerical validation, and performance measurement into one workflow, selecting implementations

## 星数曲线

```mermaid
xychart-beta
    title "ai-dynamo/aitune 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-28"]
    y-axis "stars" 287 --> 290
    line [288, 289, 289]
```

2026-10-18 288 → 2026-10-28 289（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `fc8cd2a18d0d` · [字段定义](../../DATASET.md)*
