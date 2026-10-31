# ai-and-lab/rebase

⭐ 15 · 推送 2026-10-13 · [GitHub](https://github.com/ai-and-lab/rebase) · 组织维护

**免训练上下文图像分割方法（ACCV 2026 Oral）的官方仓库**

REBASE 提出基于参考背景子空间消除的免训练上下文分割方法：仅需一张参考图像及其二值掩码，即可在任意查询图像中分割同类目标，无需梯度更新或针对目标的适配。README 给出在 ISIC、X-Ray、FSS-1000、PASCAL-Part、PACAL-Part 五个基准上的 1-shot mIoU 结果，与 PerSAM、Matcher、GF-SAM、INSID3 等免训练方法并列。方法构建于 SAM 与 DINOv2 之上。代码尚未发布，README 标注 'Code release coming soon'，目前主要提供论文引用信息。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单张参考图+掩码即可对查询图像做同类分割，免训练
- 五个基准上的 1-shot mIoU 结果表
- 构建于 SAM 与 DINOv2 之上

## 适用场景

- 查阅免训练上下文分割方法与基准结果
- 与 PerSAM/Matcher/GF-SAM 等方法做结果对比
- 关注该方法的后续代码发布进展

## 场景标签

`图像视频处理` `目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L12: Training-free in-context segmentation. A single reference image and its binary mask are sufficient to segment the s
> L45: This project builds upon Segment Anything (SAM) and DINOv2. We also thank the authors of PerSAM, Matcher, GF-SAM, a

## 星数曲线

```mermaid
xychart-beta
    title "ai-and-lab/rebase 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-31 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `ca44ed9236dd` · [字段定义](../../DATASET.md)*
