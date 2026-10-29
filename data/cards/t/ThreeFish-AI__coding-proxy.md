# ThreeFish-AI/coding-proxy

⭐ 19 · Python · Apache-2.0 · 推送 2026-09-29 · [GitHub](https://github.com/ThreeFish-AI/coding-proxy) · [官网](https://threefish.site) · 组织维护 · 中文 README

**面向 Claude Code 的多厂商代理：自动故障切换与格式转换**

本地运行的透明代理服务，位于 Claude Code 等 Anthropic Messages API 客户端与上游之间：当主厂商触发限流、配额耗尽或过载时，按 N 级链式顺序自动切换到 GitHub Copilot、Google Antigravity、智谱 GLM、MiniMax、通义千问等备选厂商；每个节点带独立熔断器与配额守护。支持 Anthropic↔Gemini、Anthropic↔OpenAI 双向请求与 SSE 流式格式转换及模型名映射，内置 SQLite 监控与 CLI。客户端仅需改写 ANTHROPIC_BASE_URL。需 Python 3.12+ 与 uv。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- N 级链式故障切换，覆盖 Claude 官方计划及多家厂商 Coding Plan
- Anthropic↔Gemini、Anthropic↔OpenAI 双向请求/SSE 流式转换与模型名映射
- 每厂商节点独立熔断器与配额守护，CLI 可查看状态并强制重置
- 基于 FastAPI+httpx 的异步单机部署，不依赖 Redis/消息队列

## 适用场景

- 编码时遇到 429/403/503 自动切换备用模型厂商，不中断工作流
- 让 Claude Code 客户端使用智谱 GLM、Copilot 等其他厂商配额
- 通过 dashboard 与 usage 命令查看 token 消耗与延迟

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L5: **A High-Availability, Transparent, and Smart Multi-Vendor Proxy for Claude Code**
> L20: **coding-proxy** was forged in the developer fires to terminate these exact pain points. Serving as a **purely tran
> L27: - **🔄 Universal Alchemy (Formats & Models)**: Native support for two-way request/streaming (SSE) translations betwe

## 星数曲线

```mermaid
xychart-beta
    title "ThreeFish-AI/coding-proxy 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `25074e3c5b96` · [字段定义](../../DATASET.md)*
