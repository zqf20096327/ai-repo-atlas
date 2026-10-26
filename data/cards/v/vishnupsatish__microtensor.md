# vishnupsatish/microtensor

⭐ 91 · C++ · MIT · 推送 2026-02-08 · [GitHub](https://github.com/vishnupsatish/microtensor) · 个人维护

**从零实现的 C++ 深度学习库，含训练推理与 GPT-2 实现**

用 C++20 从零编写的张量与深度学习库，无外部依赖。提供张量库（strided views、内存偏移、OpenMP 并行）、自动微分引擎、SGD/AdamW 优化器、多头自注意力与 GPT-2 实现、支持训练与分词的 BPE 实现。张量库与梯度通过对 PyTorch 的差分测试验证。构建使用 CMake 与 make，主要在 macOS 上以 Apple Clang 和 G++ 测试。未来目标包括权重保存、Python 绑定与 GPU 加速，当前部分能力（如需梯度的梯度）尚未支持。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从零实现的 C++20 张量库与自动微分引擎，无外部依赖
- 内置 GPT-2 完整实现，可在训练中 SIGINT 触发推理
- BPE 分词器实现，token 合并以 O(k log n) 时间完成
- 张量与梯度计算对 PyTorch 做差分测试

## 适用场景

- 学习从零实现深度学习框架与 GPT-2 的内部机制
- 在无外部依赖的 C++ 环境中训练与推理小型模型
- 参考其差分测试方法验证自定义张量/梯度实现

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L3: Supports training and inference. No external dependencies.
> L16: - Multi-headed self-attention, transformer, and GPT-2 implementation

## 星数曲线

```mermaid
xychart-beta
    title "vishnupsatish/microtensor 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 90 --> 92
    line [91, 91]
```

2026-10-18 91 → 2026-10-26 91（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `484a46892378` · [字段定义](../../DATASET.md)*
