# NVIDIA/TorchFort

⭐ 198 · C++ · Apache-2.0 · 推送 2026-08-19 · [GitHub](https://github.com/NVIDIA/TorchFort) · [官网](https://nvidia.github.io/TorchFort/) · 组织维护

**面向 HPC 的 DL 训练/推理接口库：Fortran/C++ 直接调用 PyTorch**

基于 LibTorch（PyTorch 的 C++ 后端）实现的深度学习训练与推理接口库，面向 HPC 从业者与领域科学家，用于将 PyTorch 的深度学习能力嵌入仿真程序。可从 Fortran 或 C/C++ 程序直接调用，在仿真进程内共享数据数组，无需外部胶水或数据共享代码；支持加载 TorchScript 导出的模型定义，训练流程（优化器、损失函数、学习率调度等）通过 YAML 配置文件控制。面向 NVIDIA GPU，构建与用法见其文档，Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从 Fortran/C/C++ 程序直接调用，进程内共享数据数组
- 加载 TorchScript 导出的 PyTorch 模型定义
- YAML 配置优化器、损失与学习率调度

## 适用场景

- 在数值仿真程序中嵌入深度学习训练或推理
- 领域科学家在自有求解器中复用 PyTorch 模型能力
- HPC 代码与 DL 框架间的无胶水数据共享

## 场景标签

`模型训练` `推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L6: TorchFort is a DL training and inference interface for HPC programs implemented using LibTorch, the C++ backend used
> L9: This library can be invoked directly from Fortran or C/C++ programs, enabling transparent sharing of data arrays to 

## 星数曲线

```mermaid
xychart-beta
    title "NVIDIA/TorchFort 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 197 --> 199
    line [198, 198]
```

2026-10-18 198 → 2026-10-26 198（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `8eb01596e726` · [字段定义](../../DATASET.md)*
