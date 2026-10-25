# sparks-baird/self-driving-lab-demo

⭐ 89 · Jupyter Notebook · MIT · 推送 2026-07-29 · [GitHub](https://github.com/sparks-baird/self-driving-lab-demo) · [官网](https://self-driving-lab-demo.readthedocs.io/) · 组织维护

**低成本自主实验（自驱动实验室）教学演示软硬件套件**

sparks-baird 团队维护的自驱动实验室演示项目，覆盖三个教学与原型演示：光学（RGB LED 混光，<100 美元）、液体（染料配色，<300 美元）、固态（彩色蜡粉配色，需机械臂）。核心机制为向硬件发送调参指令、接收测量结果、经主动学习/贝叶斯优化闭环决策，并利用云端模拟；软件以 Python 包提供，支持 pip 安装与免费公共测试 demo，可在 Colab 中对比网格搜索、随机搜索与贝叶斯优化。

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

- 三个演示：光学混光、液体染料配色、固态蜡粉配色（含机器人搬运）
- 硬件调参→测量→主动学习决策的闭环自主实验流程
- 提供免费公共测试 demo，无需自建硬件即可运行优化对比
- 支持 pip 安装、conda 环境与 Colab notebook

## 适用场景

- 低成本学习自驱动实验室的闭环优化原理
- 高校课程中搭建实验自适应设计教学套件
- 在 Colab 上对比网格/随机/贝叶斯优化算法效果
- 原型验证自主实验流程后再扩展到材料发现场景

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L12: > Software and instructions for setting up and running an autonomous (self-driving) laboratory optics demo using di
> L28: - decision-making via active learning
> L76: I recommend going through the introductory Colab notebook, but here is a shorter version of how an optimization com

## 星数曲线

```mermaid
xychart-beta
    title "sparks-baird/self-driving-lab-demo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 88 --> 90
    line [89, 89]
```

2026-10-18 89 → 2026-10-25 89（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `813840685372` · [字段定义](../../DATASET.md)*
