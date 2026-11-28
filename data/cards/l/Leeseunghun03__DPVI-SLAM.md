# Leeseunghun03/DPVI-SLAM

⭐ 4 · C++ · GPL-3.0 · 推送 2026-11-24 · [GitHub](https://github.com/Leeseunghun03/DPVI-SLAM) · 个人维护

**基于深度 patch 跟踪与回环检测的单目视觉惯性 SLAM**

DPV-SLAM 的修改版，采用 DEIO 的 IMU 后端估计米制尺度轨迹：以深度 patch 跟踪为核心，序列末端执行回环检测。安装需 conda 环境、从源码编译修改版 GTSAM 及其 Python 封装，并下载 DPVO 权重；可选启用经典回环（依赖 OpenCV C++ 与 DBoW2 编译）和 Pangolin 可视化查看器。提供 EuRoC 评估脚本与其他数据集的 YAML 配置方式（外参、噪声密度、重力等参数）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 深度 patch 跟踪 + DEIO IMU 后端的米制尺度轨迹估计
- 序列末端回环检测，支持经典回环可选组件（DBoW2/ORB 词表）
- 提供 EuRoC 评估脚本与自定义数据集配置模板
- 可通过 --viz 启动 Pangolin 可视化查看器

## 适用场景

- 在 EuRoC 等数据集上评估视觉惯性 SLAM 轨迹精度
- 接入自定义单目相机 + IMU 数据集做米制尺度里程估计
- 需要回环检测的深度学习 SLAM 研究实验

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3: > Monocular visual-inertial SLAM with deep patch tracking and loop closure
> L5: A modified version of DPV-SLAM that uses the IMU backend of DEIO to estimate metric-scale trajectories.
> L67: python evaluate_euroc.py --eurocdir <eurocdir> --scenes MH_01_easy --plot --save_trajectory


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `a2e8a4ff22b3` · [字段定义](../../DATASET.md)*
