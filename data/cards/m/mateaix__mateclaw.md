# mateaix/mateclaw

⭐ 1,209 · Java · Apache-2.0 · 推送 2026-11-23 · [GitHub](https://github.com/mateaix/mateclaw) · [官网](https://claw.mate.vip) · 组织维护 · 中文 README

**企业可部署的多用户个人 AI 代理平台（第二大脑）**

基于 Spring Boot 与 AgentScope Java 构建的 self-hosted 多智能体平台：数字员工带角色/目标配置，支持原生 ReAct/Plan-and-Execute 运行时与外部 DSH 运行时双路径；内置 LLM Wiki 知识库（含引用溯源）、持久化记忆与 Dream 工作流、SKILL.md/MCP/ACP 三种扩展方式、审批门控与审计日志。提供 Web 控制台、Electron 桌面端（内置 JRE）、网页嵌入组件、8 个 IM 渠道接入与 Java 插件 SDK。主打多用户工作区与 IT 可管控部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 模型供应商故障时按优先级链自动切换（DashScope/OpenAI/Anthropic/Ollama 等）
- LLM Wiki 将文档消化为带 [[links]] 与可追溯引用的结构化页面
- 持久化 Goals：任务检查点存储，实例重启后从断点续跑
- 五种交付面：Web 控制台/桌面端/网页 Widget/IM 渠道/插件 SDK

## 适用场景

- 在企业内部署多用户 AI 员工并通过钉钉/飞书等渠道使用
- 上传文档构建带引用溯源的团队知识库
- 运行跨多次重启的长时任务并保留检查点
- 通过审批流与 RBAC 管控敏感工具调用

## 场景标签

`多智能体` `工作流自动化` `文档问答` · 领域:Agent 开发

## 证据(README 行号)

> L9:  Your second brain
> L31: > Multi-user workspaces. Approval-gated sensitive actions. Full audit trail. Spring Boot Actuator health monitoring
> L87: You hire coworkers, not chat boxes. Each one has a **Role**, a **Goal**, a **Backstory**, a runtime, a pixel-art av

## 星数曲线

```mermaid
xychart-beta
    title "mateaix/mateclaw 星数(近 20 点)"
    x-axis ["2026-10-23", "2026-10-28", "2026-10-29", "2026-10-30", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25"]
    y-axis "stars" 1167 --> 1212
    line [1170, 1172, 1173, 1174, 1175, 1176, 1170, 1187, 1190, 1192, 1194, 1196, 1199, 1200, 1203, 1204, 1206, 1207, 1208, 1209]
```

2026-10-23 1,170 → 2026-11-25 1,209（+39）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `78f7417d2630` · [字段定义](../../DATASET.md)*
