# smart-mcp-proxy/mcpproxy-go

⭐ 398 · Go · MIT · 推送 2026-10-23 · [GitHub](https://github.com/smart-mcp-proxy/mcpproxy-go) · [官网](https://mcpproxy.app) · 组织维护

**MCP 服务器聚合代理：统一端点+隔离审查+按需工具发现**

面向使用 AI Agent 的开发者的 MCP 网关：将数百个 MCP 服务器联邦到单一本地端点，Agent 通过少量发现/执行工具（retrieve_tools、describe_tool、call_tool_*）按需检索（BM25）与调用工具，减少上下文占用。新服务器进入隔离区需人工审查批准，工具定义变更默认需复审；支持可插拔安全扫描器（Snyk/Semgrep/Trivy 等，结果归一为 SARIF）；每次调用记录本地活动日志，含敏感数据检测，并提供 headless 任务的工具预检命令。提供 macOS/Windows/Linux 二进制、Homebrew/apt/dnf/AUR/go install 等安装方式，web UI 内嵌于单二进制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 联邦多个 MCP 服务器，绕过 Cursor 40 工具限制与 OpenAI 128 函数上限
- BM25 按需工具发现，减少初始工具定义的上下文占用
- 新服务器隔离审查 + 工具定义变更默认复审，可插拔 Docker 安全扫描器
- 全量调用活动日志（request ID 关联、敏感数据检测）与 headless 预检命令

## 适用场景

- 把多个 MCP 服务器聚合成一个端点供 Cursor、VS Code、Claude Desktop 使用
- 在批准新 MCP 服务器前隔离审查，降低工具定义攻击风险
- 审计 Agent 实际调用了哪些工具、参数是否含敏感数据
- CI/cron 等 headless 任务运行前预检所需工具是否就绪

## 场景标签

`网络安全` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L2:  MCPProxy — Supercharge AI Agents, Safely · One safe endpoint in front of every MCP server
> L29: - **Scale beyond API limits** – Federate hundreds of MCP servers while bypassing Cursor's 40-tool limit and OpenAI'
> L32: - **Pluggable security scanners** – Run Snyk, Semgrep, Trivy, Cisco, and other Docker-based scanners against quaran

## 星数曲线

```mermaid
xychart-beta
    title "smart-mcp-proxy/mcpproxy-go 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22", "2026-10-24"]
    y-axis "stars" 394 --> 399
    line [395, 396, 398, 398]
```

2026-10-18 395 → 2026-10-24 398（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `617be6f3dc4d` · [字段定义](../../DATASET.md)*
