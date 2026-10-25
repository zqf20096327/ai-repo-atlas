# zscaler/zscaler-mcp-server

⭐ 51 · Python · MIT · 推送 2026-10-12 · [GitHub](https://github.com/zscaler/zscaler-mcp-server) · [官网](https://pypi.org/project/zscaler-mcp/) · 组织维护

**连接 AI 代理与 Zscaler 零信任平台的 MCP 服务器**

由 Zscaler 官方维护的 Model Context Protocol 服务器，让 AI 代理（Claude Desktop、Cursor、GitHub Copilot 等）管理 Zscaler 多产品（ZPA/ZIA/ZDX/ZCC 等），暴露 402 个工具、按 63 个工具集分组加载。默认只读模式（110+ 个 list/get 工具），写操作需 --enable-write-tools 加 --write-tools 白名单双重开启；DELETE 操作走 MCP elicitation 人工确认或 HMAC 一次性令牌兜底。含输出净化、审计日志、OneAPI 权限过滤等多层安全机制。目前处于 Public Preview，官方提示勿用于生产。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 402 个工具覆盖 ZPA/ZIA/ZDX/ZCC 等 Zscaler 服务，63 个工具集按需加载
- 默认只读模式，写操作需双重开关与强制白名单
- DELETE 走人工确认（MCP elicitation 或 HMAC-SHA256 一次性令牌）
- 三段式输出净化防御资源描述中的提示注入

## 适用场景

- 让 Claude/Cursor 等 AI 助手查询和运维 Zscaler 零信任平台资源
- 以白名单方式授权 AI 代理执行特定的创建/更新/删除操作
- 通过 JMESPath query 控制工具返回字段以压缩上下文

## 场景标签

 · 领域:网络安全/零信任平台运维

## 证据(README 行号)

> L12: **zscaler-mcp-server** is a Model Context Protocol (MCP) server that connects AI agents with the Zscaler Zero Trust
> L37: > **Writing effective prompts**: This server exposes **402 tools** across multiple Zscaler services. Most MCP clien

## 星数曲线

```mermaid
xychart-beta
    title "zscaler/zscaler-mcp-server 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22", "2026-10-25"]
    y-axis "stars" 48 --> 52
    line [49, 50, 51, 51]
```

2026-10-18 49 → 2026-10-25 51（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `762bd7baf8a2` · [字段定义](../../DATASET.md)*
