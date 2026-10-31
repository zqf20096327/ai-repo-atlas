# ApexPanda-Ai/apexpanda-release

⭐ 26 · Shell · 推送 2026-03-23 · [GitHub](https://github.com/ApexPanda-Ai/apexpanda-release) · [官网](https://www.apexpanda.ai/) · 组织维护 · 中文 README

**自托管多 Agent 平台：渠道接入、记忆、技能与工作流一体化**

ApexPanda 是一个自托管的多 Agent 协作平台，面向个人开发者与团队。通过飞书、钉钉、企微、Telegram、Slack、Discord、WhatsApp 等渠道与 Agent 对话；提供 80+ 内置 Skill、MCP 扩展、DAG 工作流编排、知识库 RAG（BM25+本地向量混合检索）、远程 Linux/Windows/Android 设备节点。长期记忆跨会话持久化并按 scope 隔离；过程记忆将成功脚本自动提炼为可复用技能并做信任分级。多 Agent 支持讨论与主从/流水线/并行协同。提供 Docker、docker-compose、预编译版与 Kubernetes 部署方式，需 Node.js>=22。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多渠道接入（飞书/钉钉/企微/Telegram/Slack/Discord/WhatsApp），群内 @ 路由多 Agent
- 长期记忆（scope 隔离、冲突检测、联想检索）与过程记忆（成功脚本自动提炼为技能、信任分级）
- 80+ 内置 Skill、MCP 扩展、DAG 工作流编排、混合检索知识库 RAG
- 远程 Linux/Windows/Android 设备节点（sysRun、uiTap、screenOcr 等）

## 适用场景

- 在飞书/钉钉/Telegram 等日常渠道内使用和编排多个 AI Agent
- 将成功执行的任务沉淀为可复用技能，重复任务直接复用
- 通过设备节点远程操控真实 Linux/Windows/Android 环境执行任务
- 团队内做 RBAC、审计与预算告警可控的 Agent 部署

## 场景标签

`Agent 记忆` `多智能体` `工作流自动化` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L13: 面向个人开发者与团队：一人一机即可部署，飞书/钉钉/Telegram 等日常渠道即用即连；团队协作可扩展至 RBAC、审计、多 Agent 协同。**长期记忆**实现跨会话持久化、自动提取与联想检索；**过程记忆**将成功执行的脚
> L38: - **Agent Runner**：消息 → 会话历史 → RAG 检索 → 长期记忆注入 → **过程记忆技能检索** → 系统提示词 → LLM → 工具循环（Skills/MCP/节点）→ 回复 → 记忆提取 flush、

## 星数曲线

```mermaid
xychart-beta
    title "ApexPanda-Ai/apexpanda-release 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-31 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `fc8eb84b5ce6` · [字段定义](../../DATASET.md)*
