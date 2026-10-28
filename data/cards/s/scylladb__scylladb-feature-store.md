# scylladb/scylladb-feature-store

⭐ 21 · Jupyter Notebook · 推送 2026-10-26 · [GitHub](https://github.com/scylladb/scylladb-feature-store) · [官网](https://feature-store.scylladb.com/) · 组织维护

**Feast + ScyllaDB 实时信贷评分示例应用（特征存储演示）**

基于 Feast 开源特征存储框架的示例工程：演示以 ScyllaDB Cloud 作为在线存储、parquet 文件作为离线存储，搭建实时信贷评分应用。流程包括创建 ScyllaDB Cloud 集群与 keyspace、安装依赖并配置 Feast（原生 ScyllaDB 连接器）、feast apply 部署、materialize-incremental 加载特征、run.py 训练并对单笔贷款申请给出判定，另提供 feast ui 与 Streamlit 交互演示。要求 Python 3 与 ScyllaDB Cloud 账户，面向 ML 基础设施使用者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 演示 Feast 以 ScyllaDB Cloud 为在线存储、parquet 为离线存储的完整配置流程
- Feast 内置原生 ScyllaDB 在线存储连接器，pip install feast[scylladb] 即可
- 包含特征物化、模型训练与单笔贷款申请评分的端到端示例
- 提供 feast ui 与本地 Streamlit 交互演示

## 适用场景

- 学习如何用 Feast 搭建以 ScyllaDB 为在线存储的特征存储
- 评估 ScyllaDB 在实时模型服务场景下的低延迟特征读取
- 参考实时信贷评分的离线训练与在线推理示例代码

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L7: This sample project is a real-time credit scoring application example that shows you how to set up Feast with Scylla
> L10: Feature store is a central data store to power operational machine learning models. They help you store transformed
> L20: * **Integration with Feast**: ScyllaDB integrates with the popular open-source feature store framework, Feast.

## 星数曲线

```mermaid
xychart-beta
    title "scylladb/scylladb-feature-store 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `5ebe078def01` · [字段定义](../../DATASET.md)*
