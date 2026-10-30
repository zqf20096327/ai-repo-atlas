# demwick/polymarket-agent-mcp

⭐ 16 · TypeScript · MIT · 推送 2026-10-29 · [GitHub](https://github.com/demwick/polymarket-agent-mcp) · [官网](https://www.npmjs.com/package/polymarket-agent-mcp) · 个人维护

**面向 AI 客户端的 Polymarket 预测市场交易 MCP 服务器（48 工具）**

通过 MCP 协议向 Claude Code、Cursor 等 AI 客户端提供 48 个 Polymarket 操作工具，覆盖市场发现、分析（AI 机会评分/信念评分）、下单交易、跟单交易（监控循环/回测）、组合与风险管理（止损止盈/敞口上限）。默认 preview 模拟模式，可切 live 实盘。数据存本地 SQLite，密钥仅驻内存。支持 stdio 与 HTTP 两种传输；单租户设计，README 明确警告公开 HTTP 端点会共享状态并可被任意调用者消耗钱包。提供 npm 全局安装、Docker 镜像（GHCR 多架构）与源码构建三条安装路径。

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

- 48 个工具分 6 类：发现/分析/交易/跟单/组合风险/配置
- 默认 preview 模拟模式，实盘需显式 config.go_live 并配置签名密钥
- 安全限制：单笔上限、总敞口上限、止损止盈、最小流动性要求
- stdio 与 HTTP 双传输，GHCR 预构建多架构 Docker 镜像

## 适用场景

- 在 Claude Code 或 Cursor 中用自然语言查询和交易 Polymarket
- 跟踪聪明钱流向并自动跟单（含回测）
- 对持仓设置止损止盈并做组合风险检查

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L21: The most comprehensive MCP server for Polymarket — 48 tools spanning direct trading, market discovery, smart money 
> L168:         | MCP Protocol (stdio)
> L19: **Trade, analyze, and automate Polymarket prediction markets through AI.**

## 星数曲线

```mermaid
xychart-beta
    title "demwick/polymarket-agent-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `8ea1b9b70eb7` · [字段定义](../../DATASET.md)*
