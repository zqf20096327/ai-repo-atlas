# huggingface/hf-rocm-kernels

⭐ 24 · Python · Apache-2.0 · 推送 2026-09-23 · [GitHub](https://github.com/huggingface/hf-rocm-kernels) · 组织维护

**面向 AMD ROCm GPU 的 PyTorch 算子内核库及扩展指南**

Hugging Face 维护的 ROCm 设备优化 ML 内核库，以 CUDA/C++ 源码编写算子并通过 PyTorch 绑定暴露给 Python。安装需先确定 GPU 架构（仅测试过 gfx942/MI300），运行 install.sh 指定架构编译安装。README 详细说明新增算子的流程：编写源文件、加入 CMake 构建列表、声明 C 绑定、torch 绑定与 Python 封装。已集成进 vLLM。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PyTorch 算子内核，C++/CUDA 源码经 CMake 编译
- 支持自定义新增算子的完整流程文档
- 通过 ./install.sh 指定 GPU 架构（如 gfx942）编译安装
- 已集成进 vLLM

## 适用场景

- 在 AMD MI300 等 ROCm 硬件上运行优化 ML 内核
- 为 PyTorch 项目添加自定义 ROCm 算子
- 通过 vLLM 使用其中的内核

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L2: Optimized ML kernels for ROCm devices.
> L6: To install this package, you first need to find your GPU's architecture. For instance, __if you are using a MI300 GP

## 星数曲线

```mermaid
xychart-beta
    title "huggingface/hf-rocm-kernels 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-28 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `66d587358221` · [字段定义](../../DATASET.md)*
