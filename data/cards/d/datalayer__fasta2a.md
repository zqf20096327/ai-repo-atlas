# datalayer/fasta2a

⭐ 222 · Python · MIT · 推送 2026-10-16 · [GitHub](https://github.com/datalayer/fasta2a) · 组织维护

**将任意 AI Agent 封装为 A2A 协议服务器的 Python 库**

Python 实现的 A2A 协议框架，与具体 agent 框架无关：基于 Starlette 将 agent 暴露为 ASGI 应用，通过 Storage/Broker/Worker 三组件架构运行任务，Worker 可部署在独立进程或机器上。提供 InMemoryStorage 与 InMemoryBroker 默认实现，用户需实现 Worker 以接入自己的 agent 框架；附 Pydantic AI 集成（pydantic-ai extra），一行调用即可将 Pydantic AI Agent 转为 A2A 应用。支持 SSE 流式响应、URI 协商的扩展机制与输出媒体类型声明。仅依赖 starlette、pydantic 与 opentelemetry-api。

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

- 与 agent 框架无关的 A2A 协议实现，Worker 可独立于 Web 服务器部署
- Pydantic AI 集成：agent_to_a2a 一行转换（需 Pydantic AI 2）
- message/stream 以 SSE 流式返回状态与 artifact
- 通过 URI 协商的扩展机制与输出媒体类型声明

## 适用场景

- 把自己的 agent 框架封装成 A2A 服务器供其他 agent 调用
- 将 Pydantic AI Agent 快速暴露为 A2A 兼容服务
- 构建跨 agent 互操作的 A2A 协议基础设施

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L9: **FastA2A** is an agentic framework agnostic implementation of the A2A protocol in Python.
> L30: To use **FastA2A**, you need to bring the `Storage`, `Broker` and `Worker` components.

## 星数曲线

```mermaid
xychart-beta
    title "datalayer/fasta2a 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 221 --> 223
    line [222, 222]
```

2026-10-18 222 → 2026-10-23 222（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `7af3ae4e6d80` · [字段定义](../../DATASET.md)*
