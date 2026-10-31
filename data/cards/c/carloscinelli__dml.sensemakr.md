# carloscinelli/dml.sensemakr

⭐ 20 · R · 推送 2026-10-23 · [GitHub](https://github.com/carloscinelli/dml.sensemakr) · [官网](http://carloscinelli.com/dml.sensemakr/) · 个人维护

**R 包：因果机器学习估计的敏感性分析工具套件**

R 语言包 dml.sensemakr，实现 Chernozhukov、Cinelli 等人（2026，Review of Economics and Statistics）论文所述的因果机器学习（Causal ML）遗漏变量偏误敏感性分析通用工具，面向使用去偏机器学习（Debiased ML）做因果推断的研究者。安装方式为通过 devtools 从 GitHub 安装开发版，CRAN 版本尚未发布（README 标注 coming soon），README 提供基本用法示例，理论细节指向论文与相关教程。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 实现因果机器学习遗漏变量偏误的敏感性分析方法
- 基于 Chernozhukov et al. (2026) 论文的方法
- 以 R 包形式提供，附基本用法代码示例

## 适用场景

- 对去偏机器学习的因果估计做稳健性与敏感性检验
- 评估遗漏变量对因果机器学习结论的影响
- 复现论文中的敏感性分析方法

## 场景标签

 · 领域:因果推断/计量经济学

## 证据(README 行号)

> L7: `dml.sensemakr` implements a general suite of sensitivity analysis tools
> L8: for Causal Machine Learning as discussed in [Chernozhukov, V., Cinelli,
> L32: For a primer on Debiased Machine Learning, [please check Chernozukohv et

## 星数曲线

```mermaid
xychart-beta
    title "carloscinelli/dml.sensemakr 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-31 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `837968654203` · [字段定义](../../DATASET.md)*
