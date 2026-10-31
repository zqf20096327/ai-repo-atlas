# The-Swarm-Corporation/AdvancedResearch

⭐ 38 · Python · MIT · 推送 2026-08-03 · [GitHub](https://github.com/The-Swarm-Corporation/AdvancedResearch) · [官网](https://swarms.ai) · 组织维护

**基于 Anthropic 论文编排-工作者模式的多智能体研究系统**

用 swarms 框架实现的编排者-工作者（orchestrator-worker）多智能体研究系统：Director Agent 规划研究策略，多个专职 worker agent 通过 Exa API 并行执行搜索（ThreadPoolExecutor），再聚合综合为研究结果。支持 LLM-as-judge 评估、可配置模型（Claude/GPT）、多种输出格式（JSON/markdown）与带时间戳的 JSON 导出、批量查询与会话管理。以 pip 包发布，需 Python 3.10+，运行至少需要 EXA_API_KEY 及 ANTHROPIC 或 OPENAI 的 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Director Agent 规划 + worker agent 并行搜索的编排-工作者架构
- ThreadPoolExecutor 并行执行多智能体任务
- 支持自定义模型（Claude/GPT）、循环次数与 token 限制
- JSON/markdown 多输出格式与批量处理、会话管理

## 适用场景

- 给一个问题自动完成多智能体并行网络调研并生成报告
- 批量处理多个研究查询并导出 JSON 结果
- 按需切换 Claude/GPT 模型做自定义深度的迭代研究

## 场景标签

`多智能体` `科研工具` · 领域:Agent 开发

## 证据(README 行号)

> L11: An enhanced implementation of the orchestrator-worker pattern from Anthropic's paper, "How we built our multi-agent
> L119: |**Orchestrator-Worker Architecture**|A `Director Agent` coordinates research strategy while specialized worker ag

## 星数曲线

```mermaid
xychart-beta
    title "The-Swarm-Corporation/AdvancedResearch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-31 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `8bccee86fa48` · [字段定义](../../DATASET.md)*
