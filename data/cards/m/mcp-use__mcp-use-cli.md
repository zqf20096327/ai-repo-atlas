# mcp-use/mcp-use-cli

⭐ 52 · TypeScript · 推送 2026-10-21 · [GitHub](https://github.com/mcp-use/mcp-use-cli) · [官网](https://github.com/mcp-use/mcp-use/tree/main/libraries/typescript/packages/cli) · 组织维护

**MCP 客户端与开发服务器的预构建 CLI**

mcp-use monorepo 中 CLI 包的只读镜像仓库。提供预构建 CLI：mcp-use dev 启动开发服务器，提供 MCP 端点、视图热更新并挂载 Inspector；支持通过 @mcp-use/tunnel 的托管中继以 --tunnel 暴露服务；另含 MCP client 命令，可连接端点并列出工具。问题与 PR 需提交至 monorepo，本仓库不接受修改。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- mcp-use dev 启动开发服务器并提供 MCP 端点与 HMR
- client 命令可连接 MCP 端点并列出工具
- --tunnel 通过 @mcp-use/tunnel 托管中继暴露 dev/start 服务

## 适用场景

- 开发调试 MCP 服务端并热更新视图
- 通过 CLI 连接 MCP 端点查看可用工具
- 将本地 dev/start 服务经隧道对外暴露

## 场景标签

 · 领域:LLM 基础设施/MCP 工具链

## 证据(README 行号)

> L11: Prebuilt CLI, development server, build pipeline, and MCP client for
> L12: mcp-use.
> L29: `mcp-use dev` serves the MCP endpoint, watches views for HMR, and mounts the

## 星数曲线

```mermaid
xychart-beta
    title "mcp-use/mcp-use-cli 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 51 --> 53
    line [52, 52]
```

2026-10-18 52 → 2026-10-24 52（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `cafa5aa01c32` · [字段定义](../../DATASET.md)*
