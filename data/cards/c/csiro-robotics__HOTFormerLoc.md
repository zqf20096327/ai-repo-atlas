# csiro-robotics/HOTFormerLoc

⭐ 32 · Python · NOASSERTION · 推送 2026-08-11 · [GitHub](https://github.com/csiro-robotics/HOTFormerLoc) · [官网](https://openaccess.thecvf.com/content/CVPR2025/papers/Griffiths_HOTFormerLoc_Hierarchical_Octree_Transformer_for_Versatile_Lidar_Place_Recognition_Across_CVPR_2025_paper.pdf) · 组织维护

**CVPR 2025 论文官方代码：激光雷达位置识别的八叉树 Transformer 网络**

CVPR 2025 论文 HOTFormerLoc 的官方 PyTorch 实现：基于层次八叉树的多尺度注意力机制，处理地面与航空视角的大规模 3D 位置识别，覆盖城市与森林环境。配套发布 CS-Wild-Places 跨源数据集（四片森林的地面与航空激光扫描）。README 提供基于 conda/mamba 的环境安装、四个数据集（Wild-Places、CS-Wild-Places、CS-Campus3D、Oxford RobotCar）的训练元组生成流程、训练/评估命令、SLURM 集群提交脚本及各数据集预训练权重下载。改进版 HOTFLoc++ 另行发布，支持重排序与 6-DoF 度量定位。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 八叉树多尺度注意力机制，支持 ground-to-ground 与 ground-to-aerial 场景
- 配套发布 CS-Wild-Places 跨源 3D 数据集（四片森林的航空与地面激光扫描）
- 提供四个数据集的预训练权重与训练/评估代码
- 提供 SLURM 集群训练提交脚本（自动 checkpoint 与超时重提交）

## 适用场景

- 机器人/SLAM 系统中做激光雷达位置识别（回环检测/重定位）
- 在森林或城市环境中做跨视角（地面↔航空）定位
- 在 CS-Wild-Places 等基准上复现或对比位置识别方法

## 场景标签

 · 领域:机器人/激光雷达定位

## 证据(README 行号)

> L14: **HOTFormerLoc: Hierarchical Octree Transformer for Versatile Lidar Place Recognition Across Ground and Aerial View
> L20: We present **HOTFormerLoc**, a novel and versatile **H**ierarchical **O**ctree-based **T**rans**Former** for large-
> L28: Our results demonstrate that HOTFormerLoc achieves a top-1 average recall improvement of 5.5% – 11.5% on the CS-Wil

## 星数曲线

```mermaid
xychart-beta
    title "csiro-robotics/HOTFormerLoc 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-30"]
    y-axis "stars" 30 --> 33
    line [31, 32, 32]
```

2026-10-18 31 → 2026-10-30 32（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `398d93a0b33c` · [字段定义](../../DATASET.md)*
