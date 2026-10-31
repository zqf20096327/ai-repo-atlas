# adityamwagh/SuperSLAM

⭐ 184 · C++ · LGPL-2.1 · 推送 2026-07-10 · [GitHub](https://github.com/adityamwagh/SuperSLAM) · 个人维护

**基于深度学习特征的实时双目/RGB-D 视觉 SLAM 系统**

SuperSLAM 是面向机器人定位建图的双目与 RGB-D 视觉 SLAM 系统：SuperPoint 检测特征、LightGlue 在 TensorRT FP16 后端匹配，配合 GTSAM 优化核心与位姿图回环。提供 KITTI、EuRoC、TUM、TartanAir、TartanGround 数据集上的 ATE/RPE/fps 基准结果。通过 Docker 或裸机（CUDA 12.9、TensorRT 10/11、cuDNN 9）构建运行，代码目标架构为 Ampere/Ada/Blackwell。README 自标为 Alpha 软件；无显式动态物体处理，高速运动场景精度下降。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | LGPL-2.1 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- SuperPoint 特征检测 + LightGlue 匹配，运行于 TensorRT FP16
- GTSAM 优化核心与位姿图回环闭环
- 五个公开数据集的完整基准结果（ATE/RPE/fps）
- Docker 与裸机两种构建路径，支持 TensorRT 10/11

## 适用场景

- 机器人在双目或 RGB-D 相机输入下实时定位与建图
- 在 KITTI/EuRoC/TUM 等公开数据集上复现基准并对比 SLAM 方案
- 需要 GPU 加速的深度学习特征 SLAM 研究与开发

## 场景标签

 · 领域:机器人/计算机视觉

## 证据(README 行号)

> L5: SuperSLAM is a real-time stereo and RGB-D visual SLAM system. SuperPoint detects features and
> L6: LightGlue matches them on a TensorRT FP16 backend, with a GTSAM optimization core and pose-graph

## 星数曲线

```mermaid
xychart-beta
    title "adityamwagh/SuperSLAM 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-31"]
    y-axis "stars" 182 --> 185
    line [183, 184, 184]
```

2026-10-18 183 → 2026-10-31 184（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `5f5434dc4edf` · [字段定义](../../DATASET.md)*
