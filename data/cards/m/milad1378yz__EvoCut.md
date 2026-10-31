# milad1378yz/EvoCut

⭐ 13 · Python · 推送 2026-09-01 · [GitHub](https://github.com/milad1378yz/EvoCut) · 个人维护

**用进化搜索与 LLM 为 MILP 自动生成加速割平面的 Python 库**

面向混合整数线性规划（MILP）的 Python 库：通过进化搜索与 LLM 生成问题特定的割平面（cutting planes），注入 LP 松弛以缩小可行域、提升求解效率。提供数据预处理脚本、主程序运行入口、割平面最优解保持率验证与测试集评估脚本；README 附 IMO 2025 P6 铺砖问题的实验结果。需配置模板文件填入凭证与超参数，依赖商业 MILP 求解器（如 Gurobi，需许可证），推荐 Python 3.9。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 进化搜索 + LLM 自动生成问题特定割平面
- 提供割平面最优解保持率验证脚本
- 配置文件模板化，种子可配置以保证确定性
- 附 IMO 2025 P6 问题的实验评估结果

## 适用场景

- 为 MILP 求解实例自动生成加速割平面
- 验证生成割平面对最优解的保持率
- 在留出测试实例上评估割平面效果

## 场景标签

 · 领域:运筹优化/整数规划

## 证据(README 行号)

> L8: **EvoCut** is a Python library that accelerates Mixed-Integer Linear Programming (MILP) by injecting problem-specifi
> L18: - Implication: Demonstrates EvoCut's applicability to new, previously unseen problems for LLMs, the IMO 2025 P6 til

## 星数曲线

```mermaid
xychart-beta
    title "milad1378yz/EvoCut 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 low · 依据 README sha `471e6f49bb2b` · [字段定义](../../DATASET.md)*
