# AmpereComputingAI/ampere_model_library

⭐ 23 · Python · Apache-2.0 · 推送 2026-02-26 · [GitHub](https://github.com/AmpereComputingAI/ampere_model_library) · [官网](https://hub.docker.com/u/amperecomputingai) · 组织维护

**面向开发者的 Ampere CPU AI 架构基准测试库**

Ampere Computing 维护的模型基准测试库，在 Ampere CPU 上运行和评测 ResNet-50、Whisper、DLRM、BERT large、YOLO v8、LLaMA2 7B 等多种 AI 架构。提供 benchmark.py 脚本快速评估系统性能，各架构按任务分类（计算机视觉、语音识别、自然语言处理）组织目录，每个模型有对应 run.py。使用方式为在 Ampere 优化框架（PyTorch/ONNX Runtime/TensorFlow）的 Docker 容器内克隆仓库并运行脚本，支持 FP32 与隐式 FP16 转换。限制：面向 Ampere CPU 硬件，部分模型（如 LLaMA2）需先获得 Meta 授权。

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

- benchmark.py 一键评估多架构性能（ResNet-50/Whisper/DLRM/BERT/YOLO v8）
- 覆盖计算机视觉、语音识别、自然语言处理等任务分类的模型目录
- 基于 Ampere 优化 PyTorch/ONNX Runtime/TensorFlow 的 Docker 镜像
- 支持隐式 FP16 转换与 AIO_NUM_THREADS 线程控制等调优变量

## 适用场景

- 评估 Ampere CPU 系统运行各 AI 架构的性能
- 在 Ampere 平台上复现 LLaMA2/BERT/ResNet 等模型的基准测试
- 参考结构化代码了解被测量的具体内容

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L9: AML's goal is to make benchmarking of various AI architectures on Ampere CPUs a pleasurable experience :)
> L38: ### The go-to solution is benchmark.py script

## 星数曲线

```mermaid
xychart-beta
    title "AmpereComputingAI/ampere_model_library 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-27 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `1e204a96b951` · [字段定义](../../DATASET.md)*
