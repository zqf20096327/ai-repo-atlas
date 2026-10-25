# aviralchharia/MV-SSM

⭐ 17 · Apache-2.0 · 推送 2025-11-15 · [GitHub](https://github.com/aviralchharia/MV-SSM) · [官网](https://aviralchharia.github.io/MV-SSM/) · 组织维护

**CVPR 2025 论文项目页：多视角状态空间模型做 3D 人体姿态估计**

CMU 与 NUS 研究团队的 CVPR 2025 论文仓库，提出 MV-SSM 框架用于多视角 3D 人体关键点估计：在多视角图像特征层与人体关键点层显式建模联合空间序列，提出 Projective State Space（PSS）块与 Grid Token-guided Bidirectional Scanning（GTBS）扫描方式。摘要报告在 CMU Panotic 三相机设定与跨数据集评估上的量化指标。截至 Dec. 15, 2025 更新说明，代码与模型权重标注 Coming Soon，尚未发布；README 无安装运行说明。部分代码改编自 Mamba、VMamba、MVGFormer、MvP、VoxelPose，许可为 CC BY-NC 4.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 安装:github 包 `release-assets` 月下载无数据

## 能力要点

- 多视角 3D 人体关键点估计的状态空间建模框架
- PSS 块学习相机配置泛化的联合空间排列表示
- GTBS 修改 Mamba 传统扫描为网格 token 引导的双向扫描
- 代码改编自 Mamba、VMamba、MVGFormer、MvP、VoxelPose

## 适用场景

- 研究人员复现或跟进多视角 3D 人体姿态估计方法
- 了解状态空间模型在多视角感知任务中的用法
- 作为论文引用与后续代码发布的关注入口

## 场景标签

 · 领域:计算机视觉/人体感知

## 证据(README 行号)

> L26: While significant progress has been made in single-view 3D human pose estimation, multi-view 3D human pose estimati

## 星数曲线

```mermaid
xychart-beta
    title "aviralchharia/MV-SSM 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-25 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `eb4e395adce9` · [字段定义](../../DATASET.md)*
