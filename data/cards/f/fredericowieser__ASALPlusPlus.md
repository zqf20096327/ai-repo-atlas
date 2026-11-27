# fredericowieser/ASALPlusPlus

⭐ 10 · Python · 推送 2026-08-06 · [GitHub](https://github.com/fredericowieser/ASALPlusPlus) · 组织维护

**用多模态基础模型驱动人工生命开放式演化搜索的研究代码**

ASAL++ 扩展 ASAL 的监督目标机制：内层用 CLIP 与 Sep-CMA-ES 把 Lenia 等人工生命模拟优化到自然语言目标，外层由多模态 Evolver Model（论文中为 Gemma-3-4b-it）观看 rollout 视频并提出下一目标，热启动下一轮搜索。论文研究 EST 与 ETT 两种变体并给出开放式性得分的量化结果。仓库包含论文实验、消融、分支生命树、保留输出、notebook、固定版 JAX ASAL fork 与实验性 PyTorch Lenia 实现。安装需 Python 3.11、uv、CUDA GPU、Hugging Face 访问 Gemma 权重与 FFmpeg。

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

- 外层 Evolver Model 自动生成目标序列，内层 CLIP+Sep-CMA-ES 热启动搜索
- EST 与 ETT 两种目标演化变体，在 Lenia 上报告 OE 量化结果
- 含固定版 JAX ASAL fork（Boids/Particle Life/神经元胞自动机等多种底物）与实验性 PyTorch Lenia 实现
- 方法对底层人工生命底物不可知，只需参数化模拟与 2D 渲染

## 适用场景

- 复现论文中基于视觉-语言模型的人工生命开放式演化实验
- 在 Lenia 等底物上研究自动生成目标序列的搜索方法
- 替换底物或 Evolver 模型做相关消融研究

## 场景标签

`多模态` · 领域:感知与多模态

## 证据(README 行号)

> L15: **ASAL++** extends the supervised-target mechanism in Automated Search for Artificial Life (ASAL) from fixed, human
> L17: The paper studies two variants in Lenia using Gemma-3-4b-it:
> L22: The repository contains the paper experiments, ablations, branching “trees of life”, preserved outputs, exploratory

## 星数曲线

```mermaid
xychart-beta
    title "fredericowieser/ASALPlusPlus 星数(近 2 点)"
    x-axis ["2026-10-25", "2026-11-27"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-25 10 → 2026-11-27 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `95bc8151c6c1` · [字段定义](../../DATASET.md)*
