# Yrobot/cloudflare-search

⭐ 43 · JavaScript · GPL-3.0 · 推送 2026-03-13 · [GitHub](https://github.com/Yrobot/cloudflare-search) · [官网](https://sink.proddig.com/cloudflare-search-github) · 个人维护 · 中文 README

**部署在 Cloudflare Workers 的聚合搜索 API，带 MCP 集成**

基于 Cloudflare Workers 的搜索 API 服务：并行请求 Google、Brave、DuckDuckGo、Bing 四个引擎并聚合结果，提供超时控制、单引擎故障隔离与 Token 认证，附带 Web 测试界面与 GET/POST API。原生支持 MCP 协议，可通过官方 npx 包 @yrobot/cf-search-mcp 接入 OpenClaw、Claude Code、Codex 等 AI 助手作为实时搜索工具。部署方式含一键部署按钮、Wrangler CLI 与 Dashboard 上传，Workers 免费额度支持每日 10 万次请求。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多引擎并行请求与结果聚合，单引擎故障不影响整体
- 原生 MCP 支持，npx 一键接入 OpenClaw / Claude Code / Codex
- TOKEN 环境变量认证与可配置超时
- 提供 Web 搜索界面与 GET/POST API

## 适用场景

- 为 Claude Code 等 AI 助手接入实时联网搜索工具
- 自建聚合搜索 API 供网站或应用调用
- 采集多引擎结果做对比分析

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L7: > Supports **MCP (Model Context Protocol)**, giving AI assistants (OpenClaw, Claude Code, Codex, OpenCode) real-time
> L14: - 🤖 **AI Enhanced (MCP)** - Native support for Model Context Protocol, one-click search tool integration for **Open

## 星数曲线

```mermaid
xychart-beta
    title "Yrobot/cloudflare-search 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-28 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `6b5f06303dca` · [字段定义](../../DATASET.md)*
