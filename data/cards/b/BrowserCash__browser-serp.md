# BrowserCash/browser-serp

⭐ 27 · TypeScript · MIT · 推送 2026-03-09 · [GitHub](https://github.com/BrowserCash/browser-serp) · [官网](https://browser.cash/developers) · 组织维护

**给 AI Agent/RAG 的实时 Google 搜索 API，基于远程浏览器**

通过 Browser.cash 托管的远程浏览器执行 Google 搜索，把 SERP 结果解析为结构化 JSON 输出的 Node.js API 服务。面向 AI agent、RAG 管道与市场研究工具的开发者。核心机制包括浏览器会话池管理、连接池保持热启动、速率限制与 CORS 配置；支持按国家本地化与最多 20 条结果，需 Browser.cash API Key 才能运行。提供 Docker 部署方式。

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

- 远程浏览器执行 Google 搜索，输出结构化 JSON
- 浏览器会话池管理与并发请求处理
- 内置速率限制（默认每 IP 每分钟 100 次）
- 提供 Docker 与 Docker Compose 部署

## 适用场景

- 为 AI agent 或 RAG 管道提供实时搜索结果数据
- 获取结构化的 Google SERP 数据用于下游处理
- 搭建自托管的搜索 API 服务

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L34: **Browser SERP** is a lightweight, high-performance API that provides real-time Google Search results. It uses mana
> L36: Unlike traditional SERP APIs that can be slow or expensive, Browser SERP is optimized for speed and scalability, ma

## 星数曲线

```mermaid
xychart-beta
    title "BrowserCash/browser-serp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-28 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `f9c915582040` · [字段定义](../../DATASET.md)*
