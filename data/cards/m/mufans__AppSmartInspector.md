# mufans/AppSmartInspector

⭐ 19 · Python · 推送 2026-06-04 · [GitHub](https://github.com/mufans/AppSmartInspector) · 个人维护 · 中文 README

**AI 驱动的移动端性能分析 CLI：自然语言采集 trace 并归因到源码**

面向移动端开发者的性能分析 CLI 工具：用中文自然语言描述性能问题，Orchestrator 通过 LLM 路由到对应 Agent，自动完成 Perfetto trace 采集、SQL 分析、SI$ tag 源码归因与 Markdown/JSON 报告生成。Android 平台已完整支持（Pine AOP 方法 Hook、11 个 Perfetto stdlib 模块、7 个可扩展分析维度），HarmonyOS/iOS 规划中。提供 MCP Server 将 23 个分析工具暴露给外部 AI Agent，支持 CI/Headless 非交互模式与自托管 Perfetto UI 框选帧分析。LLM 可选 DeepSeek/Claude/OpenAI，/quick 模式不调用 LLM。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言路由到采集/分析/归因/报告全量流水线
- SI$ 源码归因：Trace 热点经 Glob/Grep/Read 定位到源码位置
- MCP Server 暴露 23 个分析工具供 Claude Desktop/OpenClaw/Cursor 调用
- CI/Headless 模式输出 JSON 报告，可直接集成 CI/CD

## 适用场景

- 用中文描述卡顿/冷启动问题，自动采集并分析 Android 性能
- 把性能分析工具接入 Claude Desktop 等 AI Agent 工作流
- 在 CI 流水线中非交互运行性能分析并输出结构化报告
- 在 Perfetto UI 框选时间范围触发 AI 帧分析

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L3: AI 驱动的跨平台移动端性能分析 CLI 工具。通过自然语言交互，自动采集设备性能 trace，分析性能瓶颈，并将热点归因到源码。
> L109: **全量分析管线**：collector (Trace 采集 + SQL) → analyzer (LLM 性能解读) → attributor (SI$ → 源码归因) → reporter (Markdown / JSON 
> L393: |Agent 编排|LangGraph + LangChain|

## 星数曲线

```mermaid
xychart-beta
    title "mufans/AppSmartInspector 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-31"]
    y-axis "stars" 18 --> 21
    line [20, 19, 19]
```

2026-10-18 20 → 2026-10-31 19（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `643d5ba34526` · [字段定义](../../DATASET.md)*
