# nshen7/alpha-gfn

⭐ 124 · Jupyter Notebook · 推送 2026-01-23 · [GitHub](https://github.com/nshen7/alpha-gfn) · 个人维护

**用 GFlowNet 深度强化学习挖掘量化投资公式型 alpha 因子的框架**

基于 Python 与 PyTorch 的深度强化学习应用：以 GFlowNet 作为策略模型，按概率与奖励成比例采样的方式生成多样化的公式型 alpha 因子。动作空间由一元/二元算子与 OHLCV 市场数据特征构成，状态以逆波兰记号表示表达式序列，奖励定义为信息相关（IC）平方并按缺失比例惩罚。Demo 仅使用 2018-2019 年标普 500 成分股日线数据，因工业保密协议仅含少量训练数据的演示示例，方法论实现位于 src/，训练流程见 notebooks。

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

- GFlowNet 按奖励成比例采样多样化 alpha 因子，区别于单最优解的 RL
- 奖励为 Spearman IC 平方乘以 (1-NaN%) 的日均值
- 动作空间覆盖 abs/log/滚动标准差等算子与 OHLCV 特征
- 提供 preprocess 与 train 两个 notebook 示例

## 适用场景

- 量化研究中自动生成候选 alpha 因子
- 作为 GFlowNet 在金融领域应用的参考实现
- 复现并扩展逆波兰记号表达式搜索的方法论

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L17: In this repo, we build an application that leverages a deep reinforcement learning framework to mine formulaic alph
> L44: 1. **Agent**: The learner or decision-maker that interacts with the environment. It takes actions and receives rewa

## 星数曲线

```mermaid
xychart-beta
    title "nshen7/alpha-gfn 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 123 --> 125
    line [124, 124]
```

2026-10-18 124 → 2026-10-30 124（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `fd42bd3d6e0b` · [字段定义](../../DATASET.md)*
