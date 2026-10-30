# egaoharu-kensei/flash-attention-triton

⭐ 33 · Python · MIT · 推送 2026-01-12 · [GitHub](https://github.com/egaoharu-kensei/flash-attention-triton) · 个人维护

**FlashAttention-2 的 Triton 跨平台实现，面向 Turing+ GPU**

基于 FlashAttention-2 论文的 Triton 算子实现，支持 Linux 和 Windows，覆盖 Turing 到 Blackwell 架构。提供双模式：legacy（确定性，序列并行关闭）与 modern（非确定性，更高性能），并针对 Turing (CC 7.5) 与 Ampere+ (CC 8.0+) 做硬件感知优化。支持同构与异构 GPU 集群自动选择配置，另提供 custom 配置模式用于旧架构或专用调优。通过 pip 以 legacy/modern extra 安装，需先装对应 PyTorch+CUDA；Windows 需 MSVC++ 14.42+ 运行库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- Triton 实现的 FlashAttention-2 算子，支持 Linux 与 Windows
- legacy/modern 双模式（确定性与高性能）
- Turing 至 Blackwell 架构的硬件感知优化与集群自动配置
- custom 配置模式用于旧架构或专用调优

## 适用场景

- 在 Turing+ GPU 上运行 FlashAttention-2 注意力计算
- 异构 GPU 集群场景下自动选择内核配置
- 为老架构或专用需求定制注意力内核参数

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L10: FlashAttention-2 Triton implementation based on Tri Dao's paper ["FlashAttention-2:
> L17: - Cross-platform support (Linux and Windows)

## 星数曲线

```mermaid
xychart-beta
    title "egaoharu-kensei/flash-attention-triton 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-30 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `f0c21c35c587` · [字段定义](../../DATASET.md)*
