# intel/neural-compressor

⭐ 2,734 · Python · Apache-2.0 · 推送 2026-11-23 · [GitHub](https://github.com/intel/neural-compressor) · [官网](https://intel.github.io/neural-compressor/) · 组织维护

**面向开发者的模型压缩库：量化/剪枝/蒸馏与低比特支持**

Intel 开源的 Python 模型压缩库，提供静态/动态量化、SmoothQuant、Weight-Only、量化感知训练、混合精度、剪枝与稀疏化等技术，支持 LLM/VLM（LLaMA、Qwen、DeepSeek 等）的 INT8/FP8/MXFP8/INT4/MXFP4/NVFP4 低比特量化，通过集成 AutoRound 支持多种量化方法。运行在 PyTorch 与 JAX 后端，覆盖 Intel Gaudi/CPU/GPU 及有限测试的 AMD/ARM/NVIDIA 硬件，通过 pypi 包与 Docker 镜像安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 INT8/FP8/MXFP8/INT4/MXFP4/NVFP4 多种低比特数据类型
- 通过 AutoRound 集成支持 LLaMA、Qwen、DeepSeek 等 LLM/VLM 量化
- 覆盖 Intel Gaudi 加速器、Core Ultra、Xeon 等多款 Intel 硬件
- 提供 PyTorch/JAX 扩展 API、Transformers 风格 API 与自动调优模块

## 适用场景

- 对部署在 Intel Xeon/Gaudi 上的大模型做低比特量化推理
- 在有限资源上压缩 PyTorch 模型以降低内存与推理开销
- 用自动调优在精度约束下搜索量化策略
- 在 Intel Core Ultra 本地环境部署量化后的 LLM/VLM

## 场景标签

`模型量化` · 领域:训练与推理

## 证据(README 行号)

> L2:  An open-source Python library supporting popular model compression techniques on mainstream deep learning framework
> L14: Intel® Neural Compressor aims to provide popular model compression techniques such as Static Quantization, Dynamic 
> L17: across diverse quantization techniques and low-precision data types through integration with AutoRound.

## 星数曲线

```mermaid
xychart-beta
    title "intel/neural-compressor 星数(近 14 点)"
    x-axis ["2026-10-22", "2026-10-23", "2026-10-26", "2026-10-27", "2026-10-28", "2026-11-06", "2026-11-08", "2026-11-11", "2026-11-13", "2026-11-14", "2026-11-20", "2026-11-21", "2026-11-23", "2026-11-25"]
    y-axis "stars" 2721 --> 2735
    line [2722, 2723, 2724, 2727, 2729, 2723, 2729, 2730, 2731, 2732, 2731, 2733, 2734, 2734]
```

2026-10-22 2,722 → 2026-11-25 2,734（+12）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `afe3b6669c7a` · [字段定义](../../DATASET.md)*
