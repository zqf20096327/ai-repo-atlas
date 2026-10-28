# aildnont/HIFIS-model

⭐ 19 · Python · MIT · 推送 2026-09-19 · [GitHub](https://github.com/aildnont/HIFIS-model) · 组织维护

**用 HIFIS 数据预测慢性无家可归风险的神经网络模型（面向市政）**

为加拿大伦敦市无家预防部门构建的神经网络（多层感知机）分类模型：读取 HIFIS 4.0.57.30 数据库客户端数据，经预处理后在指定预测期内分类是否有慢性无家可归风险。训练流程含单次/多次训练选优，用 LIME 生成预测解释以支持透明度与偏差审查，并支持客户记录删除、特征移除与审计追踪等数据治理功能。定位为其他使用 HIFIS 的市政的交钥匙模板，需自有 HIFIS 数据库实例。

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

- 多层感知机模型，在指定预测期内分类慢性无家可归风险
- LIME 解释（全测试集/子模选取/单客户三种模式）
- 支持客户记录删除、特征移除与审计追踪等数据治理功能
- 多次训练按指标偏好（如 recall）保存最优模型

## 适用场景

- 市政无家预防部门识别有慢性无家可归风险的客户
- 其他使用 HIFIS 的市政基于本地数据复现训练
- 对政府预测系统生成可解释性报告与偏差分析

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L11: train a neural network model to classify clients in the city's
> L14: (HIFIS) database as either at risk or not at risk of chronic
> L15: homelessness within a specified predictive horizon. In an effort to

## 星数曲线

```mermaid
xychart-beta
    title "aildnont/HIFIS-model 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `6902153375f1` · [字段定义](../../DATASET.md)*
