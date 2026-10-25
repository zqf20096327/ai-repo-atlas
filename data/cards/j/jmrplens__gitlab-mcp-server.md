# jmrplens/gitlab-mcp-server

⭐ 45 · Go · MIT · 推送 2026-10-23 · [GitHub](https://github.com/jmrplens/gitlab-mcp-server) · [官网](https://docs.jmrp.io/gitlab-mcp-server/) · 个人维护

**把 1,103 个 GitLab API 操作接入 AI 助手的 MCP 服务器**

Go 编写的自包含单二进制 MCP 服务器，将 GitLab REST/GraphQL API 的最多 1,103 个操作以 2 个动态发现/执行工具暴露给 MCP 客户端（Claude、Cursor、VS Code、Codex 等），默认启动上下文 11,343 tokens。自动检测 GitLab 版本层级并调整能力目录，支持 stdio/HTTP 传输、OAuth、只读模式、安全模式与破坏性操作确认。面向在 AI 助手中操作 GitLab 的开发者与团队，提供 npm/PyPI/NuGet/brew/winget/Docker 多渠道安装与公共托管实例。

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

- 2 个工具覆盖最多 1,103 个 GitLab 操作，启动上下文 11,343 tokens
- 自动检测 GitLab 层级（Free 到 Ultimate），目录随层级调整
- 只读模式、安全模式（写操作预览）、按名称排除工具与破坏性操作确认
- stdio 与 HTTP 两种传输，产物带签名校验和、SBOM 与构建溯源

## 适用场景

- 让 Claude/Cursor/VS Code 里的 AI 助手代为审查 MR、排查流水线、管理 issue
- 在共享部署中通过 HTTP 模式为多用户隔离凭证
- 对自建 GitLab 实例通过自然语言执行 API 操作

## 场景标签

 · 领域:开发工具/AI 接入层

## 证据(README 行号)

> L23: **All of GitLab for your AI assistant.** Up to 1,103 actions over GitLab's REST and GraphQL APIs, from Free to Ulti
> L34: - **Three surfaces, two transports.** Two discovery tools by default, one tool per domain or one per action; stdio 

## 星数曲线

```mermaid
xychart-beta
    title "jmrplens/gitlab-mcp-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-25 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `093a670454c2` · [字段定义](../../DATASET.md)*
