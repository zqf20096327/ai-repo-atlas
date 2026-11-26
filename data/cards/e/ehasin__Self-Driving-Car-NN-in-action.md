# ehasin/Self-Driving-Car-NN-in-action

⭐ 4 · JavaScript · MIT · 推送 2026-11-02 · [GitHub](https://github.com/ehasin/Self-Driving-Car-NN-in-action) · [官网](https://hasin.eu/projects/nn-self-driving-car-in-action/) · 个人维护

**浏览器里可视化训练小神经网络开车的交互教学项目**

以静态网页形式实现的教学演示：一条双车道道路上的蓝车避让停放车辆，屏幕实时展示两输入雷达→三隐层神经元→Move! 输出的网络权重与偏置。提供三种训练路径：Flashcards（监督学习、反向传播）、Copycat（模仿学习/行为克隆）、Trial & Error（Deep Q-learning 含 replay memory），均从随机初始化网络开始，并在同一条 500 m 未见测试路上验证。无构建步骤、无依赖，纯 JavaScript 实现，核心模块也可在 Node 中运行。作者自述为教孩子及好奇者了解机器如何学习而建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三种学习方式对比训练：监督/模仿/强化学习（Deep Q-learning）
- 屏幕实时展示每个权重、偏置及当前连接贡献（Impact 可视化）
- 引导式 tour：从撞车到训练再到 500 m 未见测试路
- 纯 JavaScript，无构建步骤、无依赖，支持桌面与手机

## 适用场景

- 直观理解反向传播与误差如何向后传播
- 对比监督、模仿、强化三种学习范式的效果差异
- 向初学者或孩子演示机器学习的基本原理
- 本地运行静态文件即可复现同一训练实验

## 场景标签

`强化学习` `教程课程` · 领域:学习与行业

## 证据(README 行号)

> L12: Built for teaching my kids and anyone curious about how machines learn.
> L14: Explore various learning methods (flashcards, copycat, trial & error), observe how individual neurons impact a deci
> L31: Each method starts from an untrained network and ends with the same test road. Below the demo, an explainer covers 

## 星数曲线

```mermaid
xychart-beta
    title "ehasin/Self-Driving-Car-NN-in-action 星数(近 2 点)"
    x-axis ["2026-11-10", "2026-11-26"]
    y-axis "stars" 3 --> 5
    line [4, 4]
```

2026-11-10 4 → 2026-11-26 4（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 mid · 依据 README sha `2698ff94a017` · [字段定义](../../DATASET.md)*
