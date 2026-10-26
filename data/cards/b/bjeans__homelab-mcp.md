# bjeans/homelab-mcp

⭐ 43 · Python · MIT · 推送 2026-06-20 · [GitHub](https://github.com/bjeans/homelab-mcp) · 个人维护

**通过 Claude Desktop 管理家庭实验室基础设施的 MCP 服务器合集**

基于 FastMCP 框架的 Model Context Protocol 服务器集合，供 Claude Desktop 调用以管理和监控家庭实验室：统一服务器模式（单进程、工具命名空间化）或 7 个独立服务器（Ansible、Docker/Podman、Ollama、Pi-hole、Unifi、UPS、Ping），共 39 个带 MCP 注解的工具。支持 stdio/HTTP/SSE 三种传输方式；提供 Docker Hub 多平台预构建镜像（amd64/arm64）或原生 Python 安装（Python 3.10+）。含安全检查、git pre-push 钩子与项目说明模板。

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

- 7 个 MCP 服务器覆盖 Docker/Podman、Ollama、Pi-hole、Unifi、UPS、Ping、Ansible
- v3.0.0 基于 FastMCP，39 个工具带 MCP 注解，支持 stdio/HTTP/SSE 传输
- 统一服务器与独立服务器两种部署模式，Docker 与原生 Python 两种安装方式
- 安全文档与自动 pre-push 安全校验钩子

## 适用场景

- 在 Claude Desktop 中用对话监控和管理我的家庭实验室容器、DNS 与网络设备
- 远程部署 MCP 服务器并通过 HTTP/SSE 接入多个客户端
- 从 v1.x/v2.x 迁移到 v3.0 统一服务器模式

## 场景标签

 · 领域:基础设施管理/运维

## 证据(README 行号)

> L13: Model Context Protocol (MCP) servers for managing homelab infrastructure through Claude Desktop.
> L378: **Note:** The unified server includes 7 MCP servers: Ansible, Docker/Podman, Ollama, Pi-hole, Unifi, UPS, and Ping

## 星数曲线

```mermaid
xychart-beta
    title "bjeans/homelab-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-26 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `2681f41ec6b3` · [字段定义](../../DATASET.md)*
