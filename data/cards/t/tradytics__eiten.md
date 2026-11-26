# tradytics/eiten

⭐ 3,331 · Python · GPL-3.0 · 推送 2026-11-24 · [GitHub](https://github.com/tradytics/eiten) · [官网](https://www.tradytics.com/) · 组织维护

**为投资者生成统计与算法投资组合的开源工具包**

Tradytics 开源的投资组合构建工具包，实现特征组合、最小方差、最大夏普比率与遗传算法四类策略。用户在 stocks.txt 中填入自选股票（建议 5-50 只），运行 portfolio_manager.py 后工具会基于 yahoo finance 历史数据生成多种组合权重，并用留出的样本外数据做回测与前向测试，还可与指定市场指数（如 SPY/QQQ）对比表现；协方差矩阵可用随机矩阵理论做噪声过滤。依赖 Scikit-learn/Numpy/Pandas/Yfinance 等包，以 Python 脚本形式运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四种组合策略：特征组合、最小方差、最大夏普比率、遗传算法
- 内置回测与前向测试框架，可与市场指数对比
- 随机矩阵理论噪声过滤协方差矩阵（可选开关）
- 蒙特卡洛模拟器模拟组合未来价格

## 适用场景

- 用自己挑选的一篮子股票构建多种算法投资组合
- 对候选组合做样本外回测与指数对比
- 用蒙特卡洛模拟组合未来价格走势

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L2: Eiten is an open source toolkit by Tradytics that implements various statistical and algorithmic investing strategie
> L80: 4. **Genetic Algorithm (GA) based Portfolio**


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `1ef70f42dd74` · [字段定义](../../DATASET.md)*
