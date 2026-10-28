# serverlessclaw/serverlessclaw

⭐ 21 · TypeScript · MIT · 推送 2026-10-27 · [GitHub](https://github.com/serverlessclaw/serverlessclaw) · 组织维护

**AWS 上的无服务器自主多智能体框架，闲置零成本**

基于 SST v4 部署到 AWS Lambda/DynamoDB/EventBridge 的自主 AI 智能体集群框架：SuperClaw 编排器接收指令，经 Strategic Planner 规划后通过 EventBridge 分发任务，采用异步 Pause & Resume 模式（智能体发任务后终止，结果回传时唤醒）。含 7 类专职智能体（编码、QA、评审 Council 等），支持自演进（智能体写代码、跑测试、重新部署）并经 Council 评审把关。面向 AWS 开发者，git clone + pnpm + make 部署；另提供付费托管版 ClawMore。

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

- Lambda 弹性伸缩，闲置成本 $0
- 异步 Pause & Resume 智能体运行模式
- Council-Verified 自演进循环：写代码→测试→重新部署
- 7 类专职智能体角色分工

## 适用场景

- 在 AWS 上低成本运行自主代码审查与改进智能体
- 基础设施监控与自动修复
- 大规模并行研究与数据分析任务

## 场景标签

`多智能体` `编码 Agent` `数据分析` · 领域:Agent 开发

## 证据(README 行号)

> L39: **ServerlessClaw** is the authoritative open-source autonomous agent framework that:
> L69: When you send a message, **SuperClaw** receives it, develops a plan with the **Strategic Planner**, and dispatches 

## 星数曲线

```mermaid
xychart-beta
    title "serverlessclaw/serverlessclaw 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-28"]
    y-axis "stars" 19 --> 22
    line [20, 21, 21]
```

2026-10-18 20 → 2026-10-28 21（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `c452075a5e1e` · [字段定义](../../DATASET.md)*
