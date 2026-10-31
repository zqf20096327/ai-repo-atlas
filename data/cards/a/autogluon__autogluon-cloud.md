# autogluon/autogluon-cloud

⭐ 41 · Python · Apache-2.0 · 推送 2026-10-12 · [GitHub](https://github.com/autogluon/autogluon-cloud) · [官网](https://auto.gluon.ai/cloud) · 组织维护

**为开发者提供在 AWS SageMaker 上训练与部署 AutoGluon 模型的 Python 库**

AutoGluon-Cloud 是 AutoGluon 团队推出的 Python 库，用于在 Amazon SageMaker 上训练与部署分类、回归和时间序列预测模型。用户传入 DataFrame（或本地路径、S3 URL）即可训练并在云端获得预测，无需编写训练脚本、推理处理器或序列化代码；基础设施与依赖由 AWS 维护的 AutoGluon Deep Learning Containers 承载。安装后需一次性运行 bootstrap 命令配置 IAM 角色与 S3 桶，计算资源在用户自己的 AWS 账户中运行。另支持 Chronos-2 等预训练基础模型的零样本时间序列预测。

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

- 在 Amazon SageMaker 上训练与部署分类/回归/时间序列模型
- 无需编写训练脚本、推理处理器与序列化代码，传 DataFrame 即用
- 运行于 AWS 官方维护的 AutoGluon Deep Learning Containers
- 支持 Chronos-2 等预训练时间序列基础模型的零样本预测

## 适用场景

- 把 AutoGluon 建模流程迁移到 AWS 云端，由云上算力完成训练与推理
- 不写胶水代码直接部署表格或时间序列预测器到 SageMaker
- 用预训练基础模型对时间序列做零样本预测

## 场景标签

`模型训练` `推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L10: AutoGluon-Cloud lets you train and deploy state-of-the-art ML models for classification, regression, and time serie
> L41: Train an AutoGluon predictor on your data and serve it from SageMaker. Full walkthrough: time series, tabular.

## 星数曲线

```mermaid
xychart-beta
    title "autogluon/autogluon-cloud 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-31 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `7b2f3b956eef` · [字段定义](../../DATASET.md)*
