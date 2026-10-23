# jma127/pyltr

⭐ 463 · Python · BSD-3-Clause · 推送 2025-12-27 · [GitHub](https://github.com/jma127/pyltr) · 个人维护

**Python 学习排序（LTR）工具包：排序模型与评测指标**

面向排序学习任务的 Python 工具包，提供 LambdaMART 排序模型（支持验证集早停与查询子采样）、NDCG/ERR/AP/Kendall's Tau/AUC-ROC 等评测指标，以及 LETOR 格式数据读取器、查询分组校验等数据处理工具。示例演示了导入 MQ2007 数据集、训练与评估的完整流程。代码基于 Python 2 语法（示例中 print 为语句形式），通过 PyPI 分发，附带单元测试脚本与 Sphinx 文档构建流程。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LambdaMART 模型，支持验证早停与查询子采样
- NDCG/ERR/AP/Kendall's Tau/AUC-ROC 评测指标
- LETOR 数据集读取器与查询分组工具
- 提供单元测试脚本与文档构建说明

## 适用场景

- 在 LETOR 数据集上训练学习排序模型
- 计算搜索排序结果的 NDCG 等评测指标
- 构建排序系统时做数据处理与查询分组校验

## 场景标签

 · 领域:机器学习/信息检索

## 证据(README 行号)

> L10: pyltr is a Python learning-to-rank toolkit with ranking models, evaluation
> L47:  model = pyltr.models.LambdaMART(

## 星数曲线

```mermaid
xychart-beta
    title "jma127/pyltr 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 462 --> 464
    line [463, 463]
```

2026-10-18 463 → 2026-10-23 463（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `5a5c04234f1c` · [字段定义](../../DATASET.md)*
