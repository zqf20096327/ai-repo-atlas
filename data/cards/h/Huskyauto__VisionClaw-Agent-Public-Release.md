# Huskyauto/VisionClaw-Agent-Public-Release

⭐ 26 · TypeScript · MIT · 推送 2026-10-19 · [GitHub](https://github.com/Huskyauto/VisionClaw-Agent-Public-Release) · [官网](https://agenticcorporation.net) · 个人维护

**自托管多租户 AI agent 工作台：18 个 agent 协作产出交付物**

开源的多租户 AI agent 平台，18 个专职 agent 协作产出研究报告、法律文件、财务模型、营销方案、幻灯片等交付物；含 428 个注册工具、146 个活跃能力、86 个精选模型与 6 个 AI 提供商接入。最低运行条件为一个 LLM key 加 PostgreSQL，邮件/支付/语音/Drive 等集成为可选。面向代理机构、创业者与研究团队自托管（BYO-keys）。自主决策管线（多模型评审、CI 自愈器）默认关闭自动应用，需设 JURY_AUTOAPPLY=1 显式开启。代码约 32 万行 TypeScript。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 18 个专职 agent 协作产出文档/报告/模型等成品交付物
- BYO-keys 自托管，最低仅需一个 LLM key 与 PostgreSQL
- 自主管线（jury_triage 评审、CI 自愈器）默认 safe-by-default，不自动改码
- 428 注册工具、86 精选模型、887 平台索引，OpenRouter 每日目录同步

## 适用场景

- 代理机构给每个客户配置多 agent 运营团队
- 创业者用一套自托管系统替代多个 SaaS 订阅
- 研究团队作为多 agent 编排与工具治理的实验平台

## 场景标签

`多智能体` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L19: **An open-source, multi-tenant AI agent workspace — documents, research & workflows. Built for agencies, operators,
> L38: VisionClaw Agent is an open-source, multi-tenant AI platform where 18 specialized agents work together to produce r
> L44: **The app runs with just one LLM key and a Postgres database.** Everything else — email, payments, voice, Drive — i

## 星数曲线

```mermaid
xychart-beta
    title "Huskyauto/VisionClaw-Agent-Public-Release 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-29 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `78698bd4cc01` · [字段定义](../../DATASET.md)*
