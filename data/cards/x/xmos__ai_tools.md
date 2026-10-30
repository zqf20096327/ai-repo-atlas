# xmos/ai_tools

⭐ 30 · C++ · NOASSERTION · 推送 2026-10-29 · [GitHub](https://github.com/xmos/ai_tools) · 组织维护

**面向 XMOS XCORE.AI 芯片的 TFLite 模型转换与主机解释器工具**

XMOS 官方提供的 Python 工具包，包含 MLIR 图变换器 xformer：读取 Tensorflow Lite 模型，针对 XCORE.AI 边缘芯片做优化，生成优化后模型、可编译到 xcore 目标的 C++ 源码/头文件，并可选用生成权重 flash 镜像；另含 TFLM 主机解释器，可在开发机上直接运行转换后模型验证输出。以 pip 安装使用，面向在 XCORE.AI 硬件上部署 TFLite 模型的嵌入式开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- xformer 基于 MLIR 将 TFLite 模型优化为 XCore 格式
- 转换可生成 C++ 源码/头文件与权重 flash 镜像
- TFLMHostInterpreter 在主机上运行转换后的模型
- 提供 tensor arena 大小查询与优化报告输出

## 适用场景

- 把 Tensorflow Lite 模型部署到 XCORE.AI 边缘硬件
- 在主机上先行验证模型转换与推理结果
- 生成带 flash 权重的模型用于目标板加载

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L22: * the MLIR-based XCore optimizer(xformer) to optimize Tensorflow Lite models for XCore
> L23: * the XCore tflm interpreter to run the transformed models on host

## 星数曲线

```mermaid
xychart-beta
    title "xmos/ai_tools 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-30 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `895a927ecce5` · [字段定义](../../DATASET.md)*
