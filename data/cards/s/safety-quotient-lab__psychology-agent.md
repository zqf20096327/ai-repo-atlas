# safety-quotient-lab/psychology-agent

⭐ 20 · Python · Apache-2.0 · 推送 2026-05-01 · [GitHub](https://github.com/safety-quotient-lab/psychology-agent) · [官网](https://unratified.org) · 组织维护

**基于 Claude Code 的多智能体心理学分析与咨询系统**

构建在 Claude Code CLI 之上的心理学 agent 系统：一个同侪导师 agent 加五个对等子 agent（含 PSQ 评分 agent，DistilBERT 微调模型，10 维文本心理安全评分），通过 ZMQ 事件驱动同步组成多智能体网格，配对抗性评估器以 7 级程序集裁决分歧。提供 /doc /hunt /cycle /knock /sync /iterate 六个技能、SQLite 状态层（28 张表）、SPSS 数据读取与 HTTP API。README 声明为 Alpha 软件，默认启用 dangerouslySkipPermissions 并自主运行，需自备 Anthropic API key 或 Claude 订阅；Python 3.10+，核心脚本仅用标准库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 五对等 agent 网格 + 7 级程序对抗评估器裁决分歧
- PSQ 评分：DistilBERT v37 微调模型，10 维文本心理安全评分（held-out r=0.639）
- 读取 SPSS .sav/.zsav/.por 文件并做统计分析与解释
- SQLite 状态层（v32，28 张表）索引消息、决策、声明与认识论标记

## 适用场景

- 与心理学导师 agent 进行苏格拉底式咨询与研究讨论
- 对文本做 10 维心理安全（PSQ）评分
- 用 /knock 追踪决策的 10 阶连锁效应
- 读取 SPSS 调查数据并生成心理学解释

## 场景标签

`多智能体` `数据分析` `科研工具` · 领域:Agent 开发

## 证据(README 行号)

> L3: A collegial mentor for psychological analysis, research, and applied consultation —
> L166: The Psychological Safety Quotient (PSQ) scores text across 10 dimensions using
> L253: |`safety-quotient/`|PSQ agent — DistilBERT v37, held-out r=0.639, 10-dim text-level safety scoring. Sonnet-only la

## 星数曲线

```mermaid
xychart-beta
    title "safety-quotient-lab/psychology-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `908a0a6a24a7` · [字段定义](../../DATASET.md)*
