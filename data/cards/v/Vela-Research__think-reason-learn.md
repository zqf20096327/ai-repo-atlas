# Vela-Research/think-reason-learn

⭐ 20 · Python · MIT · 推送 2026-10-18 · [GitHub](https://github.com/Vela-Research/think-reason-learn) · [官网](https://thinkreasonlearn.com/) · 组织维护

**以 LLM 为推理函数重写经典 ML 算法的 Python 库**

TRL 扩展传统机器学习：将决策树、随机森林等核心算法重新实现，使模型的每一步调用 LLM 作为推理函数，替代静态启发式。核心算法包括 GPTree（LLM 引导决策树）、RRF（LLM 生成规则的集成）、Policy Induction、RRM 与 Verifiable RL；每个预测附带可追溯的推理路径。安装需 Python 3.13+、pip 与 Graphviz 系统包；运行需配置聊天模型（OpenAI/Google/Anthropic/xAI）与默认回答模型 Jev（Typesafe System One）的 API key，费用设 10 美元默认上限。由 Vela Research 与牛津大学合作开发，首批应用为风险投资领域，框架本身领域无关。

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

- GPTree/RRF/Policy Induction 等 LLM 引导的经典 ML 算法实现
- 每个预测附带可追溯的推理路径、规则或聚类描述
- 全异步设计，面向并发 LLM 交互
- fit()/predict() 前打印预估 Jev 费用并默认设 10 美元上限

## 适用场景

- 在需要可解释预测的高风险决策场景（风控、法律、医疗）中建模
- 用 LLM 推理替代静态启发式训练决策树与规则集成
- 从数据中挖掘自然语言 IF-THEN 规则并组成加权集成

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L4: TRL is an open-source Python library that extends traditional machine learning with language-based reasoning.
> L5: It re-implements core algorithms such as decision trees and random forests so that each step of the model can call o
> L20: - **GPTree**: LLM-guided decision trees for dynamic feature generation.

## 星数曲线

```mermaid
xychart-beta
    title "Vela-Research/think-reason-learn 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `64814f1f1183` · [字段定义](../../DATASET.md)*
