# antgroup/ai-vision

⭐ 5 · Python · Apache-2.0 · 推送 2026-11-23 · [GitHub](https://github.com/antgroup/ai-vision) · [官网](https://antgroup.github.io/ai-vision/) · 组织维护 · 中文 README

**给 AI agent 提供自托管观测与诊断的平台**

Ant AI Vision 是蚂蚁集团可观测团队与 OceanBase 联合开发的开源自托管 agent 观测与诊断平台。基于 OpenTelemetry 追踪 agent 会话、模型用量、工具调用、记忆检索与路由决策，支持按 ID 查询、调用树下钻、token 用量与成本估算、双运行对比；内置规则检查与调度诊断，可在质量板中回溯 BadCase 到具体步骤。个人部署为 All-in-One 单容器（内嵌 seekdb），团队部署用 Docker 或 Kubernetes 搭配 OceanBase CE，兼容 Langfuse SDK。

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

- 基于 OpenTelemetry 追踪 agent 会话、模型用量与记忆
- 兼容 Langfuse SDK 接入既有埋点数据
- 规则检查可调度执行，LLM 诊断与 Python 沙箱检查可选
- All-in-One 单容器运行平台与内嵌 seekdb，支持 Linux x86-64/ARM64

## 适用场景

- 排查 agent 运行为何变慢、哪次调用拖慢了流程
- 对比两次运行的 trace 找出重试与 token 增长原因
- 定时执行规则检查，跟踪修复是否复发
- 为已有 agent 应用（如编码 agent）安装采集插件观测日常任务

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L5:  Ant AI Vision is an open-source, self-hosted platform for agent observability and diagnostics.
> L30: - **Building your own?** Reuse supported instrumentation or follow the integration examples for LangGraph, Deep Age
> L96: **Already instrumented with Langfuse?** Reuse a supported SDK and send new traces to Ant AI Vision. See the integra


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `c04b6152ad05` · [字段定义](../../DATASET.md)*
