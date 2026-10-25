# rakesh-i/ESP32-Autonomous-car

⭐ 78 · Python · MIT · 推送 2026-09-13 · [GitHub](https://github.com/rakesh-i/ESP32-Autonomous-car) · 个人维护

**ESP32 遥控车改造的自动驾驶小车项目：训练并部署转向模型**

面向学习者的低成本自动驾驶小车项目：用常见零件组装 RC 小车，通过 ESP32-CAM 采集赛道图像，人工驾驶采集训练数据（stream.py），经 balance.py 平衡后用 train_model.py 基于 AlexNet 训练转向预测模型，运行 run.py 时模型预测方向并经 TCP 无线控制小车转向；另含巡线训练模式与 PID 转向修正。开发语言为 MicroPython、Python 与 Arduino，安装方式为 git clone 源码并用 rshell 将脚本刷入 ESP32。需要自行具备焊接、ESP32 编程等基础技能。

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

- 人工驾驶采集图像数据，AlexNet 训练转向预测模型
- 无线 TCP 连接：PC 端运行推理，控制 ESP32 小车
- 巡线训练模式与 PID 转向修正
- 使用廉价常见零件搭建硬件

## 适用场景

- 动手构建并训练自己的自动驾驶小车
- 学习图像数据采集、数据平衡与模型训练部署流程
- 低成本实践机器人在真实赛道上的自主行驶

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L32: There are many autonomous car projects on GitHub, however, many of those require costly hardware or it is just a si
> L46: * Arduino
> L108: 8. Now time to train our AI model. You can change prameters which suits your requirements. But I recommend to leav

## 星数曲线

```mermaid
xychart-beta
    title "rakesh-i/ESP32-Autonomous-car 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 77 --> 79
    line [78, 78]
```

2026-10-18 78 → 2026-10-25 78（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `59def95b1f64` · [字段定义](../../DATASET.md)*
