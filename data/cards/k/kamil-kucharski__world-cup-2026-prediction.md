# kamil-kucharski/world-cup-2026-prediction

⭐ 13 · Jupyter Notebook · 推送 2026-06-14 · [GitHub](https://github.com/kamil-kucharski/world-cup-2026-prediction) · 个人维护

**预测 2026 世界杯各队夺冠概率的机器学习 notebook**

基于历史国际比赛结果（2010 年起）与 FIFA 排名数据训练两个 Poisson 回归模型（分别预测主客队进球数），特征包括双方 FIFA 排名与积分、排名差、积分差、东道主与中立场指示变量。随后从 Poisson 分布抽样模拟单场比分，完整模拟小组赛至决赛，默认运行 1000 次蒙特卡洛模拟，输出各队夺冠概率、预测小组排名与淘汰赛示例对阵。README 明确列出模型未纳入伤病、旅途、点球等因素。以 Jupyter notebook 形式提供，附三个 CSV 数据文件。

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

- 双 Poisson 回归模型预测两队进球数
- 默认 1000 次蒙特卡洛模拟完整赛程
- 输出夺冠概率、小组排名与淘汰赛示例对阵
- README 明确列出模型局限（伤病/旅途/点球等未纳入）

## 适用场景

- 我想看 2026 世界杯各队夺冠概率的量化估计
- 我想了解 Poisson 回归+蒙特卡洛模拟赛事的完整流程
- 在 notebook 中复用数据与流程做自己的世界杯预测

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: This project is a machine learning notebook for predicting the 2026 FIFA World Cup. It uses historical international
> L21: The notebook trains two Poisson regression models:
> L39: After training, the notebook simulates matches by drawing goals from a Poisson distribution.

## 星数曲线

```mermaid
xychart-beta
    title "kamil-kucharski/world-cup-2026-prediction 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `71de854a5089` · [字段定义](../../DATASET.md)*
