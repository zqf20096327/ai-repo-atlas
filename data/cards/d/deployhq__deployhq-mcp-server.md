# deployhq/deployhq-mcp-server

⭐ 13 · TypeScript · MIT · 推送 2026-07-22 · [GitHub](https://github.com/deployhq/deployhq-mcp-server) · [官网](https://deployhq.com/) · 组织维护

**让 Claude 等 AI 助手通过 MCP 操作 DeployHQ 部署的适配服务器**

DeployHQ 官方生态的 MCP 服务器：向 Claude Desktop、Claude Code 等 MCP 客户端暴露 18 个工具，覆盖项目/服务器/部署的查询、创建部署并读取部署日志，以及 SSH 密钥与账户级环境变量、配置文件模板的增删改。用 TypeScript + Zod 构建，以 npx 免安装运行，凭证通过环境变量传入且不落盘；支持 stdio 为主、SSE/HTTP 可选传输，并提供 DEPLOYHQ_READ_ONLY 只读模式阻断变更操作，要求 Node.js 18 及以上。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 18 个 DeployHQ API 工具：项目、服务器、部署、部署日志、SSH 密钥、全局环境变量与配置文件模板
- npx 免安装直接运行，凭证仅经环境变量传入
- stdio/SSE/HTTP 多传输方式，支持只读模式阻断所有变更操作
- TypeScript + Zod 参数校验与分级日志

## 适用场景

- 在 Claude Desktop/Code 中用自然语言查询部署状态与日志
- 让 AI 助手创建并跟踪生产部署
- 通过对话管理账户级环境变量与配置文件模板

## 场景标签

 · 领域:DevOps/AI 工具集成

## 证据(README 行号)

> L3: A Model Context Protocol (MCP) server for DeployHQ that enables AI assistants like Claude Desktop and Claude Code to
> L17: The MCP server provides **18 tools** for AI assistants:

## 星数曲线

```mermaid
xychart-beta
    title "deployhq/deployhq-mcp-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `05c92127f55e` · [字段定义](../../DATASET.md)*
