# agentevals-dev/agentevals

⭐ 166 · Python · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/agentevals-dev/agentevals) · [官网](https://aevals.ai/) · 组织维护

**基于 OpenTelemetry 追踪的 AI agent 评测工具，无需重跑或专用 SDK**

面向开发者的 agent 评测方案：作为 OTLP 目标接收 agent 已产生的 OpenTelemetry GenAI 追踪，把 span 与日志事件解析为轮次、工具调用、token 与回答，再对照评测集打分，结果以 gen_ai.evaluation.result 事件回传管线。支持任意遵循 OTel GenAI 语义约定的框架（Google ADK、LangChain、OpenAI Agents SDK、Pydantic AI 等）。提供确定性轨迹/响应匹配、LLM 裁判、rubric 与任意语言自定义评测器；CLI 可离线运行并用于 CI 门禁，另有 Web UI、gRPC API、MCP server、Docker 与 Helm 部署。项目声明处于活跃开发期，可能有破坏性变更。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 读取已录制的遥测数据打分，无需重跑 agent、不消耗 token
- 框架无关：兼容 Google ADK、LangChain、OpenAI Agents SDK、Pydantic AI 等 OTel GenAI 生产者
- 确定性轨迹/响应匹配 + LLM 裁判 + rubric + 任意语言自定义评测器
- CLI（CI 门禁）、Web UI、gRPC API、MCP server、Docker、Helm 多种运行形态

## 适用场景

- 在 CI 中对 agent 追踪打分并用退出码拦截不达标版本
- 接入现有 OpenTelemetry/Collector 管线，对任意框架 agent 做评测
- 在 Web UI 中实时观察会话、工具调用并现场评测
- 通过 MCP server 让 Claude Code 等 assistant 客户端调用评测能力

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L22: agentevals scores AI agent behavior from the OpenTelemetry telemetry your agent already produces. It is an OTLP des
> L27: * **Gates and judges.** Tool trajectory and response matching for deterministic pass/fail, LLM judges and rubrics f

## 星数曲线

```mermaid
xychart-beta
    title "agentevals-dev/agentevals 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 163 --> 167
    line [164, 166, 166]
```

2026-10-18 164 → 2026-10-28 166（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `cd72c0693e3c` · [字段定义](../../DATASET.md)*
