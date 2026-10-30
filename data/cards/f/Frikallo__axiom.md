# Frikallo/axiom

⭐ 115 · C++ · MIT · 推送 2026-05-29 · [GitHub](https://github.com/Frikallo/axiom) · [官网](https://axiom-cpp.readthedocs.io) · 个人维护

**C++ 张量库：为 C++ 提供 NumPy/PyTorch 风格 API**

开源 C++20 张量计算库，API 设计对齐 NumPy 与 PyTorch（运算符重载、链式调用、同名函数），供需要原生性能的研究者与工程师使用。核心机制：惰性计算，操作先构建计算图，按需物化，由图编译器自动融合算子并复用缓冲区；支持多设备（CPU 与 Metal GPU，API 一致），Apple Silicon 上 CPU/GPU 张量共享物理内存，设备切换零拷贝；SIMD 向量化与 BLAS 加速。跨 macOS/Linux/Windows，MIT 许可。GPU 后端目前为 Metal，非 Apple 平台的 GPU 支持未在 README 中说明。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 惰性计算图，编译器自动融合算子并复用缓冲区
- CPU 与 Metal GPU 统一 API，所有算子可在 GPU 运行
- Apple Silicon 上 CPU/GPU 统一内存，设备切换零拷贝
- 跨平台（macOS/Linux/Windows），CMake FetchContent 可直接引入

## 适用场景

- 在 C++ 项目中做张量运算而不依赖 Python 环境
- 在 Apple Silicon 上利用 Metal GPU 与统一内存做数值计算
- 已有 NumPy/PyTorch 经验的开发者迁移到 C++ 原生代码

## 场景标签

 · 领域:机器学习/数值计算库

## 证据(README 行号)

> L5: **Axiom** is an open-source, high-performance C++ tensor library that brings NumPy and PyTorch simplicity to native 
> L20:  * ... **Multi-device**: Operations can run on any supported device — currently CPU and Metal GPU, with more coming

## 星数曲线

```mermaid
xychart-beta
    title "Frikallo/axiom 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 114 --> 116
    line [115, 115]
```

2026-10-18 115 → 2026-10-30 115（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `98cadc49333a` · [字段定义](../../DATASET.md)*
