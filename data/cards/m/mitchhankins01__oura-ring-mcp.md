# mitchhankins01/oura-ring-mcp

⭐ 31 · TypeScript · 推送 2026-02-08 · [GitHub](https://github.com/mitchhankins01/oura-ring-mcp) · 个人维护

**把 Oura 戒指健康数据接入 Claude 等 AI 助手的 MCP 服务器**

通过 MCP 协议将 Oura Ring 的睡眠、准备度、活动与健康指标数据提供给 Claude Desktop、Claude.ai 等 AI 助手，输出人类可读的格式化结果而非原始 JSON。提供 17 个工具（数据获取与智能分析，含异常检测、指标相关性、周期对比）、5 个资源与 5 个提示模板。认证支持个人访问令牌或 OAuth CLI 流程，支持 Railway 远程部署并代理 OAuth。需要 Node >=18 与 Oura 账号。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 17 个 MCP 工具：睡眠/准备度/活动/心率/SpO2/压力等数据获取与智能分析
- 异常检测、指标相关性、条件对比（如饮酒 vs 不饮酒睡眠）等分析工具
- 支持 Personal Access Token 与 OAuth 两种认证及令牌自动刷新
- 提供 Railway 远程部署方案，用户直接用 Oura 账号授权

## 适用场景

- 让 Claude 直接回答我昨晚睡得怎么样、今天该不该训练
- 分析健康指标的趋势、相关性与异常
- 对比不同条件（如补镁前后）下的睡眠与恢复数据

## 场景标签

 · 领域:健康数据/AI 集成工具

## 证据(README 行号)

> L7: An MCP server that connects your Oura Ring to Claude and other AI assistants. Get human-readable insights about your
> L58: Add to `claude_desktop_config.json`:

## 星数曲线

```mermaid
xychart-beta
    title "mitchhankins01/oura-ring-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-28 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `c86e27c5b4c8` · [字段定义](../../DATASET.md)*
