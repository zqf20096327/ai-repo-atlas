# Nolpak14/agorio

⭐ 15 · TypeScript · MIT · 推送 2026-05-27 · [GitHub](https://github.com/Nolpak14/agorio) · [官网](https://agorio.dev) · 个人维护

**构建 UCP/ACP 电商购物 Agent 的 TypeScript SDK 工具包**

面向开发者的 AI 电商 Agent 工具包：基于 UCP（Google/Shopify）与 ACP（OpenAI/Stripe）开放商务协议，提供 ShoppingAgent（plan-act-observe 循环、17 个内置购物工具）、UcpClient/AcpClient/McpClient 协议客户端、MockMerchant 等三种模拟商家服务器、插件系统与 npx CLI。LLM 适配器支持 Gemini/Claude/OpenAI/Ollama，Ollama 可完全本地离线运行。另有 B2B 采购编排（AgentChain）、治理插件与 Agorio Cloud 审计等能力。需 Node.js 20+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ShoppingAgent 含 17 个购物工具覆盖发现/浏览/下单全流程
- 内置 Gemini/Claude/OpenAI/Ollama 四种 LLM 适配器，Ollama 支持本地离线
- UCP/ACP/MCP 三种协议客户端与三类 Mock 商家测试服务器
- 插件系统、AgentChain 子代理编排与 CLI 脚手架

## 适用场景

- 快速搭建能完成真实购物流程的 AI Agent
- 对接 Shopify 等电商平台的商家适配器
- 用 Mock 商家在本地测试购物 Agent 的完整结账流程
- 构建带人工审批与 PO 跟踪的 B2B 采购代理

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L10: Agorio gives you everything you need to build AI agents that can discover merchants, browse products, and complete 
> L86: ### Agent SDK (`@agorio/sdk`)
> L98: **LLM Adapters** -- Provider-agnostic interface. Ships with Gemini, Claude, OpenAI, and Ollama adapters, all with f

## 星数曲线

```mermaid
xychart-beta
    title "Nolpak14/agorio 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `137cabafb1a5` · [字段定义](../../DATASET.md)*
