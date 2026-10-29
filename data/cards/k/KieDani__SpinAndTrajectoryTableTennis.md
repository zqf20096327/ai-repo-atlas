# KieDani/SpinAndTrajectoryTableTennis

⭐ 30 · Python · GPL-3.0 · 推送 2026-07-15 · [GitHub](https://github.com/KieDani/SpinAndTrajectoryTableTennis) · [官网](https://kiedani.github.io/CVPRW2025/) · 组织维护

**CVPR 2025 论文官方代码：从乒乓球转播视频估计球旋转与轨迹**

论文 "Towards Ball Spin and Trajectory Analysis in Table Tennis Broadcast Videos via Physically Grounded Synthetic-to-Real Transfer" 的官方实现（CVSports@CVPR 2025 最佳论文）。提供数据与已训练模型下载，用 pip 安装依赖后可进行训练、评估与推理；另含基于 MuJoCo 的合成数据仿真模块（论文中仿真 5 万条轨迹）。README 提示后续 WACV 2026 论文代码可应用于实际场景。仿真步骤需 xvfb-run 虚拟显示并建议多 CPU 核心。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从转播视频进行乒乓球 3D 轨迹与旋转估计
- 提供数据与已训练模型下载，支持训练/评估/推理脚本
- MuJoCo 合成数据仿真（论文中生成 50000 条轨迹）
- 物理约束的合成到真实迁移方法

## 适用场景

- 复现论文中的旋转与轨迹估计实验
- 生成乒乓球飞行仿真数据用于训练
- 在自采转播视频上推理球旋转与轨迹

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L1: # Towards Ball Spin and Trajectory Analysis in Table Tennis Broadcast Videos via Physically Grounded Synthetic-to-Re
> L3: This repository is the official implementation of the paper Towards Ball Spin and Trajectory Analysis in Table Tenni

## 星数曲线

```mermaid
xychart-beta
    title "KieDani/SpinAndTrajectoryTableTennis 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-29"]
    y-axis "stars" 28 --> 31
    line [29, 30, 30]
```

2026-10-18 29 → 2026-10-29 30（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `17f73b4ea476` · [字段定义](../../DATASET.md)*
