# prescient-design/holo-bench

⭐ 24 · Python · MIT · 推送 2026-04-15 · [GitHub](https://github.com/prescient-design/holo-bench) · 组织维护

**生物物理序列优化算法的基准测试库**

面向生物物理（如蛋白质）序列优化算法的基准测试工具：提供闭式测试函数（如 Ehrlich）、离散进化优化器等组件，用户通过导入 holo 模块或运行 benchmark_optimizer.py 脚本对黑盒优化算法进行评测。以 pip 包 pytorch-holo 形式发布，基于 PyTorch，配套论文为 Closed-Form Test Functions for Biophysical Optimization Algorithms，实验可经 Weights & Biases 复现。主要面向算法研究者。

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

- 提供闭式测试函数（如 Ehrlich）用于评测
- 内置离散进化优化器 DiscreteEvolution
- 附带 benchmark_optimizer.py 基准脚本
- 配套论文与 Weights & Biases 实验仪表板

## 适用场景

- 评测离散序列优化算法在生物物理问题上的表现
- 在蛋白质设计优化研究中做算法对比
- 复现论文中的基准实验

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L2: ### Benchmarking Discrete Sequence Optimization Algorithms
> L45: If you use HoloBench in your research, please cite the following paper:

## 星数曲线

```mermaid
xychart-beta
    title "prescient-design/holo-bench 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-28 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `407a8c2eae06` · [字段定义](../../DATASET.md)*
