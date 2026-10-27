# harvard-cns/orla

⭐ 261 · Go · MIT · 推送 2026-10-25 · [GitHub](https://github.com/harvard-cns/orla) · [官网](https://orlaserver.github.io/) · 组织维护

**面向 agentic 工作流的运行时自适应执行层**

Go 编写的 LLM 调用执行层：开发者将 agent 指向 Orla 的 OpenAI 兼容端点，并为每次调用标注 stage（用途标签）。Orla 按各 stage 当前策略服务调用、记录执行结果，外部优化器读取记录并修订策略（如更换后端、先廉价模型失败再升级），以生产数据在成本与准确率上调优，无需改动 agent 代码。三参与方：agent（发出调用并评分）、Orla（执行层与共享记录）、优化器（修订策略）。由哈佛 SEAS Minlan Yu 实验室维护，提供 go install 安装与快速上手文档，可引用其 demo 论文。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenAI 兼容端点，stage 标签式调用路由
- 记录执行数据供外部优化器修订各 stage 策略
- 支持从后端替换到 cheap-first 逐级升级的策略形式
- agent 代码无需改动即可接入

## 适用场景

- 多 LLM 调用的 agentic 应用做按 stage 的策略调优
- 在生产数据上以成本/准确率为目标调整模型选择
- 统一记录与审计 agent 各阶段的 LLM 调用

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L8: Orla is a runtime-adaptive execution layer for agentic workflows. Modern agentic applications combine many LLM calls
> L10: You point your agent at Orla as an OpenAI-compatible endpoint and tag each call with a stage, what the call is for 

## 星数曲线

```mermaid
xychart-beta
    title "harvard-cns/orla 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-27"]
    y-axis "stars" 259 --> 262
    line [260, 261, 261]
```

2026-10-18 260 → 2026-10-27 261（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `74f9d56477fb` · [字段定义](../../DATASET.md)*
