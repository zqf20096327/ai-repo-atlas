# neu-vi/UniCorrn

⭐ 225 · Python · NOASSERTION · 推送 2026-08-28 · [GitHub](https://github.com/neu-vi/UniCorrn) · [官网](https://neu-vi.github.io/UniCorrn/) · 组织维护

**统一 2D/3D 对应关系 Transformer 模型：跨模态特征匹配（CVPR 2026）**

CVPR 2026 论文官方实现：UniCorrn 以单一 Transformer 处理 2D-2D 图像匹配、2D-3D 图像-点云匹配与 3D-3D 点云配准，两阶段训练，基于 CroCoV2 预训练权重与自定义特征融合模块。提供 HuggingFace 上的两阶段预训练权重、conda/pip 安装流程、训练脚本（MegaDepth/ScanNet++/7Scenes/3DMatch 等数据集）及 MegaDepth-1500、InLoc、3DMatch 等基准脚本。含 notebooks 示例，可选安装 CUDA cuRoPE 扩展。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一模型统一 2D-2D / 2D-3D / 3D-3D 三类对应任务
- 两阶段训练，提供预训练权重下载（HuggingFace）
- 覆盖 MegaDepth-1500、ScanNet-1500、InLoc、3DMatch、ModelNet 等基准脚本
- 提供 2D2D/2D3D/3D3D 使用示例 notebook

## 适用场景

- 我在做视觉定位或 SfM，需要跨图像的特征点匹配
- 我有图像与点云需要做 2D-3D 配准
- 我在 3D 重建流程中需要点云到点云的配准模型

## 场景标签

 · 领域:计算机视觉/三维对应

## 证据(README 行号)

> L1: 🦄 UniCorrn: Unified Correspondence Transformer Across 2D and 3D CVPR 2026
> L66: __2D2D__
> L74: __2D3D__ and __3D3D__ examples are included in `notebooks/2d3d.ipynb` and `notebooks/3d3d.ipynb`.

## 星数曲线

```mermaid
xychart-beta
    title "neu-vi/UniCorrn 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 224 --> 226
    line [225, 225]
```

2026-10-18 225 → 2026-10-24 225（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `93a94ea31f36` · [字段定义](../../DATASET.md)*
