# posit-dev/orbital

⭐ 121 · Python · MIT · 推送 2026-10-27 · [GitHub](https://github.com/posit-dev/orbital) · [官网](https://posit-dev.github.io/orbital/) · 组织维护

**将 SKLearn 流水线与 PyTorch 前馈网络转为 SQL 查询**

Python 库：解析已训练的 scikit-learn 流水线和 PyTorch 前馈神经网络，生成可在数据库（如 DuckDB）中执行的 SQL 查询，使预测脱离 Python 环境运行。支持线性/逻辑回归、决策树、随机森林、梯度提升及前馈网络等模型；神经网络仅限前馈架构，卷积/循环/注意力/嵌入层不支持。README 声明为进行中项目，可能遇到 bug 或缺失功能，且并非所有变换和模型都能表示为 SQL。pip 安装，PyTorch 支持需额外安装 orbital[pytorch]。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 解析 SKLearn 流水线与 PyTorch 前馈网络并生成 SQL 查询
- 支持线性/逻辑回归、决策树、随机森林、梯度提升等 10 类模型
- 生成的 SQL 可在数据库中执行，无需 Python 环境

## 适用场景

- 将训练好的模型部署到数据库环境做批量预测
- 把模型推理嵌入 SQL 数据管道，脱离 Python 运行时
- 复用导出的 SQL 到其他系统中执行预测

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: Convert SKLearn pipelines and PyTorch neural networks into SQL queries for
> L4: execution in a database without the need for a Python environment.

## 星数曲线

```mermaid
xychart-beta
    title "posit-dev/orbital 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-30"]
    y-axis "stars" 119 --> 122
    line [120, 121, 121]
```

2026-10-18 120 → 2026-10-30 121（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `d1231f0e1329` · [字段定义](../../DATASET.md)*
