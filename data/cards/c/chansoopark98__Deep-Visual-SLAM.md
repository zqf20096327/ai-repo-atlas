# chansoopark98/Deep-Visual-SLAM

⭐ 16 · Python · MIT · 推送 2026-11-22 · [GitHub](https://github.com/chansoopark98/Deep-Visual-SLAM) · 个人维护

**为机器人与 AR 研究者提供单目度量尺度视觉里程计/SLAM 的 PyTorch 实现**

基于 PyTorch 的单目视觉里程计系统（视觉 SLAM 前端，无回环检测）：用自监督单目深度网络提供尺度先验，以 RAFT 光流跟踪、PnP 与滑窗光束法平差估计位姿，再经 GPU 光度细化精修，支持 LoRA 测试时自适应新序列。在 TUM-VI 室内基准评测，官方集平移步进误差 2.48%。需 Linux、Python 3.10+ 与 NVIDIA GPU（单测可跑 CPU），运行时约 137 ms/帧（RTX 5090），非实时。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单 RGB 相机推理即可恢复度量尺度，无需尺度对齐
- RAFT-large 稠密光流 + 滑窗 BA + GPU 光度细化的完整管线
- 可选 LoRA 测试时自适应，将深度网络适配到新序列
- 发布深度权重、单命令 demo 与单元测试套件

## 适用场景

- 在 TUM-VI/EuRoC 等数据集上复现与评测视觉里程计结果
- 机器人或 AR 场景中从单目序列恢复度量轨迹与三维地图
- 基于自监督深度先验研究 SLAM 管线的组件替换与改进

## 场景标签

 · 领域:计算机视觉/机器人

## 证据(README 行号)

> L14: `dvslam` is a **monocular visual odometry** (visual SLAM front end, no loop closure) system that recovers **metric
> L18: sequence. It is written in PyTorch and evaluated on the TUM-VI indoor benchmark, for robotics and AR use cases.

## 星数曲线

```mermaid
xychart-beta
    title "chansoopark98/Deep-Visual-SLAM 星数(近 2 点)"
    x-axis ["2026-11-23", "2026-11-26"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-11-23 16 → 2026-11-26 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `2855b6aef4e2` · [字段定义](../../DATASET.md)*
