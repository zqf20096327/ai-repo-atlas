# ansh1113/terrain-aware-locomotion

⭐ 14 · Python · MIT · 推送 2026-04-09 · [GitHub](https://github.com/ansh1113/terrain-aware-locomotion) · 个人维护

**四足机器人地形感知运动管线：感知分类与自适应足步规划**

面向四足机器人（ANYmal C / Unitree A1）的运动管线：RGB-D 相机与 IMU 数据经 elevation_mapping_cupy 生成高程图，微调 SegFormer 模型将地形分为平地/坡地/碎石/楼梯四类，再由改造的 MoveIt2 规划器生成地形自适应足步序列与步态参数，以 10Hz 感知-规划循环运行。README 报告 95% 导航成功率、跌倒减少 50%。提供 setup 脚本与 ROS2 启动命令，含 Gazebo 仿真演示与 colcon 测试。

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

- 深度相机+IMU 高程建图，SegFormer 四类地形分类（>95% 合成数据准确率）
- MoveIt2 足步规划与按地形类别的步态自适应
- 分类置信度 <80% 时规划器自适应的不确定性处理
- 10Hz 实时感知-规划循环，Gazebo 仿真环境

## 适用场景

- 让四足机器人在楼梯、坡地、碎石等非结构化地形自主行走
- 在仿真中验证地形感知与足步规划方案
- 为巡检、救援等场景的机器人运动开发提供管线参考

## 场景标签

 · 领域:机器人/自主导航

## 证据(README 行号)

> L27: RGB/Depth Camera → Elevation Mapping → CNN Classifier → Footstep Planner → Robot Control
> L94: - Fine-tuned SegFormer model on synthetic terrain dataset

## 星数曲线

```mermaid
xychart-beta
    title "ansh1113/terrain-aware-locomotion 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `6a0ef45008ab` · [字段定义](../../DATASET.md)*
