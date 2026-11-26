# respanai/respan-gateway

⭐ 1,061 · Rust · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/respanai/respan-gateway) · [官网](https://respan.ai/ai-gateway) · 组织维护

**Rust 开源 LLM 网关：一个端点接入各厂商 API**

用 Rust 编写的开源 AI 网关，作为用户代码与各 AI API 之间的单一适配层：支持聊天、实时语音、图像、视频、语音、嵌入与工具调用，内置回退重试、对冲请求、服务端工具循环（MCP）、插件机制与 Web UI 观测（记录每次调用的成本、延迟、token）。通过 PyPI、Cargo、安装脚本、Docker 及预编译二进制分发，支持 macOS/Linux/Windows。提供 Respan 托管网关服务，统一 key 访问托管模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 31 个内置模型供应商，外加任意 OpenAI 兼容端点
- 服务端工具循环：将 MCP 服务器与内置工具暴露给任意模型
- 内置回退、重试与对冲请求，可选 first/cheapest/fastest 等策略
- 插件机制：单个 trait 四个钩子，附 guardrails、PII 掩码等示例

## 适用场景

- 用现有 SDK（OpenAI/Anthropic/Gemini）调用其他厂商模型
- 为应用配置多供应商回退与故障转移
- 集中记录所有 AI 调用的成本、延迟与 token
- 通过 MCP 让任意模型使用服务端工具

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L21: **Respan Gateway** is an open-source AI gateway: a single Rust binary between
> L23: video, speech, embeddings and tools, from every major provider. Point the SDK
> L105: No config file needed: every provider whose key is set is ready. No provider

## 星数曲线

```mermaid
xychart-beta
    title "respanai/respan-gateway 星数(近 27 点)"
    x-axis ["2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26"]
    y-axis "stars" 76 --> 1150
    line [165, 217, 293, 342, 351, 368, 394, 408, 428, 468, 217, 625, 673, 749, 789, 812, 832, 856, 880, 909, 940, 954, 964, 979, 995, 1019, 1061]
```

2026-10-24 165 → 2026-11-26 1,061（+896）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 high · 依据 README sha `5ed2621382c3` · [字段定义](../../DATASET.md)*
