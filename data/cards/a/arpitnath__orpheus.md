# arpitnath/orpheus

⭐ 27 · Go · Apache-2.0 · 推送 2026-02-04 · [GitHub](https://github.com/arpitnath/orpheus) · [官网](https://orpheus.run) · 个人维护

**面向 LLM Agent 的运行时：按队列深度自动扩缩容并持久化工作区**

用 Go/TypeScript 编写的 Agent Runtime，以 runc 轻量容器执行 agent 工作负载，用队列深度（而非 CPU 指标）驱动自动扩缩容，`/workspace` 在容器重启与 worker 回收后仍保留。每个部署的 agent 自动获得 MCP 端点供 LLM 发现调用，内置 SSE 流式输出、熔断器/退避/OOM 处理的生产级监督、Prometheus 指标，并自动管理 Ollama（macOS）与 vLLM（Linux/CUDA）模型服务器生命周期。支持 macOS（经 Lima VM）与 Ubuntu 22.04+ 生产部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 runc 的亚秒级容器启动，无需 Docker daemon
- 队列深度驱动扩缩容，面向 I/O 密集的 LLM agent 工作负载
- 持久化 /workspace，会话状态与缓存跨容器重启保留
- 每个 agent 自动生成 MCP 端点，内置 SSE 流式输出

## 适用场景

- 部署需要跨调用保持上下文的多步 LLM agent
- 让 LLM 通过 MCP 将部署的 agent 作为工具发现和调用
- 自托管基础设施上按待处理任务量扩缩 agent 工作负载

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L7: Orpheus is an Agent Runtime that solves the 'Silent Failure' of CPU autoscaling. It scales on queue depth, persists 
> L11: Built for agents that call LLMs, orchestrate multi-step workflows, and maintain context across invocations, Orpheus

## 星数曲线

```mermaid
xychart-beta
    title "arpitnath/orpheus 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-29 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `577726d54783` · [字段定义](../../DATASET.md)*
