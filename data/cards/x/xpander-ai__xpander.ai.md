# xpander-ai/xpander.ai

⭐ 868 · Jupyter Notebook · MIT · 推送 2025-11-11 · [GitHub](https://github.com/xpander-ai/xpander.ai) · [官网](https://app.xpander.ai) · 组织维护

**AI agent 的运行时与控制平面：构建、部署、管理 agent**

面向开发团队的平台：Workbench 用于跨框架（Agno、LangChain、PydanticAI、CrewAI 等）配置 agent 与工具，AgentOS 提供 VPC/Kubernetes 或云端的部署运行时，含状态化数据库、日志、密钥、CI/CD 与任务调度。部署分 Managed（serverless）与 Embedded（容器、代码可改）两种方式，agent 可经 Chat、Webhook、REST、SDK、A2A、MCP 调用。另含从 OpenAPI 生成 MCP 服务器的 Connector Hub 与 OCR、浏览器自动化等 AI 工具。开源部分为 Apache 2.0 的 SDK 运行时。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Managed（serverless）与 Embedded（容器）两种部署形态，可在自有 VPC/Kubernetes 运行
- agent 可经 Chat/Webhook/REST/SDK/A2A/MCP 六种方式调用
- 从 OpenAPI 规范生成 MCP 服务器，内置 2,000+ 工具库
- 每个 agent 附带状态化 DB、日志、密钥、可观测性与 CI/CD

## 适用场景

- 在自有基础设施上部署和管理多框架 AI agent
- 把现有 agent 通过 MCP 接入 Claude Desktop 或 Cursor
- 从 OpenAPI 规范生成 MCP 服务器供 agent 与 MCP 客户端复用

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L22: xpander.ai is the runtime and control plane to build, run, and ship reliable AI agents fast. Start in Chat to use y
> L30: 🏗️ AgentOS — Deploy agents of any framework on a production runtime in your VPC/Kubernetes or in xpander cloud; inc
> L99: 🧩 Works with any framework: Agno, LangChain, PydanticAI, CrewAI — or your own runtime.

## 星数曲线

```mermaid
xychart-beta
    title "xpander-ai/xpander.ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 867 --> 869
    line [868, 868]
```

2026-10-18 868 → 2026-10-29 868（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `75da8902b8c0` · [字段定义](../../DATASET.md)*
