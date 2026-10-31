# itlab-vision/dl-benchmark

⭐ 36 · HTML · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/itlab-vision/dl-benchmark) · [官网](http://hpc-education.unn.ru/dli) · 组织维护

**多框架深度学习推理性能基准测试工具**

DLI 测量多种深度学习模型在不同推理框架与硬件上的推理性能，支持 OpenVINO、TensorFlow、ONNX Runtime、PyTorch、ncnn、PaddlePaddle 等 17 种框架的 C++/Python API。仓库包含基准脚本、C++ 测量工具、精度检查、模型转换与量化脚本、各框架的 Dockerfile，以及历史测试与验证结果（html/xlsx）。测量方法参考 OpenVINO Benchmark C++ 工具。构建、部署与推理步骤见外部 Wiki。附多篇已发表论文可引用。

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

- 支持 17 种推理框架（OpenVINO/PyTorch/ONNX Runtime/ncnn/PaddlePaddle 等）
- C++ 与 Python 双实现，测量方法对齐 OpenVINO Benchmark 工具
- 提供各框架 Dockerfile 与远程执行基准脚本
- 包含精度检查、模型转换、量化（POT/TFLite/TVM）辅助工具

## 适用场景

- 对比多个推理框架在本机硬件上的模型推理性能
- 复现或引用 Intel CPU/集成显卡、RISC-V 平台的基准结果
- 验证各框架推理实现的正确性与模型精度

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L6: DLI is a benchmark for deep learning inference on various hardware.
> L18: DLI supports inference using the following frameworks:

## 星数曲线

```mermaid
xychart-beta
    title "itlab-vision/dl-benchmark 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-31 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `b22dee9549f7` · [字段定义](../../DATASET.md)*
