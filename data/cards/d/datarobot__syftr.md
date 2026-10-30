# datarobot/syftr

⭐ 345 · Python · MIT · 推送 2026-03-04 · [GitHub](https://github.com/datarobot/syftr) · 组织维护

**agent 工作流优化器：按预算搜索 Pareto 最优流程**

用户自带数据集，从模型与组件组合出搜索空间，syftr 通过多目标贝叶斯优化与自研 Pareto Pruner 采样 agentic 与非 agentic 流程，估计准确率与成本/延迟/吞吐之间的 Pareto 前沿。构建在 Ray（分布式调度）、Optuna（多目标优化）、LlamaIndex（RAG 工作流）之上。以 Python 库与 CLI 形式提供，需 config.yaml、study 文件与 Azure OpenAI 凭据；示例需 API key，默认用 SQLite 存储，分布式负载建议 Postgres。附有 AutoML 2025 论文。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多目标贝叶斯优化估计 accuracy 与 cost/latency/吞吐的 Pareto 前沿
- 自研 Pareto Pruner 剪枝加速搜索
- 基于 Ray 的 CPU/GPU 集群分布式搜索
- 可配置多种 LLM 提供方并在 config.yaml 中定义成本结构

## 适用场景

- 在给定预算下为我的 agent/RAG 应用挑选最优工作流组合
- 对比不同 LLM 与流程配置在准确率与成本上的权衡
- 用自定义数据集与自定义 flow 类扩展搜索空间

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: __syftr__ is an agent optimizer that helps you find the best agentic workflows for a given budget. You bring your ow
> L18: * Optuna for its flexible define-by-run interface (similar to PyTorch’s eager execution) and support for state-of-t

## 星数曲线

```mermaid
xychart-beta
    title "datarobot/syftr 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-30"]
    y-axis "stars" 343 --> 346
    line [344, 345, 345]
```

2026-10-18 344 → 2026-10-30 345（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `b50467e1aacd` · [字段定义](../../DATASET.md)*
