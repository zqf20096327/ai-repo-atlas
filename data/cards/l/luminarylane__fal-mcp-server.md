# luminarylane/fal-mcp-server

⭐ 61 · Python · MIT · 推送 2026-05-04 · [GitHub](https://github.com/luminarylane/fal-mcp-server) · [官网](https://luminarylane.github.io/fal-mcp-server/) · 个人维护

**让 Claude 等 MCP 客户端调用 Fal.ai 生成图像/视频/音乐的 MCP 服务器**

基于 Model Context Protocol 的服务器，将 Fal.ai 平台的 600+ 模型以 18 个工具的形式暴露给 Claude Desktop 及其他 MCP 客户端，覆盖文生图、图生视频、风格迁移、背景移除、放大、音乐生成、定价与用量查询等。模型列表从 Fal.ai API 动态发现并带 TTL 缓存，长任务走队列接口并回报进度。提供 STDIO、HTTP/SSE 及双传输三种模式；安装途径包括 uvx 免安装运行、Docker（GHCR 官方镜像）、PyPI 与源码，另有 Claude Code 插件通道。运行需 Fal.ai API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 18 个工具覆盖图像生成/编辑、视频、音乐与用量查询
- 动态发现 Fal.ai 平台 600+ 模型，支持别名与完整模型 ID
- STDIO / HTTP/SSE / 双传输三种运行模式
- 提供 uvx、Docker、PyPI、源码与 Claude Code 插件五种安装方式

## 适用场景

- 在 Claude Desktop 中直接用自然语言生成图片、视频和音乐
- 为 MCP 客户端接入 Fal.ai 的模型能力
- 生成前查询模型定价与用量统计

## 场景标签

`图像生成` `视频生成` · 领域:内容生成

## 证据(README 行号)

> L12: A Model Context Protocol (MCP) server that enables Claude Desktop (and other MCP clients) to generate images, video
> L25: ### 🌐 Transport Modes (New!)
> L54: - 🔍 **list_models** - Discover 600+ available models with smart filtering

## 星数曲线

```mermaid
xychart-beta
    title "luminarylane/fal-mcp-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 60 --> 62
    line [61, 61]
```

2026-10-18 61 → 2026-10-25 61（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `548161a4114b` · [字段定义](../../DATASET.md)*
