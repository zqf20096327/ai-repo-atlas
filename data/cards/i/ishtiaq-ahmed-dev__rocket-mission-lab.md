# ishtiaq-ahmed-dev/rocket-mission-lab

⭐ 3 · HTML · MIT · 推送 2026-11-26 · [GitHub](https://github.com/ishtiaq-ahmed-dev/rocket-mission-lab) · 个人维护

**神经网络全程驾驶的猎鹰9级发射回收浏览器仿真实验**

一个浏览器内的 Three.js 仿真实验室：两个神经网络（MLP，10 Hz 评估）从起飞到 LZ-1 着陆及入轨全程输出飞行指令，页面内含 RK4 物理积分与 base64 权重，无脚本导引与后备控制器。训练采用模仿学习的 DAgger 流程，教师为不随产品发布的预测控制器，在 Node 中跑飞行并用 PyTorch 拟合；提供硬例挖掘、held-out 评估与多种回归检查脚本。README 明确声明这是仿真研究，非飞行软件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 两个 MLP 网络在页面内 10 Hz 输出全部飞行指令，无脚本导引与后备控制器
- DAgger 模仿学习训练流程：演示、克隆、微调、选择门与 held-out 测试
- 权重以 base64 float32 打包进页面，含 1,300 留出任务与引擎故障恢复评估记录
- 提供 check_flight/check_standards 等脚本验证事件顺序与物理标准锚点

## 适用场景

- 在浏览器中观看并回放神经网络全程驾驶的发射与回收任务
- 复现 DAgger 模仿学习训练与评估流水线
- 作为火箭着陆控制与仿真教学的研究案例

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L5: **A Falcon 9-class launch and return-to-launch-site landing, flown end to end by a neural network.**
> L18: Two neural networks fly the whole mission at 10 Hz from the vehicle's own state: the booster from liftoff to touchd
> L76: The networks imitate a classical **teacher** that is never shipped: a predictive controller that simulates the rest

## 星数曲线

```mermaid
xychart-beta
    title "ishtiaq-ahmed-dev/rocket-mission-lab 星数(近 2 点)"
    x-axis ["2026-11-21", "2026-11-27"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-21 3 → 2026-11-27 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 mid · 依据 README sha `05d23c206240` · [字段定义](../../DATASET.md)*
