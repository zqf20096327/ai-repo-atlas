# Ayush-Deore/Autonomous-Car-Simulation

⭐ 47 · JavaScript · 推送 2026-07-05 · [GitHub](https://github.com/Ayush-Deore/Autonomous-Car-Simulation) · [官网](https://autonomous-car-simulation.vercel.app) · 个人维护

**浏览器中用神经网络实现自动驾驶小车模拟**

纯前端的浏览器模拟项目：多辆虚拟车依靠自建前馈神经网络，根据射线传感器的距离输入输出转向决策，避开车道边界与交通车辆；通过逐代变异权重与保留最佳模型实现学习，支持 localStorage 保存模型，并可用方向键手动控制测试车。页面同时可视化网络结构。README 未给出安装命令，需自行从源码运行 index.html。

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

- 自建前馈神经网络（5 输入→6 隐藏→4 输出）驱动车辆转向
- 基于射线投射的传感器模拟与几何碰撞检测
- 逐代变异与最佳模型保存（localStorage）
- Canvas 可视化神经网络与模拟画面

## 适用场景

- 在浏览器中观察神经网络通过变异学会避障驾驶
- 学习 Canvas API、射线投射、OOP 等 JavaScript 概念
- 手动驾驶对照测试 AI 车辆表现

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L5: This is a browser-based simulation where virtual cars attempt to drive autonomously on a road. The key idea is to tr
> L61: Custom-built feedforward neural network with adjustable weights and biases

## 星数曲线

```mermaid
xychart-beta
    title "Ayush-Deore/Autonomous-Car-Simulation 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 46 --> 48
    line [47, 47]
```

2026-10-18 47 → 2026-10-25 47（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `00498ff4e778` · [字段定义](../../DATASET.md)*
