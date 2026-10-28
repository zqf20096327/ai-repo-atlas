# itzam-ai/itzam

⭐ 60 · TypeScript · NOASSERTION · 推送 2026-07-27 · [GitHub](https://github.com/itzam-ai/itzam) · [官网](https://itz.am) · 组织维护

**开源 AI 集成平台：Dashboard 配置 Workflow，SDK 两行代码接入**

由 Dashboard 与 API/SDK 两部分组成：开发者在 Dashboard 中创建 Workflow，配置所用模型（GPT o3、Claude 3.7、Gemini 2.5）、模型设置、Prompt 与知识上下文，随后在应用中通过 API key 与 Workflow slug 调用 generateText 等接口生成输出。功能包括模型热切换、Prompt 管理与输出对比、成本用量统计、Playground 调试与知识管理；附件、规则、模型推荐、护栏为规划中功能。README 顶部声明项目处于开发暂停期，正寻求付费用户与投资。

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

- Dashboard 中以 Workflow 为单位配置模型、Prompt 与知识上下文
- 模型热切换：一键或自动更换当前模型
- 成本与用量统计、Playground 调试
- 计划功能：附件、规则（如超费自动换便宜模型）、模型推荐、护栏

## 适用场景

- 在落地页快速接入一个 AI 客服聊天
- 不改动代码即可切换底层模型或修改 Prompt
- 统一追踪多个 AI 功能的花费与用量

## 场景标签

`模型网关` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L10: Itzam is an open-source platform for integrating AI.
> L29: We are divided into 2 components: the Dashboard and the Integrations (API & SDKs).

## 星数曲线

```mermaid
xychart-beta
    title "itzam-ai/itzam 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 59 --> 61
    line [60, 60]
```

2026-10-18 60 → 2026-10-28 60（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `0b38c37c3b52` · [字段定义](../../DATASET.md)*
