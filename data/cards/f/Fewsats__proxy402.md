# Fewsats/proxy402

⭐ 26 · Go · 推送 2026-02-18 · [GitHub](https://github.com/Fewsats/proxy402) · [官网](https://proxy402.com) · 组织维护

**给 API 加 x402 付费墙的代理：访问前需在 Base 支付**

Proxy402 是一个自托管代理服务，用于将任意 HTTP 端点变为按次付费的 API：用户在 Base（Sepolia 或主网）上通过 x402 协议以 USDC 支付后才能访问目标 URL，同时兼具短链接功能。服务端通过 Docker Compose 部署，经 Web 界面或 REST API 配置目标 URL、价格与 HTTP 方法；转发请求时附带 Proxy402-Secret 头供目标服务校验。面向希望货币化自有 API 的开发者，主题标签标明面向 AI agent 场景。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 任意端点按 USDC 定价，访问前强制 x402 支付
- Docker Compose 一键部署自托管服务
- Web 界面或 REST API 创建付费路由（含短码）
- 转发请求附带 Proxy402-Secret 头供目标服务验证

## 适用场景

- 把自己的 API 按次收费，无需自建计费系统
- 为 AI agent 提供按调用付费的 API 接入点
- 通过短码形式分发付费链接

## 场景标签

 · 领域:API 基础设施/加密支付

## 证据(README 行号)

> L3: Proxy402 lets you monetize APIs by requiring x402 payments on Base before accessing your endpoints.
> L79: 2. Server returns 402 with x402 payment token

## 星数曲线

```mermaid
xychart-beta
    title "Fewsats/proxy402 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-28 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `a8e7a9a958a8` · [字段定义](../../DATASET.md)*
