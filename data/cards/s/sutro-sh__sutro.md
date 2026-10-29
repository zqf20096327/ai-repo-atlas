# sutro-sh/sutro

⭐ 19 · Python · Apache-2.0 · 推送 2026-10-24 · [GitHub](https://github.com/sutro-sh/sutro) · [官网](https://sutro.sh) · 组织维护

**构建与运行 LLM 判分/分类/抽取任务的 Python SDK 与批量推理平台**

Sutro 提供 Python SDK 与 CLI，面向团队构建基于偏好的 LLM 判分器、分类器与抽取器（Sutro Functions），并通过 Sutro Batch 在自有部署上执行无服务器异步批量推理。数据源支持列表、Pandas/Polars DataFrame、本地 CSV/Parquet/TXT 及 S3 与 HTTP(S) URL，结果以 Parquet/DataFrame 返回并保留输入顺序。SDK 无集中式 API 回退，密钥仅发往配置的部署地址；Functions 处于 research preview，需联系获取访问权限。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 定义任务后部署可在线或批量调用的判分/分类/抽取 Function
- Sutro Batch 支持大规模批量推理、估算作业与断点续传恢复
- 支持多模型比较、嵌入生成与作业管理（Python 与 CLI）

## 适用场景

- 对模型输出与 agent 轨迹做大规模评审与 QA 门控
- 批量分类工单、线索与业务记录并抽取结构化字段
- 生成合成数据、语义标注与大规模嵌入

## 场景标签

`模型评测` `MLOps` `推理引擎` · 领域:评测与运维

## 证据(README 行号)

> L8: Sutro helps teams build grounded LLM judges, classifiers, and extractors, then run them confidently at scale.
> L36: Sutro Batch is serverless async inference for high-volume AI workloads. Run Sutro Functions or pre-trained open-sou
> L143: You can also run pre-trained LLMs directly with `infer`. This is useful for prototyping, evals, extraction, classi

## 星数曲线

```mermaid
xychart-beta
    title "sutro-sh/sutro 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `3179f5dd2057` · [字段定义](../../DATASET.md)*
