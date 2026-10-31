# szybnev/redteam-ai-benchmark

⭐ 18 · Python · MIT · 推送 2026-07-13 · [GitHub](https://github.com/szybnev/redteam-ai-benchmark) · 个人维护

**评估 LLM 红队/攻防安全问答能力的 CLI 基准**

面向授权攻防安全场景的模型评测基准 CLI：向配置的 LLM 端点发送 60 道红队问题（覆盖 Windows、AD、Web、云与 IAM、容器等 10 个领域、5 级难度），以确定性 rubric 词典匹配评分，输出拒答率、词汇覆盖、致命错误率等审计指标；另提供离线 LLM-as-Judge 复核、排行榜生成与提示优化（仅针对被审查响应）。支持 Ollama、LM Studio、OpenWebUI、OpenRouter 四种提供方，需 Python 3.13+ 与 uv。明确声明不是黑客工具、不执行模型输出。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 60 题 v2 数据集按领域与 5 级难度（L1-L5）组织
- 确定性 rubric 评分，无需外部 LLM 法官，记录匹配证据
- 离线 LLM-as-Judge 复核与可校验的排行榜产物生成
- 可选提示优化仅针对被审查响应，不替换基线得分

## 适用场景

- 在本地 Ollama/LM Studio 模型上跑红队能力基准测试
- 对模型拒绝或审查响应的比例与覆盖做审计
- 比较多个模型在攻防安全问答上的表现并生成排行榜

## 场景标签

`模型评测` `网络安全` · 领域:评测与运维

## 证据(README 行号)

> L5: Red Team AI Benchmark is a CLI **model-evaluation benchmark**. It measures how LLMs understand and respond to red-te
> L16: project_type: LLM evaluation benchmark
> L18: execution_target: configured LLM provider, optional judge, and optional tracing services

## 星数曲线

```mermaid
xychart-beta
    title "szybnev/redteam-ai-benchmark 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-31"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-31 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `c6183112de18` · [字段定义](../../DATASET.md)*
