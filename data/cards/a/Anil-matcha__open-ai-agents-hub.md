# Anil-matcha/open-ai-agents-hub

⭐ 33 · JavaScript · 推送 2026-08-29 · [GitHub](https://github.com/Anil-matcha/open-ai-agents-hub) · [官网](https://muapi.ai/agents) · 个人维护

**自托管平台：单一界面构建、托管并对话各类 AI agent**

开源自托管平台，用于构建、浏览和对话 AI agent——含 LLM 对话 agent 与图像/视频/音频生成 agent。由 Next.js 16 前端（agent 库、React Flow 可视化构建器、聊天与主页）与 FastAPI 后端代理组成，后端将 agent CRUD、聊天、生成请求转发到用户配置的 provider（如 MuAPI），自带 API key，无固定厂商绑定。需分别启动前后端服务，README 声明为早期进行中的项目。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Agent 库：自有/模板/精选 agent 统一浏览
- 可视化 Agent 构建器（React Flow），自定义 prompt、技能与主页
- 媒体生成 agent：回复可为图像、视频或音频
- 后端为 FastAPI 代理，自带 API key、可指向任意 provider

## 适用场景

- 搭建私有 agent 市场并与团队分享
- 在同一界面中运行客服聊天 agent 与图像生成 agent
- 不绑定单一厂商、自托管地运行 LLM 对话与媒体生成

## 场景标签

`聊天机器人` `图像生成` `视频生成` · 领域:对话与助手

## 证据(README 行号)

> L3: Open-source platform for building, browsing, and chatting with AI agents — both LLM chat agents and media generation
> L5: Instead of writing custom integration code for every model provider, Open AI Agents Hub gives you an agent library (
> L52: These all proxy through to a configurable base URL, so you can point the backend at whichever agent/model provider 

## 星数曲线

```mermaid
xychart-beta
    title "Anil-matcha/open-ai-agents-hub 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-28", "2026-10-31"]
    y-axis "stars" 30 --> 34
    line [31, 32, 33, 33]
```

2026-10-18 31 → 2026-10-31 33（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `266f48ff5713` · [字段定义](../../DATASET.md)*
