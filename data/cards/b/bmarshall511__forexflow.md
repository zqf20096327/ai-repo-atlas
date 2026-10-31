# bmarshall511/forexflow

⭐ 14 · TypeScript · AGPL-3.0 · 推送 2026-05-16 · [GitHub](https://github.com/bmarshall511/forexflow) · [官网](https://bmarshall511.github.io/forexflow/) · 个人维护

**自托管外汇交易平台：实时 OANDA 接入、AI 交易分析与自动交易**

基于 Next.js 15/TypeScript 的自托管外汇交易平台，连接用户 OANDA 经纪账户，提供实时 WebSocket 行情面板、持仓管理、TradingView 告警自动执行（经 Cloudflare Worker 中转、9 项安全检查）、供需区自动检测下单。AI 功能需 Anthropic API key：Claude Haiku/Sonnet 三级流水线做自主交易扫描、逐笔交易结构化分析、可执行条件与周/月绩效摘要，另含 MCP Server 供 Claude Code 查询运行中系统。macOS 提供 DMG 桌面端，支持 PWA 与 Cloudflare 隧道远程访问。声明仅供教育/个人用途，非投资建议。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- TradingView 告警经 9 项安全检查自动下单（熔断/白名单/冷却等）
- 三级 AI 流水线：14 项技术扫描 + Claude Haiku 快筛 + Claude Sonnet 深度决策，支持全自动模式
- 供需区多时间框架检测与 7 项 Odds Enhancers 评分
- Claude 逐笔交易分析与可一键激活的执行条件规则

## 适用场景

- 连接自己的 OANDA 账户做实时持仓与风控管理
- 用 TradingView 告警触发带安全检查的自动交易
- 让 AI 扫描候选交易并按手动/半自动/全自动模式执行

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L3: **A self-hosted, real-time forex trading platform built with AI — as both development tool and runtime feature.**
> L16: ForexFlow is a self-hosted forex trading platform that connects to your OANDA broker account and gives you a real-t
> L23: 2. **AI as a runtime feature** — Claude analyzes trades with rich context, suggests executable conditions, and gene

## 星数曲线

```mermaid
xychart-beta
    title "bmarshall511/forexflow 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `33c3cd72a837` · [字段定义](../../DATASET.md)*
