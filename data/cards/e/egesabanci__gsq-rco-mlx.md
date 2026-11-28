# egesabanci/gsq-rco-mlx

⭐ 4 · Python · 推送 2026-10-24 · [GitHub](https://github.com/egesabanci/gsq-rco-mlx) · [官网](https://konic.io/research/gsq-rco-mixed-precision-mlx) · 个人维护

**在 Apple Silicon 上用 MLX 做低比特 LLM 量化的论文复现库**

将 GSQ（Gumbel-Softmax 标量量化）与 RCO（黎曼约束优化比特分配）两篇论文移植到 MLX 框架，在 Qwen2.5-0.5B 上实现 3 比特级量化，提供 build-db、allocate、quantize、export、eval 五步流水线，支持断点续跑。README 记录了一次完整审计：修正了 23 项实现缺陷并给出修复提交号，结果以 WikiText-2 困惑度表呈现。限制包括仅覆盖单模型、单数据集、单 seed，且 GPU 上不可比特级复现。面向能在 Apple Silicon 上运行 Python 3.12 与 uv 的研究者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- GSQ+RCO 组合量化在 Qwen2.5-0.5B 上的完整可运行实现
- build-db/allocate/quantize/export/eval 各步独立命令且可断点续跑
- 记录 23 项审计发现及对应修复 commit，含前后对照数据
- README 逐条列出与论文参数的偏差（校准规模、组大小等）

## 适用场景

- 在 M 系列 Mac 上复现 GSQ 与 RCO 的低比特量化实验
- 为小模型生成约 3 比特并带组缩放的量化权重并导出
- 研究量化感知训练中比特分配与网格学习的组合效果

## 场景标签

`模型量化` · 领域:训练与推理

## 证据(README 行号)

> L3: This repository ports two quantization papers to Apple silicon with MLX. **GSQ** (Gumbel-Softmax scalar
> L47: `gsq-rco run` is resumable. Finished steps are skipped on a rerun. Each step is also its own command

## 星数曲线

```mermaid
xychart-beta
    title "egesabanci/gsq-rco-mlx 星数(近 3 点)"
    x-axis ["2026-11-25", "2026-11-26", "2026-11-28"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-25 3 → 2026-11-28 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `c2caf863410c` · [字段定义](../../DATASET.md)*
