# Husk-ai-lab/husk-ai

⭐ 14 · Python · NOASSERTION · 推送 2026-10-14 · [GitHub](https://github.com/Husk-ai-lab/husk-ai) · [官网](https://husk-ai.com/) · 组织维护

**本地可视化 AI agent 调试器：回放运行、定位失败原因**

面向正在构建 AI agent 的开发者的本地调试工具：通过一行代码接入（OpenTelemetry 兼容框架均可用），捕获并流式读取 agent 运行轨迹，在 Studio 仪表盘中以节点图和时间线展示每步由哪个模型处理、花费多少。失败运行可一键触发自动调试，用自然语言说明根因；支持从失败步骤编辑状态并重放，跳过上游 token 消耗。设计上仅限本机开发使用：trace 摄取、调试器与重放均限定 loopback，不能用于生产监控。Python 3.11+，BUSL 1.1 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一行代码接入 agent（OpenTelemetry 兼容框架均可用）
- 一键自动调试：自然语言说明失败根因与修改建议
- 从失败步骤编辑状态重放，跳过上游 token 消耗
- loopback-only 设计，仅限本机开发环境使用

## 适用场景

- 开发阶段调试 AI agent 的失败运行，定位出错步骤
- 多模型 agent 中查看各步骤由哪个模型处理及成本
- 修改某步状态后从该点重放，节省 token 花费

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L6:  A local, visual debugger for the agent you're building: what it did, what it cost, which
> L15: Husk is an interactive debugger you use **while building** an AI agent, before it goes to
> L38: - **One click debugs it for you.** When a run fails, click once and Husk reads the whole run

## 星数曲线

```mermaid
xychart-beta
    title "Husk-ai-lab/husk-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `f9beb71d684c` · [字段定义](../../DATASET.md)*
