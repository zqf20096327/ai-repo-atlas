# MachSMT/MachSMT

⭐ 28 · Python · 推送 2026-08-28 · [GitHub](https://github.com/MachSMT/MachSMT) · [官网](https://machsmt.github.io/) · 组织维护

**SMT 求解器的机器学习算法选择工具**

面向 SMT（可满足性模理论）求解器的算法选择工具：读取 CSV 数据文件（benchmark/solver/score 三列）构建内部数据库，训练模型预测每个 .smt2 基准应选用哪个求解器，提供 build/train/eval/predict 四种 CLI 模式。训练支持 scikit-learn、xgboost、pytorch 三种框架（--ml-core 指定），可用 GPU；默认采用经验难度模型（EHM），另支持贪心与成对比较器。eval 模式用 k 折交叉验证生成 cactus/CDF/par2 报告。通过 pip 安装，源码构建需 Ubuntu 18+、Python 3.7+ 与 make。作者团队来自学术界，配套 STTT 期刊论文。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- build/train/eval/predict 四模式 CLI，按基准预测最优 SMT 求解器
- ML 框架无关：scikit-learn/xgboost/pytorch 可选，支持 GPU 训练
- 默认经验难度模型（EHM），另有贪心与成对比较器
- k 折交叉验证评估并生成 cactus/CDF/par2 报告

## 适用场景

- 为 SMT-LIB 基准自动选择最合适的求解器
- 训练并评估求解器选择模型，比较虚拟求解器与各真实求解器表现
- 研究论文配套复现（TACAS/STTT artifact）

## 场景标签

 · 领域:形式验证/自动推理

## 证据(README 行号)

> L1: # MachSMT -- An ML-Driven Algorithm Selection Tool for SMT Solvers
> L60: For example, `machsmt build -f a.csv b.csv c.csv`
> L94: This is the main prediction interface to machsmt. This is the default mode of machsmt.

## 星数曲线

```mermaid
xychart-beta
    title "MachSMT/MachSMT 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-26 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `021a2cf26d3e` · [字段定义](../../DATASET.md)*
