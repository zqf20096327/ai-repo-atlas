# mckinsey/agents-at-scale-marketplace

⭐ 19 · Python · NOASSERTION · 推送 2026-10-28 · [GitHub](https://github.com/mckinsey/agents-at-scale-marketplace) · [官网](https://mckinsey.github.io/agents-at-scale-marketplace/) · 组织维护

**面向 Ark 平台的 AI 服务 Helm 应用市场：一键部署代理相关服务**

麦肯锡（McKinsey）Agents at Scale 平台的组件市场，以 Helm Chart 与 DevSpace 配置打包执行器（claude-agent-sdk、LangChain）、基础设施服务（沙箱、观测、网关）、预置 Agent 与 MCP 服务器，通过 ark CLI、Helm 或 DevSpace 部署到任意 Kubernetes 集群。执行器实现 ark-sdk 的 BaseExecutor 并经 A2A 协议通信，MCP 服务器以 CRD 注册供 Agent 引用工具。面向在 Kubernetes 上运行代理工作负载的开发与运维人员。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 打包执行器、服务、Agent 与 MCP 服务器四类组件为 Helm Chart
- 支持 ark CLI / Helm / DevSpace 三种安装部署方式
- 执行器经 A2A 协议处理代理工作负载，MCP 服务器以 CRD 注册
- 包含 Langfuse、Phoenix 等观测服务与代码执行沙箱

## 适用场景

- 在 Kubernetes 集群上部署代理运行所需的服务组件
- 为 Agent 挂载文件系统、语音转录、Web 研究等 MCP 工具
- 为代理平台配套 LLM 观测与评估基础设施

## 场景标签

 · 领域:云原生/AI 基础设施

## 证据(README 行号)

> L17: > **Part of the Agents at Scale (Ark) Platform**
> L22: External execution engines that process agent workloads. Implement `BaseExecutor` from `ark-sdk` and communicate vi

## 星数曲线

```mermaid
xychart-beta
    title "mckinsey/agents-at-scale-marketplace 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `f426b2d6a0ab` · [字段定义](../../DATASET.md)*
