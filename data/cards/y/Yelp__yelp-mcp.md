# Yelp/yelp-mcp

⭐ 27 · Python · Apache-2.0 · 推送 2026-04-02 · [GitHub](https://github.com/Yelp/yelp-mcp) · [官网](https://business.yelp.com/data/products/fusion-ai/) · 组织维护

**将 Yelp 商户数据与对话能力接入 MCP 客户端的工具服务器**

Yelp 官方维护的 Model Context Protocol 服务器，暴露 yelp_agent 单一工具：接收自然语言查询（含经纬度、chat_id 多轮追问参数），返回商户搜索、比较、行程规划等自然语言与结构化数据，底层调用需 API key 的 Yelp Fusion AI 服务（含仅按需开放的餐厅预订）。面向使用 Claude、Cursor、VS Code 等 MCP 客户端的开发者。支持 stdio/streamable-http/sse 三种传输方式，可本地 uv 运行或构建 Docker 镜像。

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

- yelp_agent 工具支持自然语言商户查询、比较与行程规划
- 通过 chat_id 支持多轮追问
- 支持 stdio/streamable-http/sse 三种传输协议
- 提供 Docker 镜像构建方式

## 适用场景

- 在 MCP 客户端中用自然语言查询本地商户信息
- 构建需要商户数据（点评、营业信息等）的 agent 应用
- 通过对话方式完成商户比较与行程规划

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L14: This server exposes one primary tool:
> L61: This repository is designed to be run as a Model Context Protocol server. You will need an MCP client (like compati

## 星数曲线

```mermaid
xychart-beta
    title "Yelp/yelp-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-28 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `10cbd67ce50a` · [字段定义](../../DATASET.md)*
