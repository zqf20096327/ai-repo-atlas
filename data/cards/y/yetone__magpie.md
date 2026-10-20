# yetone/magpie

⭐ 16,932 · Go · MIT · 推送 2026-10-19 · [GitHub](https://github.com/yetone/magpie) · [官网](https://usemagpie.ai) · 个人维护 · 中文 README

**为多 agent 统一接入模型与账号的本地网关应用**

在多个 AI coding agent 与多个模型提供方之间做统一接入的本地应用：一个位于 127.0.0.1:3425 的本地网关读写各 agent 自身的配置文件，把模型选择、订阅账号、路由规则集中到一处。网关以 OpenAI Chat、OpenAI Responses、Anthropic Messages、Gemini 四种协议互通，含流式、工具调用与 reasoning。核心机制包括：按 agent 粒度改写配置（保持注释与格式）、配额耗尽时的多账号故障转移路由组、五种调度策略（smart/order/rotate/usage/pace）、基于 npm/Bun 的插件与网关中间件、用量与成本统计、局域网/远程共享。限多 agent 多 provider 用户使用；单一 agent 单一订阅的用户 README 明确表示不适用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 0.7 天,年发版 89,126 位贡献者
- 涨星:近 1 天 **+1,002**(自 20261016 起算)
- 平台:WINDOWS / MACOS / LINUX / ANDROID / WEB · 协议:MCP / OLLAMA

## 能力要点

- 本地网关翻译 OpenAI/Anthropic/Gemini 协议，含流式、工具调用与 reasoning
- 配额耗尽自动切换账号/模型，五种路由策略（smart/order/rotate/usage/pace）
- 原子改写各 agent 自身配置，保留注释与格式；Profiles 一键切换全套配置
- npm/Bun 插件体系与网关中间件（param-override、model-map、word-guard 等）

## 适用场景

- 在多个 coding agent 间统一切换模型与提供方
- 多个订阅账号之间做配额故障转移与轮换
- 给不能联网搜索的模型统一挂上网络搜索能力
- 在服务器/NAS 上以 Docker 部署共享网关给局域网设备

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L8: Switch any of them from the menu bar. One local gateway serves them all,
> L73: The gateway at `127.0.0.1:3425` speaks OpenAI Chat, OpenAI Responses, Anthropic Messages and Gemini, and translates
> L91: > **Presets include** Anthropic · OpenAI · Google Gemini · Google Vertex AI · Amazon Bedrock (runtime and Mantle) ·

## 星数曲线

```mermaid
xychart-beta
    title "yetone/magpie 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-20"]
    y-axis "stars" 14687 --> 17136
    line [14891, 16932, 16932]
```

2026-10-18 14,891 → 2026-10-20 16,932（+2,041）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `b97e1bd077f3` · [字段定义](../../DATASET.md)*
