# GAMS-dev/gamspy

⭐ 136 · Python · NOASSERTION · 推送 2026-10-24 · [GitHub](https://github.com/GAMS-dev/gamspy) · [官网](https://gamspy.readthedocs.io) · 组织维护

**Python 数学优化建模库：代数式构建并求解规划模型**

GAMS-dev 维护的开源 Python 包，用于构建和求解数学优化模型：以代数式、按集合索引的 API 表达变量与约束，支持线性、混合整数、非线性、二次约束与互补模型；模型数据可从 Python 列表、NumPy 数组或 pandas 对象载入，结果以 pandas DataFrame 返回。安装自带本地执行运行时与默认求解器，可接开源及商业求解器。Python 源码采用 MIT 许可，但运行时与求解器受单独的 demo/个人/学术/商业许可条款约束。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 代数式索引 API 支持线性、混合整数、非线性、二次约束与互补模型
- 兼容开源与商业求解器，切换无需重写模型
- pip 安装自带本地执行运行时与默认求解器，无需单独安装 GAMS
- 与 NumPy/pandas 数据工作流集成

## 适用场景

- 在 Python 中构建并求解生产排产、资源分配等规划模型
- 数据分析流程中嵌入优化求解并处理 pandas 数据
- 教学中以接近数学符号的语法定义优化问题

## 场景标签

 · 领域:数学优化/运筹学

## 证据(README 行号)

> L10: GAMSPy is an open-source Python package for building and solving mathematical optimization models. Its algebraic, i
> L41: - **Choice of solver:** Use compatible installed solvers without rewriting the model. GAMSPy provides access to bot

## 星数曲线

```mermaid
xychart-beta
    title "GAMS-dev/gamspy 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 135 --> 137
    line [136, 136]
```

2026-10-18 136 → 2026-10-25 136（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `e2d70bfff383` · [字段定义](../../DATASET.md)*
