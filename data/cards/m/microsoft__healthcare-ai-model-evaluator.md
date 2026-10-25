# microsoft/healthcare-ai-model-evaluator

⭐ 59 · TypeScript · MIT · 推送 2026-08-27 · [GitHub](https://github.com/microsoft/healthcare-ai-model-evaluator) · 组织维护

**医疗 AI 模型评测基准平台：供医护团队验证模型输出**

微软开源的医疗 AI 模型评测与基准平台，面向数据科学家与临床研究人员协作场景。提供 Web Arena 界面做模型对比、专家评审工作流、多评审者（人+AI）汇总、基于 Azure OpenAI 的 LLM-as-Judge 主观评测，内置 ROUGE/BERTScore/TBFact/精确匹配等指标与 Elo 排名，支持多模态输入，可接 Azure OpenAI、AI Foundry、Azure ML 端点与自定义 REST API。通过 azd 全量部署到用户自己的 Azure 订阅，数据自管；要求 PHI 脱敏合规，数据集 180 天自动删除。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Web Arena 界面做多模型对比与专家评审工作流
- 内置 ROUGE/BERTScore/TBFact/Elo 等指标与自定义评测器扩展架构
- 模型连接器：Azure OpenAI、AI Foundry、Azure ML、自定义 REST API
- azd 一键部署到自有 Azure 订阅，数据不经第三方

## 适用场景

- 医疗团队在不写代码的界面上对比和验证候选 AI 模型
- 临床专家按自定义评审标准系统性核查模型输出
- 用 LLM-as-Judge 与自动指标生成模型基准评测报告

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: Healthcare AI Model Evaluator is a medical AI model benchmarking platform with integrated evaluation engine to assis
> L14: - **Model-as-Judge**: LLM-based evaluation via Azure OpenAI for subjective metrics and complex assessments
> L15: - **Built-in Metrics**: Automated computation including exact match, ROUGE, BERTScore, TBFact factual consistency, 

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/healthcare-ai-model-evaluator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 58 --> 60
    line [59, 59]
```

2026-10-18 59 → 2026-10-25 59（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `aeeb7eacd42b` · [字段定义](../../DATASET.md)*
