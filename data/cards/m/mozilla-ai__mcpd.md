# mozilla-ai/mcpd

⭐ 195 · Go · Apache-2.0 · 推送 2026-11-26 · [GitHub](https://github.com/mozilla-ai/mcpd) · [官网](https://docs.mozilla.ai/mcpd) · 组织维护

**AI Agent 开发者的 MCP 服务器声明式运行守护进程**

mcpd 是一个守护进程，通过 .mcpd.toml 声明式配置管理 MCP 服务器：将其作为 STDIO 子进程启动，并把工具代理为 HTTP 端点，覆盖生命周期管理、密钥注入与环境提升等基础设施工作。同一配置可在本地开发与容器化生产环境运行，附带 Python/JavaScript SDK、多语言插件 SDK，以及通过单一连接向 VS Code/Cursor 暴露所有受管服务器的 mcpd-proxy。以 Homebrew 二进制分发，从源码构建需 Go。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 声明式 .mcpd.toml 配置管理 MCP 服务器生命周期
- 将 STDIO 子进程服务器代理为统一 HTTP API
- 支持 uvx/npx/docker 三种包运行方式与密钥注入
- 提供 Python/JS SDK 与 Go/.NET/Python/Rust 插件 SDK

## 适用场景

- 让本地开发的 agent 在生产容器中用同一配置接入工具
- 通过 mcpd-proxy 在 VS Code/Cursor 中统一连接多个 MCP 服务器
- 为 CI/CD 流水线导出脱敏的服务器配置

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L9: `mcpd` is a daemon that manages your MCP servers via declarative configuration, exposing them as clean HTTP endpoint
> L83: Engineering teams build agents that work locally, then struggle to make them production-ready across environments. 
> L173: |Tools|mcpd|**(You are here)** Tool sandbox & router|

## 星数曲线

```mermaid
xychart-beta
    title "mozilla-ai/mcpd 星数(近 8 点)"
    x-axis ["2026-10-25", "2026-10-31", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-18", "2026-11-27"]
    y-axis "stars" 186 --> 196
    line [187, 188, 189, 187, 193, 194, 195, 195]
```

2026-10-25 187 → 2026-11-27 195（+8）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 mid · 依据 README sha `c5d32ffb3cca` · [字段定义](../../DATASET.md)*
