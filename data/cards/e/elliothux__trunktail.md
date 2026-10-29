# elliothux/trunktail

⭐ 21 · TypeScript · 推送 2026-02-03 · [GitHub](https://github.com/elliothux/trunktail) · [官网](https://trunktail.pages.dev/commands/) · 个人维护

**macOS 上管理 Apple Container 容器的桌面客户端**

面向 macOS 开发者的桌面应用，为 Apple Container CLI 提供图形界面，管理容器与镜像；仓库内附自动生成的 Container CLI 文档与一个 MCP server（packages/mcp-server），供 LLM 与自动化工作流集成。技术栈为 React 19 + Tauri + Rust/Swift 原生桥接，CLI/Server 部分用 TypeScript。需 macOS 及 Apple Container CLI，构建需 Node.js 18+ 或 Bun 1.0+，通过 bun install 与 bun run dev:tauri 启动；正式版从 Releases 页面下载。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 为 Apple Container 提供容器与镜像管理的桌面 UI
- 附 MCP server 供 LLM 与自动化集成
- 自动生成并持续更新的 Container CLI/API 文档
- Tauri + Rust/Swift 原生桥接的 macOS 应用

## 适用场景

- 在 macOS 上用图形界面管理 Apple Container 的容器与镜像
- 通过 MCP 让 LLM 或自动化工具接入容器管理
- 查阅 Apple Container 的 CLI 与 API 文档

## 场景标签

 · 领域:容器/DevOps 工具

## 证据(README 行号)

> L5: **A modern UI for Apple Container**, providing an intuitive desktop experience for managing containers and images.
> L22: - **Container MCP server** (MCP Server) — Model Context Protocol server for LLM and automation integration.
> L11: Compared to Docker, Apple Container delivers significantly better performance and lower resource usage on macOS, ma

## 星数曲线

```mermaid
xychart-beta
    title "elliothux/trunktail 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-29 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `c9881a0e0ae4` · [字段定义](../../DATASET.md)*
