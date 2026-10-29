# brianirish/laravel-mcp-companion

⭐ 38 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/brianirish/laravel-mcp-companion) · 个人维护

**面向 Laravel 生态的 MCP 文档服务器：为 AI 助手聚合 Laravel 文档**

一个 MCP 服务器，聚合并组织 Laravel 生态文档供 AI 助手查询：覆盖 6.x 至最新版核心文档、Forge/Vapor/Envoyer/Nova 服务文档（117+ 小节）、Spatie/Livewire/Inertia/Filament 等社区包文档（42,000+ 行），提供学习路径、难度分级、15 个语义分类、统一搜索与包推荐。以 Docker 镜像为主要分发方式（文档随镜像发布，docker pull 更新），也支持源码运行。支持 stdio 与 HTTP 传输，HTTP 模式提供 JWKS 令牌认证、CORS/Host 校验、限流与 /healthz、/metrics 端点。README 标注为 Beta 阶段。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 聚合 Laravel 6.x 至最新版核心文档及 Forge/Vapor/Envoyer/Nova 服务文档
- 社区包文档 42,000+ 行，含 22 个精选包安装指南与跨包兼容性说明
- 文档随镜像发布，支持 docker pull、--update-docs 与 volume 三种更新方式
- HTTP 模式提供 JWKS bearer 认证、CORS/Host 校验、限流与 Prometheus /metrics

## 适用场景

- 在 Claude Desktop/Code 等 MCP 客户端中查询 Laravel 多版本文档
- 按主题和难度系统学习 Laravel 生态
- 查找适合当前项目的 Laravel 包及其组合兼容性

## 场景标签

 · 领域:Web 开发/文档服务

## 证据(README 行号)

> L15: **Laravel MCP Companion** is a documentation aggregator and navigator for the Laravel ecosystem. It centralizes and
> L36: - **Multi-version Laravel documentation** (6.x through latest) with enhanced search

## 星数曲线

```mermaid
xychart-beta
    title "brianirish/laravel-mcp-companion 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-29 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `a7984bc67fd0` · [字段定义](../../DATASET.md)*
