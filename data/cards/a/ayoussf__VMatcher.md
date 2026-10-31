# ayoussf/VMatcher

⭐ 19 · Python · MIT · 推送 2026-06-01 · [GitHub](https://github.com/ayoussf/VMatcher) · 个人维护

**面向位姿估计的半稠密局部特征匹配深度学习模型**

混合 Mamba-Transformer 网络的半稠密局部特征匹配方法：将 Mamba 的选择性扫描机制与 Transformer 注意力结合，用于图像对之间的特征匹配与位姿估计场景。提供 demo 脚本（自动下载 base/tiny 预训练权重）、训练流程（基于 MegaDepth 199GB 数据集）及在 MegaDepth1500/ScanNet1500/HPatches 上的评测脚本。训练目前仅支持 batch size 为 1；代码库大量复用 ELoFTR。开发环境为 RTX 3090Ti + CUDA 11.8 + PyTorch 2.2.2。

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

- Mamba 选择性扫描与 Transformer 注意力混合架构
- Base 与 Tiny 两种模型变体，提供预训练权重下载
- demo 脚本自动下载 checkpoint，支持混合精度与推理优化模式
- 提供 MegaDepth 训练与三个基准数据集评测流程

## 适用场景

- 图像对间半稠密特征匹配用于位姿估计
- 在 MegaDepth1500/ScanNet1500/HPatches 上评测匹配性能
- 复现或基于 ELoFTR 代码库扩展特征匹配研究

## 场景标签

 · 领域:计算机视觉/特征匹配

## 证据(README 行号)

> L21: VMatcher is a hybrid Mamba‑Transformer network for semi‑dense local feature matching. It combines Mamba's efficient
> L135: - **GPU**: NVIDIA GeForce RTX 3090Ti

## 星数曲线

```mermaid
xychart-beta
    title "ayoussf/VMatcher 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `00c4f2a0b641` · [字段定义](../../DATASET.md)*
