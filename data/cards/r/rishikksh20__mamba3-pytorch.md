# rishikksh20/mamba3-pytorch

⭐ 41 · Python · 推送 2026-08-22 · [GitHub](https://github.com/rishikksh20/mamba3-pytorch) · 个人维护

**Mamba-3 选择性状态空间模型的 PyTorch 可读参考实现**

用纯 PyTorch 与 einops 从零实现 Mamba-3 序列模型，不含 Triton/CUDA/TileLang 自定义核，面向理解算法。覆盖论文的三个改进：指数梯形离散化（学习式 sigmoid 门混合 Euler 与梯形）、对 B/C 投影施加 RoPE 形成复值（旋转）状态结构、以及在同一 P×D 状态上复用 R 个流的 MIMO 形式。单文件 mamba3.py 提供 SISO/MIMO 扫描、自回归解码步、完整 LM 结构与配置类；顺序扫描为 O(L) 串行，非生产用并行核。运行 python3 mamba3.py 可执行前向与形状检查。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单文件自包含实现，含 Mamba3 模块、MambaLMHeadModel 与推理缓存分配
- 支持 SISO 与 MIMO 两种模式及逐 token 自回归解码
- 实现梯形离散化、复值 RoPE 状态、MIMO 三项论文改进
- 无自定义核，纯 PyTorch + einops，便于阅读与教学

## 适用场景

- 研究/学习 Mamba-3 算法原理与实现细节
- 在论文复现或消融实验中作为可读基线代码
- 验证 SISO/MIMO 状态形状与解码逻辑的正确性

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: A clean, readable, from-scratch PyTorch implementation of **Mamba-3** — a selective state space model that addresses
> L5: **Paper:** Mamba-3: Improved Sequence Modeling using State Space Principles

## 星数曲线

```mermaid
xychart-beta
    title "rishikksh20/mamba3-pytorch 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-25"]
    y-axis "stars" 39 --> 42
    line [40, 41, 41]
```

2026-10-18 40 → 2026-10-25 41（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `04f9b9e2aee5` · [字段定义](../../DATASET.md)*
