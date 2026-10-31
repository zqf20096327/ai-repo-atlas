# humansensinglab/MVCHead

⭐ 28 · NOASSERTION · 推送 2026-06-01 · [GitHub](https://github.com/humansensinglab/MVCHead) · [官网](https://humansensinglab.github.io/MVCHead/) · 组织维护

**单视角图像生成多视角一致 3D 高斯头像的研究项目**

CVPR 2026 论文项目，作者来自卡内基梅隆大学。提出 MVCHead：单步状态空间模型，仅从随机采样的 2D 图像学习条件与无条件 3D 头部模型，不依赖多视角数据、3D 监督或中间视图生成；核心机制包括分层状态空间块（HiSS）、分层双向状态扫描（HiBiSS）与 SE(3) 多视角 Critic。同时发布 FaceGS-10K 数据集。代码、权重与数据集标注为 Coming Soon，尚未在 README 中提供安装方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 仅从 2D 图像学习，不需要多视角数据与 3D 监督
- HiSS 分层状态空间块由粗到细回归 3D Gaussians
- SE(3) 多视角 Critic 在无真实多视角对的情况下奖励跨视图像素对齐
- 发布 FaceGS-10K：首个大规模可直接使用的 3D 高斯头像资产数据集

## 适用场景

- 研究生成多视角一致的 3D 高斯头像表示
- 为 AR/VR、远程呈现、数字人应用获取头像生成方法
- 使用 FaceGS-10K 数据集训练或评测 3D 头部模型

## 场景标签

 · 领域:3D 计算机视觉/数字人

## 证据(README 行号)

> L13: MVCHead achieves state-of-the-art for unconditional generation of high fidelity, multi-view consistent 3D Gaussian 
> L23: High-fidelity 3D Gaussian head avatar generation is critical for applications such as AR/VR, telepresence, and digi

## 星数曲线

```mermaid
xychart-beta
    title "humansensinglab/MVCHead 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-29", "2026-10-31"]
    y-axis "stars" 26 --> 29
    line [27, 28, 28]
```

2026-10-18 27 → 2026-10-31 28（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `c76a76dd09ba` · [字段定义](../../DATASET.md)*
