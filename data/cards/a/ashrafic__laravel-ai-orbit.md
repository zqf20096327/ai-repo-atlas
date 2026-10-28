# ashrafic/laravel-ai-orbit

⭐ 37 · PHP · MIT · 推送 2026-10-01 · [GitHub](https://github.com/ashrafic/laravel-ai-orbit) · [官网](https://ashrafic.github.io/laravel-ai-orbit/) · 个人维护

**Laravel AI SDK 的可观测性面板与开发者试验场**

面向官方 Laravel AI SDK（laravel/ai v1.0+）的独立观测面板与开发试验场：直接读取 SDK 的 agent_conversations / agent_conversation_messages 表并将一次性运行捕获到自有 orbit_ai_runs 表，提供会话/运行/追踪时间线视图、Agent 沙箱（实时覆盖系统提示词、模型、provider、温度等参数）、最多 3 个模型并排对比的 Prompt Lab、可编辑定价规则与预算告警、PII 扫描与数据保留策略、Pest/JSONL/CSV 导出。以 Composer 包安装（PHP 8.3+、Laravel 12+），无需前端构建步骤，默认仅 local 环境可访问。

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

- 读取 Laravel AI SDK 表并提供会话/运行/追踪时间线观测
- Agent 沙箱支持实时覆盖系统提示词、模型、provider 与采样参数
- Prompt Lab 并排对比最多 3 个 provider+模型组合并自动标注最快/最省
- PII 扫描、数据保留策略、预算告警与访问审计
- 一键导出 Pest 测试用例、OpenAI 微调 JSONL 与 CSV

## 适用场景

- 我在 Laravel 项目里调试和观测 AI agent 的会话与运行
- 并排对比多个模型的提示词效果与成本
- 对 AI 调用做成本核算、预算告警与 PII 合规扫描

## 场景标签

`LLM 可观测性` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L15: **Laravel AI Orbit** is a standalone observability dashboard and developer playground for the official Laravel AI S
> L88: ## Configuration
> L109: |`observability.enabled`|`true`|Listen to Laravel AI SDK events for run capture and budget monitoring|

## 星数曲线

```mermaid
xychart-beta
    title "ashrafic/laravel-ai-orbit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-28 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `4164e2c6fe38` · [字段定义](../../DATASET.md)*
