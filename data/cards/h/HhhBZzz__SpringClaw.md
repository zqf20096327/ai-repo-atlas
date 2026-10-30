# HhhBZzz/SpringClaw

⭐ 17 · Java · MIT · 推送 2026-08-19 · [GitHub](https://github.com/HhhBZzz/SpringClaw) · [官网](https://spring-claw.vercel.app) · 个人维护 · 中文 README

**可视化 Java Agent 运行时：7 种范式可切换，执行全程可观测**

基于 Spring Boot 3.5 / Spring AI 1.1 / Vue 3 的自托管 Agent 运行时，同一引擎支持 ReAct、Plan-Execute、OPAR、Multi-Agent、Reflexion、Autonomous、Single-Turn 共 7 种范式并在运行时切换。前端 Blueprint Canvas 以节点图实时渲染真实执行轨迹（AgentTraceEvent over SSE），节点可 X-Ray 到具体 Java 类与行号；后端包含 10 层 harness（认证、路由、双轨记忆、模型故障转移、工具 AOP 治理、元守卫等）。多模型供应商接入（DeepSeek/Qwen/Claude），Docker Compose 全栈部署，按 2C2G 服务器调优。限制：需 Java 17 环境，依赖 MySQL/Redis/RabbitMQ 等组件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 同一引擎 7 种 Agent 范式，运行时一键切换
- Blueprint Canvas 实时可视化真实执行轨迹，节点 X-Ray 到 Java 代码行
- 10 层 harness：工具 AOP 治理、模型故障转移、双轨记忆（MySQL+Redis 向量）
- SKILL.md 技能目录与 REST/飞书渠道适配

## 适用场景

- 想理解或演示 Agent 内部执行过程的教学场景
- 自托管可治理的多范式 Agent 服务
- 在低配 VPS 上以 Docker 部署 Agent 平台并接入多家模型

## 场景标签

`Agent 框架` `多智能体` `LLM 可观测性` · 领域:Agent 开发

## 证据(README 行号)

> L28: SpringClaw is an agent runtime built to be **read — not just run**:
> L36: This isn't a chat wrapper or a notebook demo. It's a **production-grade agent platform** with 10 harness shells — f

## 星数曲线

```mermaid
xychart-beta
    title "HhhBZzz/SpringClaw 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-30 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `d0937cd03527` · [字段定义](../../DATASET.md)*
