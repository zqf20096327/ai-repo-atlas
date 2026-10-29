# khedekarpratik0337/featureiq

⭐ 24 · Python · Apache-2.0 · 推送 2026-04-10 · [GitHub](https://github.com/khedekarpratik0337/featureiq) · 个人维护

**数据科学家用的上下文感知自动特征工程框架**

Python 库，将特征工程经验编码为带文献引用的规则知识图谱：自动剖析数据集列级统计特征，按问题类型与声明的算法匹配适用规则，生成 sklearn 兼容的转换管道。可选的元学习层用 OpenML 基准训练 LightGBM 对推荐重排序，无训练模型时回退到纯本体模式。支持 14 种下游算法与 5 类问题类型，提供验证、消融与带引用的解释 API。通过 pip 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 规则本体 + 文献引用的数据剖析驱动的特征转换推荐
- 可选 LightGBM/OpenML 元学习重排序，缺模型时回退本体模式
- 生成 sklearn 兼容管道，支持 14 种算法与 5 类问题类型
- 提供 validate/ablate/explain 等验证与解释 API

## 适用场景

- 我想自动为回归或分类任务生成合适的特征转换管道
- 我需要每步特征转换有文献出处可解释
- 我想验证特征转换相对基线是否真的提升模型表现

## 场景标签

 · 领域:数据科学/自动化机器学习

## 证据(README 行号)

> L14: FeatureIQ solves this by encoding feature engineering expertise into a structured ontology of rules, each backed by
> L97: 3. **Meta-Learning** (optional) -- A LightGBM model trained on OpenML benchmarks that predicts which transformation

## 星数曲线

```mermaid
xychart-beta
    title "khedekarpratik0337/featureiq 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-29 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `c16f5090a011` · [字段定义](../../DATASET.md)*
