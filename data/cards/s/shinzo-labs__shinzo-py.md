# shinzo-labs/shinzo-py

⭐ 13 · Python · MIT · 推送 2025-12-10 · [GitHub](https://github.com/shinzo-labs/shinzo-py) · [官网](https://shinzo.ai) · 组织维护

**Python MCP 服务器的 OpenTelemetry 可观测性 SDK**

面向 Python MCP 服务器开发者的插桩库：通过 instrument_server 调用即可对基于核心 MCP SDK 或 FastMCP 构建的服务器进行自动检测与插桩，采集请求时长、错误率等指标与分布式追踪，支持会话关联、PII 脱敏与自定义数据处理器。遥测数据默认导出到 Shinzo 平台的 OTLP 端点，也可对接任意 OpenTelemetry 兼容的接入服务，支持 bearer/apiKey/basic 三种认证方式。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自动检测并插桩 FastMCP 与 Traditional MCP 两种 SDK 的服务器
- 采集请求时长、错误率指标与分布式追踪，支持会话关联
- 内置 PII 脱敏（默认关闭，可开启或自定义脱敏器）
- 默认导出至 Shinzo OTLP 端点，可配置其他 OpenTelemetry 兼容服务

## 适用场景

- 给自己的 MCP 服务器加上追踪与指标采集
- 分析 agent 对工具的调用模式与服务器性能
- 将 MCP 服务器遥测接入任意 OpenTelemetry 后端

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L11:  The SDK provides OpenTelemetry-compatible instrumentation for Python MCP servers. Gain insight into agent usage pa
> L17: The Shinzo Python instrumentation library works with Python MCP servers built with the core MCP SDK or FastMCP. Sim

## 星数曲线

```mermaid
xychart-beta
    title "shinzo-labs/shinzo-py 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `e3754b7d7f27` · [字段定义](../../DATASET.md)*
