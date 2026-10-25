# jason-snell/humanized-cursor-trajectory-gen

⭐ 49 · C# · MIT · 推送 2026-05-08 · [GitHub](https://github.com/jason-snell/humanized-cursor-trajectory-gen) · 个人维护

**生成拟人鼠标轨迹的自训练 ONNX 模型库**

作者用自己 2023 年末采集的鼠标运动数据训练的 ONNX 模型，在给定起点与终点坐标间生成拟人化中间轨迹点，用于测试、UI 自动化或研究，README 提及可用于对抗反爬检测。包含两个项目：TrajectoryGeneratorAPI 提供 API 实现（可在作者网站测试，附 curl 示例）；HumanizedTrajectoryGen 为基础 CLI 示例，支持无输入时随机生成坐标。训练数据暂未附上。

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

- 自训练 ONNX 模型生成拟人鼠标轨迹点
- 提供 API 版本（在线演示 + curl 示例）与 CLI 示例两个项目
- 无输入时可随机生成起终点坐标

## 适用场景

- 为 UI 自动化或测试生成拟人鼠标移动轨迹
- 研究人手鼠标运动模式的模拟
- 对抗反爬/反机器人检测的自动化场景

## 场景标签

 · 领域:自动化工具/输入仿真

## 证据(README 行号)

> L3: Human-like cursor movement generator using a self-trained ONNX model. Simulates real mouse trajectories for testing,
> L5: Generates intermediate points between a start X,Y and end X,Y. Useful against anti-bots for automation.
> L7: I trained this late 2023 on a dataset of my own cursor movement. If I come across the data, I will add here.

## 星数曲线

```mermaid
xychart-beta
    title "jason-snell/humanized-cursor-trajectory-gen 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 48 --> 50
    line [49, 49]
```

2026-10-18 49 → 2026-10-25 49（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `c5f3fb348be1` · [字段定义](../../DATASET.md)*
