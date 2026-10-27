# microsoft/genaiops-promptflow-template

⭐ 369 · Python · NOASSERTION · 推送 2026-09-15 · [GitHub](https://github.com/microsoft/genaiops-promptflow-template) · 组织维护

**微软的 Prompt Flow LLMOps 模板：LLM 应用的实验、评估与部署流程**

面向使用 Prompt Flow 构建 LLM 应用的工程团队的操作化模板：集中托管多个 flow 代码，覆盖生命周期管理、变体与超参实验、A/B 部署、多数据集评估、CSV/HTML 报告生成与部署后端点测试。支持 Azure AI Studio 与 Azure Machine Learning 两种平台，可本地或云端执行实验与评估，CI/CD 编排支持 GitHub、Azure DevOps 与 Jenkins，部署目标含 Kubernetes、Azure Web Apps 与 AML 托管算力。附 6 个示例（网页分类、NER、数学编码、Chat with PDF、函数流、类流）。限制：绑定 Azure/Prompt Flow 生态，配置驱动开发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 变体与超参实验及多数据集/flow 多对多评估
- A/B 部署与部署后端点就绪测试
- 支持 AI Studio 与 AML、本地/云端双路径执行
- GitHub / Azure DevOps / Jenkins 三种 CI/CD 编排

## 适用场景

- 团队在单一仓库集中管理多个 Prompt Flow 的实验与评估
- 将 LLM flow 从本地迭代推进到生产部署并做 A/B 对比
- 为 prompt 变体批量跑评估并生成指标报告

## 场景标签

`模型评测` `MLOps` · 领域:评测与运维

## 证据(README 行号)

> L20: It is an experimentation and evaluation framework for Prompt Flow. It is just not CI/CD pipelines for Prompt Flow, 
> L61: That's where **LLMOps with Prompt flow** comes in. LLMOps with Prompt flow is a "LLMOps template and guidance" to h
> L35: This template supports:

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/genaiops-promptflow-template 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-27"]
    y-axis "stars" 367 --> 370
    line [368, 369, 369]
```

2026-10-18 368 → 2026-10-27 369（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `a778dce1c0bf` · [字段定义](../../DATASET.md)*
