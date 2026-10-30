# snenyl/realtime-pose-estimation

⭐ 30 · C++ · Apache-2.0 · 推送 2026-02-26 · [GitHub](https://github.com/snenyl/realtime-pose-estimation) · 个人维护

**基于 YOLOX 与 RealSense 点云的实时托盘位姿估计系统**

硕士论文配套项目：用 Intel RealSense L515 RGB-D 传感器采集 RGB 图像与点云，YOLOX-S（在 LOCO 数据集上迁移学习）检测托盘，过滤点云后经两次 RANSAC 平面拟合与向量运算输出托盘的 3D 位置与朝向；最终版本以 Intel OpenVINO 优化并用 C++ 实现。评估采用 AprilTag 做移动与静止两项测试。Pallet void 检测模型置信度低于 1%，README 在 Future Work 中列出多项待改进项，属研究原型。

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

## 能力要点

- YOLOX-S + LOCO 数据集迁移学习的托盘检测（AP50 53.2%，推理 6.74 ms）
- 两次 RANSAC 平面拟合结合相机中心向量估计托盘位姿
- Intel OpenVINO 优化并以 C++ 实现，PCL 3D 查看器输出结果
- AprilTag（25h9）移动/静止两项评估测试

## 适用场景

- 工业场景中用 RGB-D 相机实时获取托盘位姿
- 机器人抓取/叉车对接前的托盘定位参考实现
- 复现或扩展基于点云的位姿估计研究实验

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L6: By combining an RGB image and point cloud data is, the system capable of detecting the object's pose by using object
> L19: The object detection algorithm is the YOLOX-S model from the YOLOX
> L57: The pose estimation is performed using the object detection algorithm and point cloud data.

## 星数曲线

```mermaid
xychart-beta
    title "snenyl/realtime-pose-estimation 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-30 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `fead2a8204e9` · [字段定义](../../DATASET.md)*
