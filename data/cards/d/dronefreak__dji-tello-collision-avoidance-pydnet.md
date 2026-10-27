# dronefreak/dji-tello-collision-avoidance-pydnet

⭐ 55 · Python · Apache-2.0 · 推送 2026-08-26 · [GitHub](https://github.com/dronefreak/dji-tello-collision-avoidance-pydnet) · 个人维护

**无人机/摄像头实时单目深度估计避障工具（PyDNet）**

基于 PyDNet 论文（IROS 2018）的单目深度估计应用，TF2.x 重构，可在 DJI Tello 视频流或普通 USB/内置摄像头上实时生成深度图，并基于深度阈值做障碍检测与自主飞行避障。无人机命令默认禁用以保安全，需显式开启；提供单元测试与 Python 包化代码结构。预训练权重需另行下载（链接待定），无权重时代码可运行但输出随机。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- DJI Tello 视频流与普通摄像头两种输入模式
- CPU 优化的 PyDNet 单目深度估计，支持 GPU 加速
- 基于深度阈值的障碍检测与自主避障（默认禁用命令）
- 深度图实时可视化与可配置参数系统

## 适用场景

- 用笔记本摄像头无无人机测试深度估计
- 让 DJI Tello 根据深度图自主避障飞行
- 研究单目深度估计在消费级无人机上的实时部署

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L6: Real-time monocular depth estimation for DJI Tello drone collision avoidance using PyDNet. Based on the paper "Towar
> L14: - 🧠 **PyDNet Depth Estimation**: Fast monocular depth estimation optimized for CPU
> L15: - 🎯 **Collision Avoidance**: Autonomous navigation based on depth maps

## 星数曲线

```mermaid
xychart-beta
    title "dronefreak/dji-tello-collision-avoidance-pydnet 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 54 --> 56
    line [55, 55]
```

2026-10-18 55 → 2026-10-27 55（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `524fa12d81e2` · [字段定义](../../DATASET.md)*
