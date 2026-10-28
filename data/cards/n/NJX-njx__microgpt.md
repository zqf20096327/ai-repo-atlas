# NJX-njx/microgpt

⭐ 22 · HTML · 推送 2026-03-05 · [GitHub](https://github.com/NJX-njx/microgpt) · [官网](https://njx-njx.github.io/microgpt/microgpt_optimized.html) · 个人维护

**265 行纯 Python 与 CUDA 双实现的 GPT-2 教学参考**

提供两份对齐的最小 GPT 实现：microgpt.py 为纯 Python、零依赖的参考实现；microgpt_cuda.cu 为面向 Windows（MSVC + CUDA）的 CUDA/C++ 实现，保持相同模型与训练逻辑并通过 GPU 常驻与内核融合提升性能。训练配方含字符级 tokenizer、RMSNorm、因果多头注意力、ReLU^2 MLP、权重绑定与 AdamW。面向想从零理解 LLM 内部机制的读者，附 HTML 页面并列对照两份代码。限制：融合实现当前仅支持 n_layer=1，CUDA 词表上限 256。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 纯 Python 与 CUDA/C++ 双实现对齐，算法一致
- 训练步骤融合为单次 kernel 启动（前向+反向+梯度裁剪+AdamW）
- HTML 转换器页面支持 Python/CUDA 双语并列对照
- 零依赖：Python 路径直接 python microgpt.py 运行

## 适用场景

- 从零逐行理解 GPT 模型与训练的内部机制
- 学习 CUDA kernel 融合与 GPU 常驻优化手法
- 对照阅读同一算法在 Python 与 CUDA 中的表达

## 场景标签

`教程课程` `模型训练` · 领域:学习与行业

## 证据(README 行号)

> L5: A minimal GPT project with two aligned implementations:
> L7: - `microgpt.py`: pure Python, dependency-free reference implementation.
> L22: - Train/val split, periodic validation, top-k sampling inference.

## 星数曲线

```mermaid
xychart-beta
    title "NJX-njx/microgpt 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-28 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `b6c43180af40` · [字段定义](../../DATASET.md)*
