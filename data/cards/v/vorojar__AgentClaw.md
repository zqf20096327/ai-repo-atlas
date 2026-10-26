# vorojar/AgentClaw

⭐ 34 · TypeScript · 推送 2026-09-27 · [GitHub](https://github.com/vorojar/AgentClaw) · [官网](https://weread.qq.com/book-detail?type=1&senderVid=7701559&v=fff327a0813abb7d8g019f2a) · 个人维护 · 中文 README

**个人 AI 助理 + Agent 托管平台，多渠道接入、工具与记忆调度**

AgentClaw 是一个指挥官级别的个人 AI 助理，同时提供 Hive 模式的 Agent-as-a-Service 托管平台：用户可创建、配置、发布独立 Agent 并获得 API 端点，每个 Agent 拥有独立记忆、工具白名单、知识库（RAG）与 API Key。本体不直接执行搜索或编程，而是理解意图、规划任务、调度约 25 种工具与 12 个内置技能，支持子代理编排、Agent Handoff、任务管理、长期记忆与多层上下文压缩。接入渠道覆盖 Web UI、Telegram、WhatsApp、QQ、钉钉、飞书与企业微信。技术栈为 TypeScript monorepo，存储用 SQLite，桌面端基于 Tauri v2 提供 Windows/macOS/Linux 安装包，另有一键脚本、Docker 与手动部署方式。需至少配置一个 LLM API Key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Hive 模式创建独立 Agent，每个 Agent 有隔离记忆、工具白名单、RAG 知识库与独立 API 端点
- 7 种消息渠道接入：Web UI、Telegram、WhatsApp、QQ、钉钉、飞书、企业微信
- 子代理编排、Agent Handoff、任务生命周期管理与模型 Failover 错误分类
- 多层上下文压缩流水线（README 声明 80-95% token 节省）与安全纵深防御（Shell 沙箱、SSRF 防护、MCP 消毒）

## 适用场景

- 通过 Telegram/飞书/钉钉等 IM 全天候使用个人 AI 助理
- 创建并发布带独立 API 端点的定制 Agent 供外部系统调用
- 让 AI 代为处理文档、PDF、表格、日程等办公任务并长期记住偏好

## 场景标签

`AI 助手` `Agent 框架` `Agent 记忆` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L12: AgentClaw 是一个指挥官级别的个人 AI 助理，同时也是一个 **Agent 托管平台（Hive）**。它自己不写代码（调用编程技能），自己不搜索（调用搜索技能），但它理解你的意图、规划复杂任务、调度合适的工具和技能，并通
> L14: **Hive 模式**下，任何人都可以创建、配置、发布独立 Agent，获得即用的 API 端点——定义 Soul，选择 Tools，导入知识，拿到 Key，上线。每个 Agent 拥有独立的记忆空间、工具白名单、技能黑名单、知识
> L161: ### 多通道接入

## 星数曲线

```mermaid
xychart-beta
    title "vorojar/AgentClaw 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-26 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `b4dbc7856b37` · [字段定义](../../DATASET.md)*
