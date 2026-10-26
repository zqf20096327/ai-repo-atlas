# phughesmcr/deno-mcp-template

⭐ 33 · TypeScript · MIT · 推送 2026-04-12 · [GitHub](https://github.com/phughesmcr/deno-mcp-template) · [官网](https://jsr.io/@phughesmcr/deno-mcp-template) · 个人维护

**Deno 编写 MCP 服务器的全功能模板：一键生成多格式分发**

面向 TypeScript 开发者的 MCP 服务器项目模板：克隆后运行 setup 脚本替换占位符即可开始开发。内置 STDIO 与 Streamable HTTP 双传输、限流/CORS/bearer 认证等安全中间件、Deno KV 持久化状态、cron 定时任务、microVM 沙箱代码执行、实验性 MCP 任务工作流与 MCP Apps 交互式 UI。单一代码库可产出 JSR 包、原生二进制、DXT 扩展或 Deno Deploy 云端部署，并附 GitHub Actions CI/CD 工作流。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单代码库支持 STDIO/HTTP 双传输与五种分发格式（JSR/二进制/DXT/Deploy）
- 内置限流、CORS、bearer 认证、TLS、会话管理等安全中间件
- Deno KV 持久化状态与 KV 事件存储的会话恢复
- @deno/sandbox microVM 沙箱执行不受信代码

## 适用场景

- 快速搭建可投入生产的 MCP 服务器项目骨架
- 将 MCP 服务器打包为 DXT 扩展供 Claude Desktop 一键安装
- 在 Cursor、Claude Code 等 MCP 客户端中接入本地或远程服务器

## 场景标签

 · 领域:LLM 基础设施/开发者工具

## 证据(README 行号)

> L18: **The batteries-included starting point for building production MCP servers in TypeScript.**
> L20: Clone, run setup, start building. Ships with STDIO + HTTP transports, security middleware, persistent state, sandbo
> L29: - a local STDIO server for Cursor, Claude Desktop, or any MCP client

## 星数曲线

```mermaid
xychart-beta
    title "phughesmcr/deno-mcp-template 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-26 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `1ee238d4e659` · [字段定义](../../DATASET.md)*
