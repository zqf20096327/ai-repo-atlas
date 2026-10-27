# triton-inference-server/model_navigator

⭐ 226 · Python · Apache-2.0 · 推送 2026-05-27 · [GitHub](https://github.com/triton-inference-server/model_navigator) · [官网](https://triton-inference-server.github.io/model_navigator/) · 组织维护

**深度学习模型优化部署工具包：转 TensorRT 并部署 Triton**

NVIDIA 维护的推理工具包，将 PyTorch、TensorFlow、ONNX 模型与 Python 流水线转换/优化为 TensorRT 与 Torch-TensorRT 格式，自动完成导出、转换、正确性验证与性能剖析，按延迟/吞吐指标选取最优格式，并通过专用 API 部署到 PyTriton 或 Triton Inference Server。提供 nav.optimize 单行优化入口与静态 batch 剖析功能。限制：要求 Linux、Python 3.9+ 与 NVIDIA GPU，剖析仅支持静态 batch 场景。

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

- 单行代码 nav.optimize 运行多框架优化路径
- 自动导出、转换、正确性验证与性能剖析
- 按延迟/吞吐指标选取最优部署格式
- 通过专用 API 部署到 PyTriton 与 Triton Inference Server

## 适用场景

- 我把 PyTorch/TF/ONNX 模型转成 TensorRT 以加速推理
- 我需要剖析模型选出延迟最优的部署格式
- 我想把优化后的模型打包部署到 Triton

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: Welcome to Triton Model Navigator, an inference toolkit designed
> L9: The Triton Model Navigator automates several critical steps, including model export, conversion, correctness testing
> L12: either PyTriton

## 星数曲线

```mermaid
xychart-beta
    title "triton-inference-server/model_navigator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 225 --> 227
    line [226, 226]
```

2026-10-18 226 → 2026-10-27 226（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `c5e02761832a` · [字段定义](../../DATASET.md)*
