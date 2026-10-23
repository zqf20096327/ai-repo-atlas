# AlexAsplund/Vanchor

⭐ 123 · Python · MIT · 推送 2026-08-25 · [GitHub](https://github.com/AlexAsplund/Vanchor) · [官网](https://vanchor.org) · 个人维护

**把低价拖曳电机改造成 GPS 自动驾驶仪的船用导航系统**

运行在 Raspberry Pi 等单板机上的船用 GPS 自动驾驶与虚拟锚定系统：手机 PWA 控制，支持定点锚泊、航向保持、避岛水路规划、巡线/测绘、钓鱼模式与安全包（电池监测、地理围栏、失联保持）。控制律默认为手调 PID；可选 Smart 模式用约 1.6k 参数的 tanh MLP（进化策略离线训练、numpy 推理、无需 ML 运行时/GPU）对 PID 输出做修正，带回退保护。内置物理仿真器，可在无硬件的笔记本上运行与测试。面向钓鱼/船艇用户与 DIY 硬件搭建者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 内置物理仿真器与模拟 NMEA 传感器，无硬件即可全栈开发测试
- Smart 模式：~1.6k 参数 MLP 修正 PID，numpy 微秒级推理，运行时守护回退
- 避岛水路规划（能见度图 + A*）与航线点导航、风/流漂移补偿
- 配套开源 PCB（vanchor-pcb）与 3D 打印转向舵机设计

## 适用场景

- 钓鱼时用手机在地图上落虚拟锚定点守钓
- 规划绕岛水路自动驶向目标点并巡线测绘
- 无硬件情况下用仿真器先行学习与测试整套系统

## 场景标签

 · 领域:船舶导航/机器人控制

## 证据(README 行号)

> L49: - **Smart (opt-in)** — a tiny neural net that *refines* the PID rather than
> L53:  run on the Raspberry Pi as a few microsecond numpy matrix multiplies —
> L55:  (gradient-free, numpy-only) against the exact Fossen 3-DOF physics across

## 星数曲线

```mermaid
xychart-beta
    title "AlexAsplund/Vanchor 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 122 --> 124
    line [123, 123]
```

2026-10-18 123 → 2026-10-23 123（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `15968a9f8166` · [字段定义](../../DATASET.md)*
