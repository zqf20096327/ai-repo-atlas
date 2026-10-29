# lablup/backend.ai-kernels

⭐ 35 · Jupyter Notebook · LGPL-3.0 · 推送 2026-10-19 · [GitHub](https://github.com/lablup/backend.ai-kernels) · [官网](https://www.backend.ai) · 组织维护

**Backend.AI 容器内核配方仓库：多语言与深度学习镜像清单**

Lablup 维护的 Backend.AI agent 内核容器配方仓库，列出官方支持镜像：深度学习框架镜像（TensorFlow/PyTorch/CNTK/MXNet 及 All-in-one 环境）、NGC（Nvidia GPU Cloud）系列镜像、社区维护的 13 种编程语言内核（C/C++/Go/Rust/Python/R 等），以及基于 Intel MKL、Nvidia CUDA、Google TPU、AMD ROCm 的底层变体镜像。表格标注各镜像的 Batch/Query/Input Hook/TTY 支持情况。以 Docker 镜像配方形式供 Backend.AI 平台使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | LGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖 TensorFlow/PyTorch/CNTK/MXNet 的多版本深度学习镜像
- NGC 系列 TensorFlow/PyTorch/MXNet/MATLAB 镜像
- 13 种社区维护编程语言内核（C/Go/Rust/R/Scala 等）
- MKL/CUDA/TPU/ROCm 四类硬件后端基础镜像变体

## 适用场景

- 为 Backend.AI 部署查找可用的计算内核镜像
- 了解某框架版本在 Batch/Query/TTY 模式下的支持情况
- 按硬件（CPU/CUDA/TPU/ROCm）选择对应基础镜像

## 场景标签

 · 领域:AI 计算基础设施/容器镜像

## 证据(README 行号)

> L1: # Backend.AI Kernels Repository
> L3: Backend.AI agent kernels in various programming languages / toolkits and frameworks.

## 星数曲线

```mermaid
xychart-beta
    title "lablup/backend.ai-kernels 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-29"]
    y-axis "stars" 33 --> 36
    line [34, 35, 35]
```

2026-10-18 34 → 2026-10-29 35（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `cd5d7b6bd006` · [字段定义](../../DATASET.md)*
