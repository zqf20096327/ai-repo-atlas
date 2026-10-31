# skillberry-ai/skillberry-store

⭐ 16 · Python · Apache-2.0 · 推送 2026-10-04 · [GitHub](https://github.com/skillberry-ai/skillberry-store) · [官网](https://skillberry-ai.github.io/skillberry-store/) · 组织维护

**面向 agent 工作流的技能/工具仓库服务：管理、执行与分发**

Skillberry Store（SBS）是一个管理 agent 技能、工具与代码片段的服务：提供增删改查、生命周期管理、语义与经典搜索、基于 Docker 沙箱的工具执行，以及文件系统/GitHub 持久化。接入方式包括 FastAPI 的 OpenAPI 接口、CLI（单文件原生可执行）、React Web UI、虚拟 MCP 服务器（VMCP）、可挂载的 WebDAV/NFSv3 虚拟文件系统（vNFS），以及通过 /.well-known/agent-skills 约定让 Claude Code、Cursor、Codex 等约 70 种 agent 一条 npx 命令安装技能。工具执行依赖 Docker 或 Podman。支持插件架构与多 MCP 后端路由。

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

- Docker 沙箱执行工具，含参数调用与生命周期管理
- 虚拟 MCP 服务器（VMCP）与 WebDAV/NFSv3 可挂载文件系统（vNFS）两种暴露方式
- npx skills add 一条命令将技能安装进约 70 种 agent（Claude Code/Cursor/Codex 等）
- 提供 Web UI、OpenAPI、CLI、Python SDK 多种交互通道，含指标与追踪观测

## 适用场景

- 集中管理团队的 agent 技能、工具与代码片段并做语义搜索
- 把技能子集作为 MCP 服务器或网络文件系统暴露给 agent 与其他工具
- 让 Claude Code/Cursor 等 agent 一条命令安装存储中的技能

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L12: This service implements a smart skills repository for agentic workflows. Manage, execute, and organize your skills,
> L49: - **MCP frontend**: Expose virtual MCP servers for any subset of the tools or all of them.
> L52: - **Support Multiple MCP backends**: Consume and route additional tools from multiple backend MCP servers.

## 星数曲线

```mermaid
xychart-beta
    title "skillberry-ai/skillberry-store 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `6831eee85008` · [字段定义](../../DATASET.md)*
