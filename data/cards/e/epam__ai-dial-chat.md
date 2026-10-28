# epam/ai-dial-chat

⭐ 502 · TypeScript · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/epam/ai-dial-chat) · [官网](https://chat.dialx.ai) · 组织维护

**EPAM AI DIAL 平台的默认聊天前端（React + NestJS）**

Nx monorepo 全栈聊天应用：React 19 + Vite + Tailwind 前端、NestJS REST 后端（backend-for-frontend），后端统一管理认证、配置并代理对 DIAL Core 的上游调用。前端界面由 libs/ 下多个库（composer、message list、catalog、sidebar 等）组合而成，可通过 props 定制与替换；支持 iframe overlay 嵌入（postMessage 协议、@epam/ai-dial-chat-overlay）、主题定制与九种身份提供商（Auth0、Azure AD、Keycloak、Okta 等）。1.0 为重写版本，旧版聊天在 development-0.x 分支维护至 2026 年底且无原地升级路径。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- backend-for-frontend 架构：chat-api 统一认证与上游 DIAL Core 调用
- 界面由 libs/ 库组合，支持替换与主题定制
- iframe overlay 嵌入协议与 Overlay Sandbox 测试页
- 内置九种身份提供商模板（Auth0/Azure AD/Keycloak/Okta 等）

## 适用场景

- 为 AI DIAL 平台部署可定制的聊天界面
- 通过 iframe overlay 将聊天嵌入宿主页面
- 企业内基于现有 IdP 接入 AI 对话入口

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L3: A modern full-stack chat application built with Nx monorepo, featuring a React frontend and NestJS backend with DIAL
> L17: - **A backend-for-frontend.** The frontend no longer talks to DIAL Core
> L40: - **Integration**: EPAM AI DIAL Core connectivity

## 星数曲线

```mermaid
xychart-beta
    title "epam/ai-dial-chat 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-28"]
    y-axis "stars" 501 --> 506
    line [505, 502, 502]
```

2026-10-18 505 → 2026-10-28 502（-3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `eab9cc0d35e0` · [字段定义](../../DATASET.md)*
