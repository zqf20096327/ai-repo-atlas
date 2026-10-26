# mathaix/OpenClawMachines

⭐ 60 · Go · Apache-2.0 · 推送 2026-07-13 · [GitHub](https://github.com/mathaix/OpenClawMachines) · [官网](https://openclawmachines.com) · 组织维护

**自托管平台：在自有硬件的 Firecracker microVM 中运行多个隔离 OpenClaw agent**

面向企业/团队的 OpenClaw agent 运行基础设施：Go 控制平面（账户、机器、宿主机、调度、备份）编排多台 Linux 宿主机，每个 agent 运行在独立的 Firecracker microVM 中（KVM 硬件隔离）；Cloudflare 数据平面提供边缘认证与按机器子域名隧道；内置 LiteLLM 每宿主机 LLM 代理（BYO-key、跨 provider 用量统计），支持浏览器 VM、工作区级 MCP 集成与 OpenTelemetry/Opik 观测。要求 KVM 启用的 Linux 宿主机，不支持 macOS/Windows/WSL。Apache-2.0 公共核心，CLI 在独立仓库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每 agent 一个 Firecracker microVM，KVM 硬件级隔离
- Go 控制平面：账户/团队、宿主机注册、调度、备份、持久工作流
- 每宿主机 LiteLLM 代理：模型密钥集中管理、BYO-key、按机器用量统计
- 工作区级原生 MCP 集成（GitHub/Google Workspace/OpenAPI/GraphQL/远程 MCP）与浏览器 VM

## 适用场景

- 在一台裸金属服务器上运行大量硬件隔离的 AI agent
- 团队多用户共享自托管 agent 基础设施并统一管理模型密钥
- 为不可信或 agent 生成的代码提供安全沙箱
- 让 agent 通过浏览器 VM 与工作区 MCP 工具执行网页自动化与外部集成

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L9: OpenClaw Machines is an **open-source platform for running
> L11: own infrastructure**. A **control plane** orchestrates your hosts, and each
> L127: hardware-isolated via KVM) that runs one AI agent. The platform is the **control

## 星数曲线

```mermaid
xychart-beta
    title "mathaix/OpenClawMachines 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-26"]
    y-axis "stars" 58 --> 61
    line [59, 60, 60]
```

2026-10-18 59 → 2026-10-26 60（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `72c62fff12e2` · [字段定义](../../DATASET.md)*
