# datalayer/earthdata-mcp-server

⭐ 26 · Python · BSD-3-Clause · 推送 2026-10-10 · [GitHub](https://github.com/datalayer/earthdata-mcp-server) · [官网](https://datalayer.earth) · 组织维护

**面向 NASA Earthdata 的 MCP 服务器：为 AI 客户端提供数据检索工具**

基于 Model Context Protocol 的服务器实现，作为 reactor_mcp_server 扩展构建，可独立运行（stdio 或 streamable HTTP），或作为 opt-in earthdata 工具集挂载到任一 reactor MCP 宿主。提供 3 个工具：数据集搜索、数据粒度搜索（支持时间与边界框过滤）、以及 manifest/download/script 三种显式模式的数据下载，其中仅 download 模式需要 NASA Earthdata Login 凭据。另含海平面上升等工作流提示词。面向需要让 AI 客户端检索 NASA 地球数据的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 两种运行方式：独立运行或作为 reactor MCP 宿主的工具集
- 3 个 Earthdata 工具：数据集搜索、粒度搜索、三模式下载
- 仅 download 模式需凭据，manifest/script 模式匿名可用
- 可通过 mcp-compose 与 jupyter-mcp-server 组合使用

## 适用场景

- 让 Claude 等 MCP 客户端检索 NASA 地球观测数据
- 在 notebook 环境中通过 script 模式执行数据下载
- 按时间范围和地理边界框查找数据集与数据粒度

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L10: Earthdata MCP Server is a Model Context Protocol (MCP) server implementation that provides tools to interact with N
> L15: - **As a toolset**: installed beside any `reactor_mcp_server` host, it is discovered and served as the opt-in `eart

## 星数曲线

```mermaid
xychart-beta
    title "datalayer/earthdata-mcp-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-29 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `96eb63b8a6c9` · [字段定义](../../DATASET.md)*
