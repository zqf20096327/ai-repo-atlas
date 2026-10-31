# mad-lab-fau/tpcp

⭐ 21 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/mad-lab-fau/tpcp) · [官网](https://tpcp.readthedocs.io/en/latest/) · 组织维护

**面向复杂算法评估的 Python 流水线与数据集辅助框架**

面向含机器学习成分的复杂算法研究场景（如多参与者传感器数据的 HMM 事件检测），提供面向对象的数据集类与带 run/optimize 接口的算法/流水线类，并内置交叉验证与网格搜索等评估构造。将所有参数/权重修改统一抽象为优化，支持从网格搜索到神经网络超参调优的统一接口。以 Python 库发布于 PyPI，附 JOSS 论文；被 gaitmap、mobgap 等项目用作算法评估基础。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 可拆分、迭代、查询的面向对象数据集类
- run/optimize 接口适配任意算法实现
- 内置交叉验证与网格搜索并尝试捕获明显错误
- 统一优化抽象：从网格搜索到神经网络超参调优

## 适用场景

- 为多模态、非表格数据的研究算法搭建评估流程
- 实现跨库、非 fit-predict 范式算法的参数优化与交叉验证
- 以自文档化类封装复杂数据源供团队复用

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L10: A generic way to build object-oriented datasets and algorithm pipelines and tools to evaluate them.
> L29: Evaluating Algorithms - in particular when they contain machine learning - is hard.
> L50: With `tpcp` we want to provide a flexible framework to approach such complex problems with structure and confidence

## 星数曲线

```mermaid
xychart-beta
    title "mad-lab-fau/tpcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-31 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `e42de5a094f2` · [字段定义](../../DATASET.md)*
