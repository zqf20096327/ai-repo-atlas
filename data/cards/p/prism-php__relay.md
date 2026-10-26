# prism-php/relay

⭐ 153 · PHP · 推送 2026-03-20 · [GitHub](https://github.com/prism-php/relay) · [官网](https://prismphp.com) · 组织维护

**PHP/Laravel 的 MCP 客户端集成包：让 Prism 接入 MCP 服务器工具**

Prism PHP 的 MCP 客户端扩展包，将 Model Context Protocol 服务器提供的外部工具接入 Prism 构建的 AI agent。通过发布 config/relay.php 显式定义各 MCP 服务器连接，支持 HTTP 与 STDIO 两种传输方式；HTTP 传输支持 OAuth/Bearer 令牌附加（OAuth 流程本身需应用自行完成），STDIO 通过子进程标准输入输出通信，可用 env 传递环境变量。支持在单个 agent 中组合多个 MCP 服务器的工具，并提供 AuthorizationException 等异常类型。经 Composer 安装，面向 Laravel/PHP 开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 将 MCP 服务器工具接入 Prism agent
- 支持 HTTP 与 STDIO 两种传输机制
- HTTP 传输支持 Bearer 令牌附加，401 时抛出 AuthorizationException 触发重新授权
- 单个 agent 可组合多个 MCP 服务器的工具

## 适用场景

- 让 Prism 构建的 AI agent 使用 Puppeteer 等 MCP 工具浏览网页、截图
- 在 Laravel 应用中通过 CLI 交互调用 MCP 工具完成任务
- 为 PHP AI 应用统一配置和调用多个 MCP 服务器

## 场景标签

 · 领域:LLM 应用开发/工具集成

## 证据(README 行号)

> L13: A seamless integration between Prism and Model Context Protocol (MCP) servers that empowers your AI applications wi
> L46: Here's how you can integrate MCP tools into your Prism agent:

## 星数曲线

```mermaid
xychart-beta
    title "prism-php/relay 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 152 --> 154
    line [153, 153]
```

2026-10-18 153 → 2026-10-26 153（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `b8ccd276baa5` · [字段定义](../../DATASET.md)*
