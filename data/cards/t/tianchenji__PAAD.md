# tianchenji/PAAD

⭐ 20 · Python · MIT · 推送 2026-11-24 · [GitHub](https://github.com/tianchenji/PAAD) · 组织维护

**机器人导航前瞻性异常检测网络的多传感器融合实现**

RA-L 2022 论文 PAAD 的 PyTorch 实现仓库：融合相机图像、LiDAR 扫描与规划路径，预测机器人导航在未来时间步的失败概率，支持传感器遮挡场景下的鲁棒异常检测。代码含网络结构定义、训练/测试脚本、CSV+图像数据集加载、数据点可视化及一个实时检测的 ROS 节点；提供离线数据集（训练 29292 条）与 6 个 rosbag。在 Ubuntu 20.04、Python 3.8、PyTorch 1.8.1 下测试。

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

- 融合相机、LiDAR 与规划路径预测导航失败概率
- 提供含 29292 条训练数据的离线数据集与 6 个 rosbag
- 提供实时检测的 ROS 节点与自定义消息包
- 数据点可视化脚本将规划轨迹投影到前视图像

## 适用场景

- 复现论文中的机器人导航异常检测实验
- 在野外机器人上通过 ROS 节点实时检测导航失败风险
- 基于多传感器融合数据训练故障预测模型

## 场景标签

 · 领域:机器人/科研

## 证据(README 行号)

> L10: **PAAD fuses camera, LiDAR, and planned path to predict the probability of future failure for robot navigation.** T
> L15: Despite the rapid advancement of navigation algorithms, mobile robots often produce anomalous behaviors that can le
> L29: * `rosnode`: Contains a rosnode which performs proactive anomaly detection in real-time using PAAD.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `058b1224914c` · [字段定义](../../DATASET.md)*
