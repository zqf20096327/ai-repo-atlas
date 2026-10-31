# BianchiGiacomo/deepLearningVolatility

⭐ 15 · Python · MIT · 推送 2026-07-07 · [GitHub](https://github.com/BianchiGiacomo/deepLearningVolatility) · 个人维护

**用神经网络逼近与校准波动率曲面的量化定价框架**

面向量化金融研究的 Python 框架，用神经网络逼近期权波动率曲面，覆盖粗 Bergomi/Heston、Lifted Heston、跳跃扩散等过程的 Monte Carlo 数据生成、网格/逐点/多期限三种神经定价器、曲面插值与 smile 修复等后处理。依赖 Python>=3.8.1 与 PyTorch，提供 Colab 免安装交互演示与训练笔记本、examples 脚本与 docs 文档。README 标注为进行中的研究项目，API 可能变动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 网格/逐点（random grid）/多期限三类神经定价器
- 支持粗 Bergomi、粗 Heston、Lifted Heston、Kou/Merton 跳跃扩散等过程
- Monte Carlo 数据生成含粗模型吸收处理
- 提供交互式 Colab 演示与训练笔记本，浏览器内免安装运行

## 适用场景

- 用神经网络替代 Monte Carlo 快速生成波动率曲面
- 研究粗波动率模型的定价与校准
- 复现与调试时间离散化、长期吸收等数值问题

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L4: Framework for **volatility surface approximation** with neural networks.
> L6: It includes dataset generators (*random grid*), neural pricers (grid, pointwise, multi‑regime),
> L17: - **Data generation**: Monte Carlo with **absorption** handling for rough models (long‑term regime)

## 星数曲线

```mermaid
xychart-beta
    title "BianchiGiacomo/deepLearningVolatility 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `c49c51ac4669` · [字段定义](../../DATASET.md)*
