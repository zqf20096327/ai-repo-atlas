# Gokuld102/ai-traffic-signal-optimization

⭐ 55 · Python · 推送 2026-05-28 · [GitHub](https://github.com/Gokuld102/ai-traffic-signal-optimization) · 个人维护

**AI 自适应交通信号优化原型：YOLO 检测车辆并动态调节信号**

面向智能交通研究与教学的原型系统：Flask 后端读取交通视频，用 YOLOv8+OpenCV 实时检测计数车辆，按车流密度自适应调整四路交叉口信号配时，检测救护车/警车/消防车以生成虚拟绿波走廊，并用基于合成数据训练的 RandomForest 模型预测拥堵等级；含 Web 仪表盘展示实时计数、信号状态与图表，可选 MongoDB 存储记录。README 声明仅为演示用途，使用单一样例视频，车道检测为基于区域的近似。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- YOLOv8+OpenCV 实时车辆检测与计数
- 按车流密度自适应调整信号配时
- 应急车辆优先通行（虚拟绿色走廊）
- RandomForest 拥堵预测与 Flask Web 仪表盘

## 适用场景

- 我想演示 AI 自适应交通信号控制的原理
- 在四路交叉口仿真中观察应急车辆优先通行
- 作为计算机视觉+机器学习的教学/课程项目

## 场景标签

`目标检测` `教程课程` · 领域:学习与行业

## 证据(README 行号)

> L15: * **Vehicle Detection (YOLOv8 + OpenCV)**
> L24: * **ML-Based Traffic Prediction**

## 星数曲线

```mermaid
xychart-beta
    title "Gokuld102/ai-traffic-signal-optimization 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 54 --> 56
    line [55, 55]
```

2026-10-18 55 → 2026-10-26 55（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `52e5e7fb90cf` · [字段定义](../../DATASET.md)*
