# gher-uliege/DINCAE.jl

⭐ 37 · Julia · GPL-3.0 · 推送 2026-01-27 · [GitHub](https://github.com/gher-uliege/DINCAE.jl) · 组织维护

**重建卫星观测缺失数据的卷积自编码器神经网络（Julia 版）**

DINCAE.jl 是用 Julia 实现的数据插值卷积自编码器，用于重建卫星观测（如海表温度）中被云层等遮挡的缺失数据，并给出误差估计。本仓库为 DINCAE 的 Julia 移植版，原 Python 代码已停止维护；绘图与数据准备工具在独立的 DINCAE_utils.jl 仓库。建议在支持 CUDA（NVIDIA）或 ROCm（AMD）的 GPU 上运行，CPU 也可运行但较慢。通过 Julia Pkg 安装，需 Julia 1.9 及以上。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 重建卫星观测缺失数据并输出期望标准差误差估计
- 支持 NVIDIA CUDA 与 AMD ROCm GPU，可选 CPU 运行（较慢）
- 多变量重建（DINCAE 2.0，融合测高数据）
- 配套 DINCAE_utils.jl 提供绘图与数据准备工具

## 适用场景

- 重建海表温度卫星数据中的云遮挡缺口
- 叶绿素浓度等海洋遥感产品的缺失数据补全
- 融合多源卫星观测生成无缝数据集

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L9: DINCAE (Data-Interpolating Convolutional Auto-Encoder) is a neural network to reconstruct missing data in satellite 
> L17: * Barth, A., Alvera-Azcárate, A., Licer, M., & Beckers, J.-M. (2020). DINCAE 1.0: a convolutional neural network wi
> L25: DINCAE is intended to be used with a GPU with CUDA support (NVIDIA GPU) or with ROCm support (AMD GPU). The code ca

## 星数曲线

```mermaid
xychart-beta
    title "gher-uliege/DINCAE.jl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-27 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `c167b53aca84` · [字段定义](../../DATASET.md)*
