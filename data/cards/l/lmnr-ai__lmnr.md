# lmnr-ai/lmnr

⭐ 3,529 · TypeScript · Apache-2.0 · 推送 2026-11-27 · [GitHub](https://github.com/lmnr-ai/lmnr) · [官网](https://laminar.sh) · 组织维护

**面向 AI agent 的开源可观测性平台：追踪、评估、信号监控**

Laminar 是为 AI agent 构建的开源可观测性平台，核心能力包括一行代码自动追踪主流框架与 LLM 调用的 OpenTelemetry SDK、用自然语言描述并监控 agent 行为的 Signals（异常时推送 Slack）、可本地或 CI/CD 运行的评估 SDK/CLI 及结果可视化界面、自定义 SQL 仪表盘、数据标注与数据集管理。平台以 Rust 编写，含 20 倍 trace 压缩、全文检索与 gRPC 导出。提供官方托管平台，也可通过 docker compose 自托管，并支持 MCP/CLI 供编码 agent 查询与调试 trace。

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

- 一行代码自动追踪 Vercel AI SDK、LangChain、OpenAI、Anthropic、Gemini 等调用
- Signals 功能用自然语言描述 agent 行为并在发生时推送 Slack
- 评估 SDK/CLI 可在本地或 CI/CD 运行，附带结果对比 UI
- Rust 实现，20 倍 trace 压缩，实时 trace 查看与全文检索

## 适用场景

- 追踪并调试 agent 的 LLM 调用链路与 span 数据
- 在 CI/CD 流水线中对 agent 运行评估
- 用自然语言信号监控 agent 是否陷入循环等行为
- 自托管搭建团队级 LLM 可观测与数据标注平台

## 场景标签

`LLM 可观测性` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L10: Laminar is an open-source observability platform purpose-built for AI agents.
> L13:  - [x] OpenTelemetry-native powerful tracing SDK - 1 line of code to automatically trace **Vercel AI SDK, Browser U

## 星数曲线

```mermaid
xychart-beta
    title "lmnr-ai/lmnr 星数(近 26 点)"
    x-axis ["2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-27", "2026-11-28"]
    y-axis "stars" 3429 --> 3538
    line [3441, 3448, 3455, 3459, 3460, 3464, 3465, 3468, 3438, 3478, 3480, 3483, 3485, 3488, 3491, 3494, 3502, 3508, 3509, 3513, 3516, 3519, 3521, 3522, 3526, 3529]
```

2026-10-26 3,441 → 2026-11-28 3,529（+88）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `846cda5f15cc` · [字段定义](../../DATASET.md)*
