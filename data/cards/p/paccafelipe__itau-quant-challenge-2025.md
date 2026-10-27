# paccafelipe/itau-quant-challenge-2025

⭐ 23 · Jupyter Notebook · MIT · 推送 2026-02-28 · [GitHub](https://github.com/paccafelipe/itau-quant-challenge-2025) · 个人维护

**面向 Ibovespa 的拓扑数据分析量化配置策略框架**

Itaú Quant Challenge 2025 的参赛项目（自称排名 40/953）：纯多头量化配置框架，针对 Ibovespa 股票池。核心机制为三部分：用持久同调（Vietoris-Rips 过滤）检测市场结构压力并触发 Risk-Off；用 Mapper 算法按拓扑行为聚类资产、区分外围/中心资产；用 Ridge/ElasticNet 集成模型（Meta-Blend）按当前状态动态确定动量、质量、Carry 因子权重，最终以 HRP 构建组合。回测采用 Walk-Forward（504 天训练/126 天测试），含回撤 kill-switch 与换手控制；验证期为 2017-09 至 2025-10。环境用 uv 或 pip 管理，需 Python 3.10+，可经 CLI、脚本或 notebook 复现全流程。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 持久同调（Vietoris-Rips 过滤）检测市场结构断裂并自动降低仓位
- Mapper 按拓扑行为聚类资产，区分外围（特质/安全）与中心（系统性）资产
- Ridge/ElasticNet Meta-Blend 按状态动态确定因子权重，HRP 构建组合
- Walk-Forward 验证（504d/126d）附 Deflated Sharpe 检验与敏感性分析

## 适用场景

- 在巴西 Ibovespa 市场上做状态感知的组合配置与回测
- 复现参赛结果或在其基础上研究 TDA 量化因子
- 参考持久同调与 Mapper 用于金融时间序列分析的实现

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L11: **Atlas** is a long-only quantitative allocation framework that uses *Topological Data Analysis* and *Machine Learn
> L82: ### 3. Meta-Blend (Machine Learning)

## 星数曲线

```mermaid
xychart-beta
    title "paccafelipe/itau-quant-challenge-2025 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-27 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `84b09518bb99` · [字段定义](../../DATASET.md)*
