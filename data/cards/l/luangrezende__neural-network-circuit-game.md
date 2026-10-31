# luangrezende/neural-network-circuit-game

⭐ 20 · Python · 推送 2026-03-04 · [GitHub](https://github.com/luangrezende/neural-network-circuit-game) · [官网](https://github.com/luangrezende/neural-network-circuit-game/releases) · 个人维护

**神经进化模拟：AI 车辆用遗传算法学习驾驶自定义赛道**

面向开发者的神经进化仿真项目：种群中每辆车由小型前馈神经网络（8 输入-14 隐藏-2 输出）控制，权重经选择、交叉与变异逐代进化，不使用反向传播。仿真核心与 Matplotlib 可视化分层，支持无头训练，附交互式赛道编辑器可导出 pista.json。提供 Windows 预编译可执行文件，也可用 Python 3.11+ 从源码运行；PyTorch 为可选依赖，不需要 CUDA GPU。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 遗传算法进化网络权重，无反向传播/梯度下降
- 仿真核心与渲染层分离，可无头训练
- 交互式赛道编辑器，点击布点并导出 JSON
- 超参数（种群、奖励、惩罚）集中在 config.json

## 适用场景

- 观察遗传算法逐代训练车辆驾驶行为
- 设计和导出自定义赛道测试进化效果
- 作为神经进化教学/实验的代码基础

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L2: Neuroevolution simulation where a population of AI-controlled cars learns to drive a custom circuit through a geneti
> L13: Each generation, a population of cars drives the circuit simultaneously. Cars are controlled by a small feedforward

## 星数曲线

```mermaid
xychart-beta
    title "luangrezende/neural-network-circuit-game 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-31 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `18645372cbb7` · [字段定义](../../DATASET.md)*
