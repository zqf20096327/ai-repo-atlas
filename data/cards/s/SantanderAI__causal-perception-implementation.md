# SantanderAI/causal-perception-implementation

⭐ 42 · Python · Apache-2.0 · 推送 2026-10-01 · [GitHub](https://github.com/SantanderAI/causal-perception-implementation) · [官网](https://github.com/SantanderAI) · 组织维护

**因果推断研究代码：在德国信贷数据上比较竞争 SCM 模型**

Santander AI Lab 开源、José M. Álvarez 著作的机器学习研究代码，随 forthcoming 论文发布。实现线性加性噪声模型（可配置因果 DAG，Chiappa 2019）、Pearl do-算子与反事实推断（ abduction→干预→预测）、三种一维分布距离（Wasserstein-2、KDE 近似 KL、总变差）、bootstrap 置信区间，以及公平决策实验（DP/EO 差距、ROC/PR、决策分歧）。数据不随仓库分发，首次运行从 OpenML 拉取 credit-g 并缓存；各实验以 python -m 模块方式运行，提供编程接口。面向因果推断与负责任 AI 研究者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 线性 ANM + 可配置因果 DAG（Chiappa 2019）拟合
- do-算子干预与三步反事实推断（abduction→干预→预测）
- Wasserstein-2 / KDE-KL / 总变差三种分布距离与 bootstrap 置信区间
- 公平决策实验：DP/EO 差距、ROC/PR、决策分歧

## 适用场景

- 复现论文中竞争 SCM 的因果感知比较实验
- 研究信贷决策场景下的算法公平性度量
- 作为线性 ANM 与 do-演算的参考实现进行扩展研究

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L13: research code for *causal perception* — comparing competing **structural causal
> L18: (Chiappa, 2019), Pearl's `do`-operator and counterfactual (abduction →
> L21: and a fair-decisions experiment (demographic-parity / equal-opportunity gaps,

## 星数曲线

```mermaid
xychart-beta
    title "SantanderAI/causal-perception-implementation 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-26 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `917b39954e39` · [字段定义](../../DATASET.md)*
