# DivitMittal/CARLA-Autonomous-Driving

⭐ 31 · Jupyter Notebook · MIT · 推送 2026-10-22 · [GitHub](https://github.com/DivitMittal/CARLA-Autonomous-Driving) · [官网](https://deepwiki.com/DivitMittal/CARLA-Autonomous-Driving) · 个人维护

**CARLA 仿真中的自动驾驶系统：深度语义分割感知**

基于 CARLA 高保真车辆仿真器的自动驾驶研究项目：用 CNN 做实时语义分割，融合 RGBA 相机与 LiDAR 数据实现环境感知，覆盖感知、规划与控制模块；支持相机、LiDAR、雷达、GPS 等传感器集成，并提供模拟数据采集工具、训练脚本与评估框架，及车辆动态与传感器数据的实时可视化。技术栈含 CARLA、OpenCV、Keras、TensorFlow 与 Pygame（手动控制）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CNN 实时语义分割用于环境感知
- RGBA 相机与 LiDAR 数据融合
- 相机/LiDAR/雷达/GPS 多传感器集成
- 含训练脚本、评估框架与实时可视化

## 适用场景

- 在 CARLA 仿真中开发与测试自动驾驶感知算法
- 采集仿真数据训练语义分割模型
- 研究多模态传感器融合的 3D 环境感知

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L8: - **Enhance Perception Systems**: Utilize deep learning techniques for semantic segmentation to improve the vehicle'
> L30: - **Neural Network Architecture**: Utilizes CNNs tailored for real-time semantic segmentation, ensuring efficient a

## 星数曲线

```mermaid
xychart-beta
    title "DivitMittal/CARLA-Autonomous-Driving 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-30 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `0566585ad619` · [字段定义](../../DATASET.md)*
