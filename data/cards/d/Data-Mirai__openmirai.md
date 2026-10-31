# Data-Mirai/openmirai

⭐ 15 · Rust · Apache-2.0 · 推送 2026-09-04 · [GitHub](https://github.com/Data-Mirai/openmirai) · [官网](https://datamirai.com) · 组织维护

**Rust 单二进制的 AI agent 工作流执行引擎**

用 Rust 编写的 agent 工作流引擎：以 YAML 图定义 agent，由单一二进制执行，声明零运行时依赖，可在笔记本、服务器、边缘设备运行。支持 7 个 LLM 提供商（Ollama 为默认，本地无需 API key）、52 个内置工具、MCP 协议，可通过 CLI、HTTP 或 Rust crate 嵌入。自述定位为 LangGraph/CrewAI/Google ADK 的替代，但刻意不包含 agent 实体、目标、长期记忆等上层能力。源码构建需 Rust 1.80+，也提供 Python SDK（pip 安装）。HTTP 服务默认只绑定回环地址，非回环启动需 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单二进制、零运行时依赖运行 YAML 定义的 agent 图
- 7 个 LLM 提供商，Ollama 为默认本地选项
- 52 个内置工具，覆盖 AI 调用、数据、文件系统、Git、MCP 等
- 支持条件分支、fan-out/fan-in、重试退避的图执行与 SSE 流式事件

## 适用场景

- 在自己的机器或边缘设备上运行 agent 工作流，不依赖云端
- 用 YAML 定义可版本化的 agent，通过 CLI/HTTP/Rust crate 嵌入应用
- 本地通过 Ollama 运行 LLM 驱动的工作流，无需 API key

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L10: OpenMirai is a Rust-native engine that runs agentic workflows defined as simple YAML graphs. No cloud lock-in, no h
> L27: - **Embeddable** — drop the engine into any app via CLI, HTTP, or as a Rust crate.

## 星数曲线

```mermaid
xychart-beta
    title "Data-Mirai/openmirai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `5614154470ba` · [字段定义](../../DATASET.md)*
