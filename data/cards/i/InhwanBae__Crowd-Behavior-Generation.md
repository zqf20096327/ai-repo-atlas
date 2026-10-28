# InhwanBae/Crowd-Behavior-Generation

⭐ 55 · Python · MIT · 推送 2026-07-21 · [GitHub](https://github.com/InhwanBae/Crowd-Behavior-Generation) · [官网](https://ihbae.com/publication/crowdes/) · 组织维护

**CVPR 2025 论文代码：从单张场景图生成持续人群轨迹**

Continuous Locomotive Crowd Behavior Generation（CVPR 2025）官方实现，含 CrowdES 框架：基于扩散的 Crowd Emitter 决定新个体出现的时空位置，状态切换的 Crowd Simulator 生成个体持续进出场景的轨迹。仅需单张输入图像即可填充人群，支持运行时覆盖场景级与个体级参数，并提供 ETH/UCY/SDD/EDIN 数据集复用基准与两级评估。基于 PyTorch 2.2.2/CUDA 12.1 训练与测试，提供预训练模型、轨迹导出、自定义图像推理及基于 CARLA 的 3D 可视化工具包。面向科研用户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 扩散式 Crowd Emitter + 状态切换 Crowd Simulator 生成持续人群轨迹
- 仅需单张输入图像即可填充场景人群，无需观测轨迹
- 复用 ETH/UCY/SDD/EDIN 真实轨迹数据集的生成基准与两级评估
- 提供基于 CARLA 的 3D 可视化工具包与预训练模型

## 适用场景

- 在场景图像上生成持续变化的人群轨迹用于仿真
- 用预训练模型导出或评估人群轨迹生成结果
- 做 Sim2Real/Real2Sim 相关的人群行为研究

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L22:  **Summary**: A **crowd emitter diffusion model** and a **state-switching crowd simulator** for **populating** inpu
> L33: * **Crowd Emitter**: A diffusion-based model that iteratively “emits” new agents by sampling when and where they ap

## 星数曲线

```mermaid
xychart-beta
    title "InhwanBae/Crowd-Behavior-Generation 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 54 --> 56
    line [55, 55]
```

2026-10-18 55 → 2026-10-28 55（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `ad8b9b3164b9` · [字段定义](../../DATASET.md)*
