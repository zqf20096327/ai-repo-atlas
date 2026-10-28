# mindsdb/type_infer

⭐ 27 · Python · GPL-3.0 · 推送 2026-09-11 · [GitHub](https://github.com/mindsdb/type_infer) · 组织维护

**面向 ML 流水线的表格数据列类型自动推断库**

MindsDB 维护的 Python 库，针对表格数据为每列推断适合机器学习用途的数据类型：例如日期/时间格式的字符串被归为时间戳，唯一值数量较少的整数列被归为类别型。作为 ML 流水线中的数据预处理环节使用，通过 pip 安装，提供 git clone 加可编辑模式的开发环境搭建流程与 unittest 单元测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 针对表格数据逐列推断 ML 场景下的最优数据类型
- 日期格式字符串识别为时间戳、低基数整数识别为类别型
- 以 pip 包形式提供，含开发环境与单元测试流程

## 适用场景

- 在 ML 建模前自动确定表格各列的数据类型
- 数据科学流水线中替代手工列类型标注

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L21: Automated type inference for Machine Learning pipelines.
> L23: In the context of tabular data, `type_infer` aims for optimal interpretation of each column’s data type for ML use 

## 星数曲线

```mermaid
xychart-beta
    title "mindsdb/type_infer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-28 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `73056331d76a` · [字段定义](../../DATASET.md)*
