# demoos415/lua-script-bridge

⭐ 68 · HTML · 推送 2026-10-27 · [GitHub](https://github.com/demoos415/lua-script-bridge) · 个人维护

**MCP 服务器：让 AI 助手接入运行中的 Roblox Luau 环境**

面向 Roblox 开发者的 Model Context Protocol 服务器，将 AI 编码助手（Claude、Cursor 等 MCP 客户端）连接到运行中的 Luau 会话。由三层组成：暴露工具/资源/提示的 MCP 面、传输无关的 Relay 消息通道、加载进会话的 Luau 运行时插装库。通过身份绑定与可组合能力令牌（inspect/execute/subscribe/replay 等作用域）控制权限，默认仅授予观察权限，操作写入 append-only 审计日志，失败时封闭而非放行。分发通过发布渠道下载二进制与插装包，首次启动前校验完整性清单。

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

- MCP 面向 AI 客户端暴露工具、资源与提示
- 三层架构：MCP 面 / Relay 通道 / Luau 插装库，各层可替换
- 身份绑定执行与可组合能力令牌（可撤销、限时）
- append-only 审计日志与确定性回放钩子

## 适用场景

- 让 AI 助手在运行中的 Roblox 会话里做快速检查与引导式修复
- 录制操作序列并在 bench 会话上回放做回归验证
- 以能力白名单方式控制助手对游戏运行时的访问权限

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L8: NeuroForge is a Model Context Protocol (MCP) server that gives AI coding companions (Claude, Cursor, or any MCP-comp
> L18: 1. **The MCP Face** — a protocol-compliant server that exposes tools, resources, and prompts to AI assistants. This

## 星数曲线

```mermaid
xychart-beta
    title "demoos415/lua-script-bridge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 67 --> 69
    line [68, 68]
```

2026-10-18 68 → 2026-10-28 68（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `5a50c9e7bd79` · [字段定义](../../DATASET.md)*
