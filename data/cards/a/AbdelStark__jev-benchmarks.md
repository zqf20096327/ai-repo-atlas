# AbdelStark/jev-benchmarks

⭐ 27 · Python · Apache-2.0 · 推送 2026-09-17 · [GitHub](https://github.com/AbdelStark/jev-benchmarks) · [官网](https://github.com/AbdelStark/jev-benchmarks#readme) · 个人维护

**类型化决策模型的概率感知评测框架：校准、选择性风险与延迟**

面向零样本单标签文本分类等类型化决策模型的评测框架：除准确率外，还测量多分类 Brier 分数、NLL、top-label ECE 等校准指标，固定误差预算下的最大可接受覆盖率，p50/p95 端到端延迟、token 用量与失败计数，并输出配对分层 bootstrap 置信区间。首个研究对比 TypeSafe Jev（托管 API）与 fastino/gliner2.5-multi-v1（本地推理）在三个 BTZSC 条件下的表现。通过 YAML 实验契约固定数据集与模型版本，JSONL 输出支持断点续跑，报告含 SHA-256 哈希。自我声明为 300 例试点而非排行榜。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 概率质量指标：多分类 Brier、NLL、top-label ECE
- 固定误差预算下的阈值可实现覆盖率（选择性自动化）
- 配对目标分层 bootstrap 置信区间
- 可复现契约：固定数据集/模型版本、协议预注册、构件 SHA-256 哈希

## 适用场景

- 评测分类模型概率输出是否校准到可支持自动化
- 对比多个分类后端在准确率、覆盖率和延迟上的表现
- 按可复现协议构建并归档评测实验

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L7: Probability-aware evaluation for typed decision models.
> L49: |Selective automation|Maximum threshold-realizable coverage at a fixed empirical error budget|

## 星数曲线

```mermaid
xychart-beta
    title "AbdelStark/jev-benchmarks 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-29"]
    y-axis "stars" 25 --> 28
    line [26, 27, 27]
```

2026-10-18 26 → 2026-10-29 27（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `6ee18dba0825` · [字段定义](../../DATASET.md)*
