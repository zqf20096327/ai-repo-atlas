# Marco-Christiani/Zigrad

⭐ 197 · Zig · LGPL-3.0 · 推送 2026-10-07 · [GitHub](https://github.com/Marco-Christiani/Zigrad) · [官网](http://zigrad.datatician.io/) · 个人维护

**Zig 编写的深度学习框架，基于自动微分引擎**

用 Zig 实现的深度学习框架，底层为通用 n 维自动微分引擎，提供类 PyTorch 的高层抽象与动态计算图，同时支持逐步下探到底层原语、内存与性能优化，面向希望在同一框架内完成研究原型到大规模训练过渡的研究者与工程师。支持计算图追踪与可视化，集成 Tensorboard 与 Mujoco，可在内存受限的边缘硬件上学习。目前正经历重写，公开版本计划于 2026 年 Q4 发布，API 会变动，卷积、池化等层仅为验证性实现，文档尚不完整。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | LGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 通用 n 维自动微分引擎，动态计算图与计算图追踪/可视化
- 类 PyTorch 的高层抽象，可逐步下探到底层原语与内存控制
- 唯一依赖为 BLAS 库，Apple Silicon 无需额外依赖
- 支持在 SWAP 受限的边缘硬件上学习

## 适用场景

- 在研究中用高层抽象快速原型神经网络
- 将研究代码过渡到大规模训练基础设施而不切换框架
- 在内存受限的边缘设备上训练模型

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L13: AI frameworks optimized for rapid research iteration do not seamlessly transition into the infrastructure required 
> L37: - A general purpose automatic differentiation system for n-dimensional data

## 星数曲线

```mermaid
xychart-beta
    title "Marco-Christiani/Zigrad 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 196 --> 198
    line [197, 197]
```

2026-10-18 197 → 2026-10-24 197（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `6e12aa85d152` · [字段定义](../../DATASET.md)*
