# julianspaeth/random-survival-forest

⭐ 66 · Python · MIT · 推送 2026-07-30 · [GitHub](https://github.com/julianspaeth/random-survival-forest) · 个人维护

**Python 随机生存森林实现：生存预测与风险分析**

提供 Ishwaran et al. (2008) 随机生存森林方法的 Python 实现，用于生存分析预测。log-rank 分割搜索用 numpy 向量化，支持 n_jobs 跨核并行构建树。要求 Python >= 3.13，通过 pip 安装；开发环境使用 uv 管理依赖，附带 pytest 测试与 ruff/pip-audit 检查。以 MIT 许可开源，面向做生存预测的机器学习开发者与科研用户。

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

- Ishwaran et al. (2008) 随机生存森林的 Python 实现
- log-rank 分割搜索经 numpy 向量化，训练随样本量与树数扩展
- n_jobs 支持跨核并行构建树
- 附带论文 DOI 引用与测试套件

## 适用场景

- 对带删失的时间到事件数据做生存预测
- 在科研项目中复现随机生存森林方法
- 估计样本的风险函数与生存函数

## 场景标签

 · 领域:机器学习/统计分析

## 证据(README 行号)

> L5: The Random Survival Forest package provides a python implementation of the survival prediction method originally pub
> L39: The log-rank split search is vectorized with numpy, so training scales well with sample size and number of trees. F

## 星数曲线

```mermaid
xychart-beta
    title "julianspaeth/random-survival-forest 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 64 --> 67
    line [65, 66]
```

2026-10-18 65 → 2026-10-24 66（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `c9863bca4f8f` · [字段定义](../../DATASET.md)*
