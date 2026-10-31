# kyo-takano/alphacube

⭐ 23 · Python · MIT · 推送 2026-03-14 · [GitHub](https://github.com/kyo-takano/alphacube) · [官网](https://alphacube.dev) · 个人维护

**DNN 求解魔方的 Python 库：给出任意打乱状态的最优/近优解**

扩展 EfficientCube 的魔方求解库：使用深度神经网络（自监督学习 + 启发式搜索，方法来自 TMLR'23 论文）对给定打乱状态搜索最优/近最优解。提供 small/base/large 三档预训练模型（Half-Turn Metric 下算力最优训练），首次 load 时自动下载并缓存模型数据；CPU 默认 small，GPU/MPS 可用 large 加速。支持调节 beam_width 权衡解质量与速度，并可设置 ergonomic_bias 使解法偏向更易执行的转法。以 pip 包形式提供。

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

- DNN 启发式搜索生成最优/近最优魔方解法
- small/base/large 三档预训练模型，首次运行自动下载缓存
- beam_width 参数调节搜索深度，权衡解长与耗时
- ergonomic_bias 偏好特定转法，生成更易执行的解序列

## 适用场景

- 求解任意打乱状态的魔方
- 寻找优化的魔方算法（按步数或人体工学）
- 在自己的魔方应用中嵌入求解能力
- 演示自监督学习与启发式搜索等 AI/ML 概念

## 场景标签

 · 领域:求解器/组合优化

## 证据(README 行号)

> L3: AlphaCube is a powerful & flexible Rubik's Cube solver that extends EfficientCube. It uses a Deep Neural Network (DN
> L131: At its core, AlphaCube uses the deep learning method from "Self-Supervision is All You Need for Solving Rubik's Cu

## 星数曲线

```mermaid
xychart-beta
    title "kyo-takano/alphacube 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-31 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `69273a02fc45` · [字段定义](../../DATASET.md)*
