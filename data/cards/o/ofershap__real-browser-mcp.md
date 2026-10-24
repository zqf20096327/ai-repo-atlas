# ofershap/real-browser-mcp

⭐ 57 · JavaScript · MIT · 推送 2026-10-19 · [GitHub](https://github.com/ofershap/real-browser-mcp) · 个人维护

**让 AI 代理控制你已登录的真实 Chrome 的 MCP 服务器**

由本地 MCP 服务器与 Chrome MV3 扩展组成，二者经 localhost WebSocket 通信，使 Cursor、Claude Code 等 MCP 客户端的代理能操作用户当前打开的 Chrome：保留 cookies、SSO 与现有标签页。提供 18 个工具，覆盖快照、点击、输入、导航、控制台与网络调试。限制：需安装 Chrome 扩展才能工作，不适合 CI 并行干净运行场景（README 建议该场景用 Playwright）。数据不离开本机。

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

- 本地 MCP 服务器 + Chrome MV3 扩展经 localhost WebSocket 桥接
- 18 个工具：快照/点击/输入/导航/控制台/网络/执行 JS 等
- 复用已有 cookies、SSO 会话与标签页，数据不经云端
- 支持多 Chrome profile（多实例不同端口）

## 适用场景

- 让编码代理在已登录 staging 的浏览器里验证修复效果
- 调试需要 SSO 会话的内部网页面
- 让代理读取当前页面的控制台与网络请求排查问题

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L35: **real-browser-mcp** is the bridge: a local MCP server plus a Chrome extension over localhost WebSocket. Your agent
> L45: - **MCP server** - runs on your machine, talks to your AI agent (Cursor, Claude Code, VS Code, …)

## 星数曲线

```mermaid
xychart-beta
    title "ofershap/real-browser-mcp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-24"]
    y-axis "stars" 55 --> 58
    line [56, 57, 57]
```

2026-10-18 56 → 2026-10-24 57（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `17b2f310afa0` · [字段定义](../../DATASET.md)*
