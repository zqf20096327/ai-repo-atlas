# gravitee-io-labs/Gravitee-AI-Agent-Workshop

⭐ 16 · JavaScript · 推送 2026-10-28 · [GitHub](https://github.com/gravitee-io-labs/Gravitee-AI-Agent-Workshop) · [官网](https://playground.gravitee.io) · 组织维护

**Gravitee AI 管理平台实操教程：暴露、安全与治理 AI Agent/LLM/MCP**

以虚构酒店预订公司 ACME Hotels 为背景的动手实验教程，演示如何用 Gravitee Enterprise AI Agent Management 暴露、安全防护与治理 AI Agent、LLM 和 MCP 服务器。内容涵盖：将 REST API 经 MCP Entrypoint 转为 MCP 工具、LLM Proxy 策略链（语义缓存、令牌限流、提示防护栏、PII 过滤）、OAuth2/OIDC 认证与 OpenFGA 细粒度授权、实时 Agent Inspector。需申请 Gravitee Enterprise 许可证（可免费获取 2 周），通过 docker compose 一键启动全套环境，推荐本地安装 Ollama 运行 qwen3:0.6b 模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- docker compose 自动化部署全套环境（API、网关、授权服务、演示站点）
- 演示 MCP Entrypoint 将 REST API 转为 AI 可发现的工具
- LLM Proxy 策略链：语义缓存、令牌限流、提示防护栏
- AI Agent Inspector 实时可视化 Agent 请求流程

## 适用场景

- 学习企业级 AI Agent 网关架构与治理策略
- 体验 LLM 代理的限流、缓存与提示注入防护
- 了解 MCP 协议如何将 REST API 暴露给 AI Agent

## 场景标签

`教程课程` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L5: A hands-on workshop demonstrating how to build, secure, and govern AI agents using the **Gravitee Al Agent Managemen
> L64: ## What You'll Learn

## 星数曲线

```mermaid
xychart-beta
    title "gravitee-io-labs/Gravitee-AI-Agent-Workshop 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `a99e9fb1246c` · [字段定义](../../DATASET.md)*
