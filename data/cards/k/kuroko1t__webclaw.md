# kuroko1t/webclaw

⭐ 22 · TypeScript · MIT · 推送 2026-03-07 · [GitHub](https://github.com/kuroko1t/webclaw) · [官网](https://github.com/kuroko1t/webclaw) · 个人维护

**运行在真实 Chrome 中的 WebMCP 浏览器 agent，供 MCP 客户端调用**

由 Chrome 扩展 + MCP 服务器（WebSocket 桥接）组成的浏览器自动化工具：MCP 客户端（Claude Desktop/Code、Cursor、VS Code Copilot、Windsurf）通过 21 个 MCP 工具（navigate/click/type/screenshot 等）控制用户已登录的真实 Chrome。页面以带 @ref 标签的紧凑无障碍树形式呈现给模型，不依赖像素坐标或 CSS 选择器；支持发现并调用页面声明的 WebMCP 工具（原生 WebMCP 需 Chrome 146+），最多同时运行 10 个 MCP 服务器实例。安装方式为 npm 包（npx webclaw-mcp）配合手动加载扩展，或 pnpm 源码构建。

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

- 以 Chrome 扩展形式运行于真实浏览器，保留用户登录态与 cookies
- 页面以带稳定 @ref 标签的紧凑无障碍树供模型读取与操作
- 21 个 MCP 工具覆盖页面交互、标签页管理与导航
- 原生 WebMCP 工具发现与调用（Chrome 146+ navigator.modelContext）

## 适用场景

- 让 Claude/Cursor 等 MCP 客户端在已登录的真实 Chrome 中执行网页操作
- 在个人生产力、开发、测试场景中自动化浏览器任务
- 多会话并行：同时运行最多 10 个 MCP 服务器实例

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L7: A **WebMCP-native** browser agent that runs inside your real Chrome — control it from Claude, Cursor, and any MCP cl
> L113: 1. The AI calls MCP tools (`navigate_to`, `page_snapshot`, `click`, ...)
> L114: 2. The MCP server forwards requests to the Chrome extension via WebSocket

## 星数曲线

```mermaid
xychart-beta
    title "kuroko1t/webclaw 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-28 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `80619d2b5795` · [字段定义](../../DATASET.md)*
