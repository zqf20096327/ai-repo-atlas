# Oabraham1/chronos

⭐ 28 · C++ · Apache-2.0 · 推送 2025-12-16 · [GitHub](https://github.com/Oabraham1/chronos) · [官网](https://oabraham1.github.io/chronos/) · 个人维护

**基于时间的 GPU 分区共享工具：多用户限时独占单块 GPU**

以 OpenCL 构建的 GPU 时间分区工具，通过创建有时限、自动过期的独占分区让多用户/多应用共享单块 GPU。支持 NVIDIA MPS 并发模式与 OpenCL 时间片模式，跨 NVIDIA/AMD/Intel/Apple Silicon GPU 与 Linux/macOS/Windows。提供 Python API 与 CLI，由 C++ 核心与后端选择器组成，分区创建延迟 3.2ms、GPU 开销 <1%（RTX 3080 基准）。面向共用 GPU 的研究实验室、小团队与高校场景。

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

- 时间限定的 GPU 分区，自动过期与清理
- 双后端：NVIDIA MPS 并发模式与 OpenCL 时间片跨厂商模式
- 提供 Python API、CLI 与 pip/Docker/源码多种安装途径
- 分区创建 3.2ms、GPU 计算开销 0.8%（RTX 3080 基准）

## 适用场景

- 实验室里多个成员公平共享一块 GPU 做训练
- Jupyter Notebook / 训练脚本中限时占用 GPU 并自动释放
- 在 AMD/Intel/Apple Silicon 等 GPU 上做跨厂商资源分配

## 场景标签

 · 领域:GPU 资源管理/HPC

## 证据(README 行号)

> L10: > **Time-based GPU partitioning with automatic expiration**
> L90: - **Any GPU**: NVIDIA, AMD, Intel, Apple Silicon
> L94: ### 🎓 Perfect For

## 星数曲线

```mermaid
xychart-beta
    title "Oabraham1/chronos 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-26 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `ba4458928a6e` · [字段定义](../../DATASET.md)*
