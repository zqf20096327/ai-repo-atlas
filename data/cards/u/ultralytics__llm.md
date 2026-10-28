# ultralytics/llm

⭐ 120 · JavaScript · AGPL-3.0 · 推送 2026-10-06 · [GitHub](https://github.com/ultralytics/llm) · [官网](https://chatjs-ultralytics.vercel.app/examples/web/demo) · 组织维护

**面向 Web 应用的零依赖 JavaScript AI 聊天挂件**

Ultralytics LLM 提供一个原生 JavaScript（约 1700 行、零依赖）的浏览器聊天挂件，通过 jsDelivr CDN 以 script 标签接入网页，与后端 /api/chat SSE 流式接口对接。功能包括 SSE 流式响应与中断、搜索模式（POST /api/search）、会话管理、暗色模式、移动端适配（iOS/Android 安全区/返回键）、WCAG 无障碍、主题定制，以及可选的页面 DOM 内容抓取作为上下文。仓库同时含 Python 后端脚手架占位，计划开源 LLMClient、FastAPI 服务与 RAG 集成。采用 AGPL-3.0 与企业双许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 零依赖原生 JS（约 1700 行），jsDelivr CDN 一行接入
- SSE 流式响应、中断支持与会话管理（X-Session-ID）
- 可选页面上下文抓取（main 元素至多 5000 字符）
- WCAG 无障碍、移动端全面适配与暗色模式

## 适用场景

- 在我的网站里加一个可流式对话的 AI 聊天挂件
- 让 AI 回答感知用户当前浏览的页面内容
- 为文档站接入带搜索模式的聊天入口

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L5: **Ultralytics LLM** provides a lightweight, production-ready JavaScript chat client for integrating AI-powered conve
> L86:   apiUrl: "/api/chat", // Chat endpoint that streams SSE

## 星数曲线

```mermaid
xychart-beta
    title "ultralytics/llm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 119 --> 121
    line [120, 120]
```

2026-10-18 120 → 2026-10-28 120（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `1b587de40e06` · [字段定义](../../DATASET.md)*
