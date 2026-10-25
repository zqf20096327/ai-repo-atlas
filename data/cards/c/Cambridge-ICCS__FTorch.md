# Cambridge-ICCS/FTorch

⭐ 208 · Fortran · MIT · 推送 2026-10-16 · [GitHub](https://github.com/Cambridge-ICCS/FTorch) · [官网](https://cambridge-iccs.github.io/FTorch/) · 组织维护

**让 Fortran 代码直接调用 PyTorch 模型的互操作库**

由剑桥 ICCS 维护的 Fortran 库，通过 LibTorch 将 PyTorch 训练的模型以 TorchScript 形式耦合进 Fortran 代码运行。用户流程：将模型保存为 TorchScript、用 FTorch 的 Fortran 绑定调用、编译链接该库。支持 CPU 与多种 GPU 后端（CUDA/HIP/MPS/XPU），在 UNIX 与 Windows 上测试。需 CMake≥3.18 及 Fortran 2008、C++20、C 编译器，从源码构建安装，附示例与测试套件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从 Fortran 直接调用 PyTorch TorchScript 模型
- 支持 CUDA/HIP/MPS/XPU 多种 GPU 后端与多设备
- 在 UNIX 与 Windows 系统上测试
- 提供示例目录与 pFUnit 单元/集成测试

## 适用场景

- Fortran 科学计算代码中嵌入 PyTorch 训练的模型做推理
- 将已有 ML 模型耦合到 Fortran 数值模拟流程
- 在 GPU 集群上运行 Fortran 调用的深度学习模型

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L10: This repository contains code, utilities, and examples for directly using PyTorch ML
> L31: FTorch is a library enabling users to directly couple their PyTorch models to Fortran code.

## 星数曲线

```mermaid
xychart-beta
    title "Cambridge-ICCS/FTorch 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-25"]
    y-axis "stars" 206 --> 209
    line [207, 208, 208]
```

2026-10-18 207 → 2026-10-25 208（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `eafdd3693937` · [字段定义](../../DATASET.md)*
