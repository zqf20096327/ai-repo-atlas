# cgbur/llama2.zig

⭐ 224 · Zig · MIT · 推送 2026-08-02 · [GitHub](https://github.com/cgbur/llama2.zig) · 个人维护

**单文件纯 Zig 的 Llama 2 推理实现**

llama2.c 的 Zig 移植版，在单个文件中以纯 Zig 实现 Llama 2 架构的模型推理：支持 checkpoint 加载、BPE 分词与 prompt、温度控制、top-p 采样、序列长度控制、自定义分词器与 multiquery。核心函数使用 Zig @Vector 的 SIMD 实现以提升吞吐；基准测试在 AMD Ryzen 9 5900X 上与 llama2.c、llama2.rs 对比。当前不支持多线程；NVIDIA GPU 实现在 CUDA 分支。面向 Zig 0.16.0，从源码构建运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单文件纯 Zig 实现 Llama 2 推理，支持温度/top-p 采样与 BPE 分词
- 基于 Zig @Vector 的 SIMD 矩阵乘法提升吞吐
- 提供与 llama2.c / llama2.rs 的单线程基准对比
- NVIDIA GPU 实现位于 CUDA 分支

## 适用场景

- 研究/学习 Llama 2 推理的简化实现
- 在 CPU 上运行 Llama 2 checkpoint 做文本生成
- 对比不同语言单文件推理实现的性能

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L6: Andrej Karpathy. It runs inference for the
> L12: - Inference of llama2 model checkpoints

## 星数曲线

```mermaid
xychart-beta
    title "cgbur/llama2.zig 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 223 --> 225
    line [224, 224]
```

2026-10-18 224 → 2026-10-28 224（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `8607da7dc9db` · [字段定义](../../DATASET.md)*
