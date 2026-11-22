# yyyy231209/ai-company-framework

⭐ 10 · JavaScript · MIT · 推送 2026-08-22 · [GitHub](https://github.com/yyyy231209/ai-company-framework) · 个人维护 · 中文 README

**给非开发者的一句话开AI公司多Agent编排框架**

以 DeepSeek Harness（DSH）插件包形式发布的 multi-agent 编排框架：用户说一句话，生成一个由写手、编辑、开发、QA、销售、客服等角色组成的 Agent 团队，覆盖澄清需求、模型盘点与分岗路由、团队组建、员工自写技能、派单、质检闭环到交付与定向返工。面向非开发者，支持飞书机器人遥控、按客户隔离的 SQLite 记忆、人工决策门（定价/退款/法务等需手机端批准）。限制：依赖 DSH Desktop 运行时，验证环境为 Windows，无 RAG 与向量数据库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一句话生成角色分工的 Agent 公司，/company 开关不影响日常对话
- 每员工一个飞书机器人 + 人工决策门推送到手机审批
- 按客户 id 隔离的 SQLite 记忆，跨群/私聊自动合并客户档案
- 15 个平面 Skills、7 个工作流模板、AgentTeams 运行时与网页活动面板

## 适用场景

- 一句话搭一个电商内容工作室，批量产出文案并质检交付
- 客服/销售团队用客户记忆与人工决策门接单
- 远程团队给每个员工配飞书机器人，手机上遥控指挥
- 代理/外包场景为每个客户一句话建隔离公司

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L13: A DeepSeek Harness `dsh.bundle` that turns **one sentence** into a **company of role-specialized agents** (writer, 
> L57: - **Ecommerce content studio** — research → copywriting → QA → rework → delivery, batched into one deliverable.
> L93: - Models/tools/sessions/Skills/Bundle runtime come from DeepSeek Harness; the rest is **implemented by this Bundle*

## 星数曲线

```mermaid
xychart-beta
    title "yyyy231209/ai-company-framework 星数(近 2 点)"
    x-axis ["2026-11-13", "2026-11-22"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-11-13 10 → 2026-11-22 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `6d4d9bdf5445` · [字段定义](../../DATASET.md)*
