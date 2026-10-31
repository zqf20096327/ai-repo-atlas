# causalis-causalcraft/Causalis

⭐ 24 · Python · MIT · 推送 2026-10-18 · [GitHub](https://github.com/causalis-causalcraft/Causalis) · [官网](https://causalis.causalcraft.com/) · 组织维护

**面向实验与观察研究的 Python 因果推断库**

Python 因果推断库，按研究场景（Classic RCT、CUPED、Unconfoundedness/DML IRM）组织，提供一致的 fit()→estimate() 工作流与 Pydantic 数据契约。功能包括 CUPED 方差缩减、多臂多结局实验估计、SRM 检查、样本量与 MDE 实验规划，以及带异质性处理效应的 DGP 模拟数据生成器。面向做 A/B 测试与观察研究的数据科学从业者；限制包括聚类/区组实验不适用、置信区间不做多重性校正、历史 API 已移除且无弃用包装。

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

- 场景化工作流（RCT/CUPED/Unconfoundedness）与一致 fit()→estimate() 接口
- CUPED 估计、样本量与 MDE 实验规划计算器
- Pydantic 数据契约与稳健性检查（SRM 检测等）
- 带异质性处理效应、潜变量与相关混杂的 DGP 模拟生成器

## 适用场景

- A/B 实验效应估计与 CUPED 方差缩减
- 上线前根据历史对照数据规划样本量与 MDE
- 观察研究中用 DML/IRM 估计处理效应

## 场景标签

 · 领域:因果推断/实验科学

## 证据(README 行号)

> L11: Robust causal inference for experiments and observational studies in Python, organized around **scenarios** (e.g., 
> L83: # Quickstart: Observational study (Unconfoundedness / DML IRM)

## 星数曲线

```mermaid
xychart-beta
    title "causalis-causalcraft/Causalis 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-31 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `b2175357386f` · [字段定义](../../DATASET.md)*
