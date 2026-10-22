# iamalexkorotin/NeuralOptimalTransport

⭐ 239 · Jupyter Notebook · MIT · 推送 2026-05-04 · [GitHub](https://github.com/iamalexkorotin/NeuralOptimalTransport) · [官网](https://openreview.net/forum?id=d8CBRlWNkqH) · 个人维护

**ICLR 2023 论文 Neural Optimal Transport 的 PyTorch 官方实现**

论文 Neural Optimal Transport（ICLR 2023 Spotlight）的官方 PyTorch 实现，用于在高维空间中用神经网络计算强/弱传输代价下的最优传输映射与方案。提供 1D/2D 玩具实验与非配对图像到图像翻译（一对一/一对多）的 Jupyter notebook，支持多 GPU。作者自称相比 GAN/扩散类翻译模型提供可控的多样性参数 γ 与更好的可解释性。实验在 torch 1.9.0 与 1-4 块 Tesla V100 上测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 计算强/弱传输代价下的高维最优传输映射与方案
- 非配对图像翻译实验（一对一 strong、一对多 weak）
- 弱二次代价单参数 γ 控制生成多样性
- GPU 实现并支持多 GPU，实验以 Jupyter notebook 形式提供

## 适用场景

- 复现论文中的最优传输实验
- 做非配对图像到图像翻译研究
- 学习强弱传输代价下的神经最优传输方法

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L2: This is the official `Python` implementation of the ICLR 2023 spotlight paper **Neural Optimal Transport** (NOT pape
> L4: The repository contains reproducible `PyTorch` source code for computing **optimal transport** (OT) **maps and plans

## 星数曲线

```mermaid
xychart-beta
    title "iamalexkorotin/NeuralOptimalTransport 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 238 --> 240
    line [239, 239]
```

2026-10-18 239 → 2026-10-22 239（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `7599e663e53e` · [字段定义](../../DATASET.md)*
