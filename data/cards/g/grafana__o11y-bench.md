# grafana/o11y-bench

⭐ 75 · Python · AGPL-3.0 · 推送 2026-10-25 · [GitHub](https://github.com/grafana/o11y-bench) · [官网](https://o11ybench.ai/) · 组织维护

**评测 LLM agent 在可观测性/SRE 任务上表现的开放基准**

基于 Harbor 构建的开放基准，将 agent 置于由 Grafana、Prometheus、Loki、Tempo 组成的真实可观测性环境中运行任务，采用确定性检查加评分细则进行判分，输出机器可读工件与 HTML 报告。任务规格源自 tasks-spec/，每 job 设统一场景时钟使不同时间启动的运行结果一致。默认提供自定义 agent，也可切换 Harbor 内置 agent 或自定义导入路径；模型经 LiteLLM 接入 OpenAI/Anthropic/Google/OpenRouter。本地运行需 mise、uv、Docker 及模型 provider API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 在真实 Grafana/Prometheus/Loki/Tempo 栈上运行并评测 agent
- 确定性检查与 rubric 标准双重判分，产出 HTML 报告
- 场景时钟机制使不同时间启动的运行与重评分结果一致
- 支持 OpenRouter 前缀运行任意可用模型，支持多种 agent 切换

## 适用场景

- 对比不同模型在可观测性/SRE 任务上的表现
- 评测自定义 Harbor agent 或 LangChain 编写的 agent
- A/B 对比 mcp-grafana 或 gcx 不同构建版本的效果

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L11: `o11y-bench` is an open benchmark for evaluating LLM agents on observability and SRE tasks.
> L12: It is built on top of Harbor and runs agents against a real
> L35: 4. Grades the result against deterministic checks plus rubric criteria

## 星数曲线

```mermaid
xychart-beta
    title "grafana/o11y-bench 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 74 --> 76
    line [75, 75]
```

2026-10-18 75 → 2026-10-25 75（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `b98de77672d2` · [字段定义](../../DATASET.md)*
