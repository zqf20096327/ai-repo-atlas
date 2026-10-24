# vbszbdrup/Pose-Angle-Coach

⭐ 56 · HTML · 推送 2026-10-23 · [GitHub](https://github.com/vbszbdrup/Pose-Angle-Coach) · 个人维护

**基于 OpenCV 姿态估计的实时动作姿态分析与反馈工具**

FormForge 是一个 Python + OpenCV 的实时姿态分析引擎：在普通 CPU 上对人体骨架做姿态估计，提取关节关键点并计算关节角度，结合规则引擎与目标角度区间生成实时教练式文本反馈，叠加渲染到视频画面上。支持左右对称评分、节奏追踪、姿态漂移检测与会话总结，视频全程本地处理不上传。面向健身居家练习、康复角度数据记录、教练辅助与人体工学研究等场景，声明非医疗设备。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CPU 运行的骨架姿态估计与关键点提取
- 关节角度计算、对称评分、姿态漂移检测
- 可配置规则引擎定义动作与角度目标区间
- 多语言教练反馈外置化，视频本地处理不上传

## 适用场景

- 居家独自训练时获得实时的动作姿态反馈
- 康复训练中记录关节角度数据以跟踪进展
- 教练带团体课时作为第二双眼睛观察学员动作
- 人体工学研究中采集姿态数据

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L10: This repository is the beating heart of that idea: a Python + OpenCV engine that performs skeletal pose estimation 
> L61: 2. **Pose Estimation** — a pose model identifies human keypoints and their confidence values.

## 星数曲线

```mermaid
xychart-beta
    title "vbszbdrup/Pose-Angle-Coach 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 55 --> 57
    line [56, 56]
```

2026-10-18 56 → 2026-10-24 56（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `844f50f6f1d8` · [字段定义](../../DATASET.md)*
