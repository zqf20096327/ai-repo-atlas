# ProbioticFarmer/mlx-deterministic

⭐ 10 · Python · MIT · 推送 2025-12-12 · [GitHub](https://github.com/ProbioticFarmer/mlx-deterministic) · 个人维护

**为 MLX 提供批量不变算子，使 Apple Silicon 上 LLM 推理结果确定**

基于 Apple MLX 的 Python 库，针对同一 prompt 在不同 batch size 下输出不一致的问题，提供 RMSNorm、矩阵乘、Attention、Softmax 的批量不变实现。提供两种模式：Python 包装（复用 mx.matmul，误差 ~1e-5，开销 +27-32%）与自研 Metal 内核（FP32/FP16，bitwise 级 0.0 差异）。附 87 项测试、确定性验证脚本与热感知基准套件，基于 Thinking Machines Labs 的研究。仅面向 Apple Silicon，README 定位为研究代码。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 批量不变的 RMSNorm/Matmul/Attention/Softmax 实现
- 自定义 Metal 内核实现 bitwise 级确定性（FP32/FP16）
- determinism_check.py 脚本可在真实模型上验证批量不变性
- 热感知基准模式采用交错测试与中位数报告

## 适用场景

- 需要可复现基准与回归测试的 LLM 推理验证
- 合规/审计场景要求推理输出逐位一致
- 在 Apple Silicon 上调试 batch size 相关的输出漂移

## 场景标签

`推理引擎` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L8: **Batch-invariant operations for deterministic LLM inference on Apple Silicon using MLX.**
> L31: This library provides **batch-invariant** implementations of core operations:

## 星数曲线

```mermaid
xychart-beta
    title "ProbioticFarmer/mlx-deterministic 星数(近 2 点)"
    x-axis ["2026-10-19", "2026-11-21"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-19 10 → 2026-11-21 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `6b601eb54b89` · [字段定义](../../DATASET.md)*
