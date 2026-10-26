# schampon/skfin

⭐ 49 · Jupyter Notebook · MIT · 推送 2026-09-28 · [GitHub](https://github.com/schampon/skfin) · 个人维护

**量化投资组合管理的机器学习工具库（基于 scikit-learn）**

skfin 是面向投资组合管理与交易策略的 Python 库，构建在 scikit-learn 之上：提供 Backtester 回测框架、MeanVariance/Ridge 等估计器，并内置数据集加载（如 load_kf_returns）。仓库以一组 notebook 形式覆盖机器学习在组合管理中的主题，附 pytest 测试与设计规范文档。安装通过 git clone 加脚本创建 conda/mamba 环境（Python 3.12）并以可编辑模式安装，可选 extras 包括 nlp、llm、boost、optim。LLM notebook 需设置 OPENAI_API_KEY 环境变量。

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

- 提供 Backtester 回测框架与 MeanVariance/Ridge 估计器
- 内置示例数据集加载（load_kf_returns）
- 教程型 notebook 覆盖组合管理机器学习主题，可合并为 PDF
- 可选依赖扩展：nlp/llm/boost/optim

## 适用场景

- 用机器学习模型做投资组合管理策略回测
- 学习组合管理与交易的机器学习方法（notebook 教程）
- 在量化研究中复用 scikit-learn 风格的估计器

## 场景标签

`金融量化` `教程课程` · 领域:学习与行业

## 证据(README 行号)

> L2: Machine learning for portfolio management and trading with scikit-learn
> L12: An example to run a simple backtest with learning using a `Ridge` estimator:

## 星数曲线

```mermaid
xychart-beta
    title "schampon/skfin 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 48 --> 50
    line [49, 49]
```

2026-10-18 49 → 2026-10-26 49（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `53899e379b7d` · [字段定义](../../DATASET.md)*
