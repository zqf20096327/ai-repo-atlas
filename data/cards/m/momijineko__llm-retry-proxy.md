# momijineko/llm-retry-proxy

⭐ 22 · Python · MIT · 推送 2026-10-21 · [GitHub](https://github.com/momijineko/llm-retry-proxy) · 个人维护 · 中文 README

**LLM API 本地反向代理：上游过载/限流时自动重试与多 key 切换**

面向 LLM API 的本地反向代理转发工具，对客户端透明透传请求、响应与 SSE 流式。上游返回 503/429 等错误时按固定间隔、指数退避或 Retry-After 自动重试；支持多上游路由、号池多 key 故障转移、JSONL 日志与内置可视化面板，另含 Codex Responses 的 WebSocket↔SSE 桥接。适用讯飞 Coding Plan 用户及中转站/多 Key 用户，提供一键脚本、手动 pip 与 Docker Compose 三种部署方式。竞速模式未经人工测试，README 提醒慎用。

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

- 503/502/504/529/429 自动重试，支持固定间隔、指数退避与 Retry-After
- CSV 号池多 key 故障转移，遇 429/5xx 自动冷却切换并记录尝试
- SSE 流式透传，重试只发生在首字节之前
- Codex Responses 的 SSE2WS 双向桥接与 /settings 配置中心页面

## 适用场景

- Coding Plan 用户把 API 地址换成本地代理，上游过载时自动等待重试
- 中转站部署多 key 号池，请求失败自动切换到下一个可用 key
- 通过内置面板查看按天日志与 Token 用量统计

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L3: 一个面向 LLM API 的本地反向代理转发工具。它对客户端透明透传请求、响应和 SSE 流式响应，在上游临时过载或限流时自动重试；也支持多上游路由、号池故障转移、JSONL 日志和可视化分析。
> L9: 把本项目当作一个本地“自动重试层”：配置 `UPSTREAM_URL`（默认就是讯飞 Coding Plan 地址），启动代理后，只需将客户端的 API 地址从上游地址改为 `http://127.0.0.1:8080`，鉴权、请求

## 星数曲线

```mermaid
xychart-beta
    title "momijineko/llm-retry-proxy 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-27"]
    y-axis "stars" 21 --> 24
    line [23, 22, 22]
```

2026-10-18 23 → 2026-10-27 22（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `3f7e66dbbf7a` · [字段定义](../../DATASET.md)*
