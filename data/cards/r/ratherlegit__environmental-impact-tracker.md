# ratherlegit/environmental-impact-tracker

⭐ 16 · Python · MIT · 推送 2026-10-19 · [GitHub](https://github.com/ratherlegit/environmental-impact-tracker) · 个人维护

**Claude Code 技能：将 token 用量换算为能耗与水耗并出报告**

一个 Claude Code skill，通过 Stop hook 在每次响应后记录 token 计数，按各模型的固定开销+边际费率模型换算为能耗（Wh）与水耗（mL），写入共享日志，可生成周/月/季/年报告、逐响应展示与历史回填（从 Claude Code 会话转录重建）。费率来自公开基准与定价信号的估算，非 Anthropic 官方数据。安装为复制文件到 skills 目录，需 Python 3；自动追踪依赖 Claude Code 的 hooks 与会话转录。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Stop hook 后台记录每次响应（含子代理）的 token 并换算能耗/水耗
- 周/月/季/年报告，含环比、按项目分解与趋势图
- 从 Claude Code 会话转录回填历史用量
- 固定开销+边际费率的能耗模型，区分长上下文档位

## 适用场景

- 我想知道自己每周用 Claude 消耗了多少能源和水
- 对比不同项目或模型的能耗开销
- 在大型响应后即时看到本轮影响数据

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L5: A Claude Code skill that calculates and displays the environmental footprint of your AI interactions, translating ab
> L16: - **Tracks everything**: a Stop hook logs every response, subagents included, so nothing depends on Claude remember

## 星数曲线

```mermaid
xychart-beta
    title "ratherlegit/environmental-impact-tracker 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `4d9dca92a2de` · [字段定义](../../DATASET.md)*
