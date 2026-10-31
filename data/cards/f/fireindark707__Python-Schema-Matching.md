# fireindark707/Python-Schema-Matching

⭐ 43 · Python · Apache-2.0 · 推送 2026-03-08 · [GitHub](https://github.com/fireindark707/Python-Schema-Matching) · 组织维护

**表格模式匹配工具：预测两个表列的对应关系**

论文 SMUTF 的代码，用 XGBoost 与 sentence-transformers 做表格 schema matching：对两表的列做规则特征工程（数值/长度/字符比例统计）与语义嵌入（列名与实例的余弦相似度），由 XGBoost 分类器输出列对匹配预测。以 pip 包提供一行式 API（输入 csv/json/jsonl，返回预测矩阵与匹配列对），也可运行源码脚本训练与推理；支持 one-to-one/one-to-many/many-to-many 三种匹配策略与阈值调节，多语言列名匹配。配套开放了 HDXSM 人道主义数据集。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 规则特征 + sentence-transformers 嵌入 + XGBoost 的混合特征方案
- 一行式 API：输入两表文件，返回预测矩阵与匹配列对
- 三种匹配策略（one-to-one/one-to-many/many-to-many）与阈值调节
- 开放 HDXSM 数据集，支持多语言列名匹配

## 适用场景

- 数据集成前对两个表自动找出对应列
- 跨领域/开放域表格的模式匹配
- 复现论文结果或用自有数据训练匹配模型

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L7: We introduce SMUTF, a unique approach for large-scale tabular data schema matching (SM), which assumes that supervis
> L38: df_pred,df_pred_labels,predicted_pairs = schema_matching("Test Data/QA/Table1.json","Test Data/QA/Table2.json")

## 星数曲线

```mermaid
xychart-beta
    title "fireindark707/Python-Schema-Matching 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-31 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `50e40f75e17b` · [字段定义](../../DATASET.md)*
