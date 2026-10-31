# boydfd/claw-agent-dashboard

⭐ 27 · Python · MIT · 推送 2026-03-23 · [GitHub](https://github.com/boydfd/claw-agent-dashboard) · 个人维护 · 中文 README

**OpenClaw AI agent 的 Web 管理面板：监控、编辑、对话**

面向 OpenClaw 运维者的 Web 管理界面：浏览与编辑 agent 工作区文件（SOUL.md、技能、记忆等），查看带 provider/模型/工具调用信息的会话历史并直接向 agent 发消息或切换模型，实时监控 CPU/内存/磁盘与 Gateway 健康状态，提供工作区全文搜索与会话转录搜索（后者需 Elasticsearch）。后端 FastAPI 代理 OpenClaw Gateway，前端 Vue 3，以 Docker Compose 部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 工作区文件浏览器与 blueprint 同步（含 diff 审阅）
- 会话查看与直接发消息、切换运行中会话的模型
- CPU/内存/磁盘/Gateway 健康实时监控与文件变更检测
- 文件版本历史、全文搜索与中英双语界面

## 适用场景

- 不通过 SSH 集中管理多渠道 agent 的工作区与配置
- 实时查看 agent 会话流、模型用量与系统健康
- 直接在页面向 agent 发消息并切换模型

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L5: A web-based management dashboard for OpenClaw AI agents. Monitor system health, browse agent workspaces, manage sess
> L19: It's designed for OpenClaw operators who want visibility and control without SSH-ing into their server.
> L136: - **Backend**: FastAPI (Python) providing REST APIs, proxying to the OpenClaw Gateway for session and agent data

## 星数曲线

```mermaid
xychart-beta
    title "boydfd/claw-agent-dashboard 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-31 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `e7daef3b7e47` · [字段定义](../../DATASET.md)*
