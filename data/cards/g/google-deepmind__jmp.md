# google-deepmind/jmp

⭐ 214 · Python · Apache-2.0 · 推送 2026-10-05 · [GitHub](https://github.com/google-deepmind/jmp) · 组织维护

**JAX 混合精度训练库：提供精度策略与损失缩放抽象**

DeepMind JAX 生态的混合精度训练库，通过两个抽象（Policy 与 LossScale）简化 f32/f16/bf16 混合精度训练：策略定义参数/计算/输出 dtype 并可对 pytree 做类型转换，损失缩放支持静态、动态与 no-op 三种模式以避免梯度下溢。面向使用 JAX（含 Haiku 等神经网络库）的开发者，纯 Python 实现但依赖 JAX/NumPy 的 C++ 代码，JAX 需按加速器自行安装，且未列入 requirements.txt。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Policy 抽象可指定 param/compute/output dtype 并转换 pytree
- 支持静态/动态/no-op 三种损失缩放，动态模式自动调整 S 值
- 可通过字符串（如 "half"）以命令行参数形式指定策略
- Haiku 等神经网络库可集成以提供 AMP 支持

## 适用场景

- 在 JAX 训练中降低显存带宽占用、提升计算效率
- 用 f32/f16 在 GPU 或 f32/bf16 在 TPU 上缩减训练时间
- 为自定义 JAX 网络库增加自动混合精度能力

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L18: This library implements support for mixed precision training in [JAX] by providing
> L20: network libraries (such as [Haiku]) can integrate with `jmp` and provide

## 星数曲线

```mermaid
xychart-beta
    title "google-deepmind/jmp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 213 --> 215
    line [214, 214]
```

2026-10-18 214 → 2026-10-31 214（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `20ce280469b6` · [字段定义](../../DATASET.md)*
