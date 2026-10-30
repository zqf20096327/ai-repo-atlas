# giorgosn/openclaw-crm

⭐ 64 · TypeScript · MIT · 推送 2026-03-07 · [GitHub](https://github.com/giorgosn/openclaw-crm) · [官网](https://openclaw-crm.402box.io) · 个人维护

**自托管开源 CRM，原生支持 AI agent 与内置 AI 对话**

基于 Next.js 15 + PostgreSQL + Drizzle ORM 的开源自托管 CRM，提供联系人/公司、Kanban 商机管道、任务、笔记、自定义对象与 40+ REST API 端点（Bearer token 认证，附 /llms-api.txt 与 /openapi.json 机器可读文档）。AI 部分：可生成 SKILL.md 接入 OpenClaw Bot 由 agent 用自然语言管理 CRM；内置 AI 聊天代理经 OpenRouter 调用 Claude/GPT-4o/Llama/Gemini 等，含 8 个只读工具与 5 个需确认的写工具。通过 git clone + pnpm 或 Docker Compose 部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 40+ REST API 端点 + OpenClaw Bot SKILL.md 集成，agent 无需胶水代码即可操作 CRM
- 内置 AI 对话代理（OpenRouter 多模型，8 只读 + 5 写工具，写操作需确认）
- Typed EAV 数据模式支持 17 种属性类型与原生 SQL 过滤
- Docker Compose 开发/生产部署与 CSV 导入导出

## 适用场景

- 自托管管理客户、公司与商机数据，规避按席位收费
- 让 OpenClaw Bot 通过自然语言查询和更新 CRM 记录
- 直接与 CRM 数据对话完成检索、建单等操作

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L15: Most CRMs are closed-source, expensive, and impossible for AI agents to work with natively. OpenClaw CRM is differe
> L48: Talk to your CRM data in plain English. Powered by OpenRouter with support for Claude, GPT-4o, Llama, Gemini, and m

## 星数曲线

```mermaid
xychart-beta
    title "giorgosn/openclaw-crm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 63 --> 65
    line [64, 64]
```

2026-10-18 64 → 2026-10-30 64（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `7ca2b3e90a85` · [字段定义](../../DATASET.md)*
