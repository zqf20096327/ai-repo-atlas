# Mytai20100/opencode-browser

⭐ 14 · JavaScript · MIT · 推送 2026-09-22 · [GitHub](https://github.com/Mytai20100/opencode-browser) · 个人维护

**Chrome 自动化 MCP 服务器：让 AI agent 远程操控浏览器**

由 Node.js MCP 服务器与 Manifest V3 Chrome 扩展两部分组成，通过本地 WebSocket（默认 :3002）通信的浏览器自动化插件。向 AI agent 提供 165+ 个 chrome_ 前缀工具，覆盖标签页/窗口管理、截图、页面交互、CDP 调试与网络拦截、Cookie/存储/书签操作、会话保存等；支持在 OpenCode、Claude Code、Codex 中注册使用。提供 chrome_get_tool_graph 按意图生成执行计划以减少冗余调用。npm 安装或源码构建，扩展需在 Chrome 开发者模式下加载未打包目录。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 165+ 个 chrome_ 前缀工具，覆盖标签页、交互、CDP 调试、网络拦截、截图等
- MCP Server + Chrome Extension 经本地 WebSocket 双段式架构
- chrome_get_tool_graph 按意图返回优化执行计划，减少冗余调用
- 支持注册到 OpenCode / Claude Code / Codex

## 适用场景

- 让编程 agent 直接操控 Chrome 完成登录、填表、截图等任务
- 通过 CDP 调试工具捕获网络请求与控制台日志辅助开发
- 用 chrome_intercept_request + chrome_mock_response 注入模拟数据做前端测试
- 保存并恢复浏览器会话避免重复登录

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L10: Chrome automation plugin for OpenCode via WebSocket and Chrome Extension. Gives AI agents **165+ tools** covering t
> L16: - **MCP Server** — a Node.js process that OpenCode connects to via stdio. It exposes all tools to the AI agent and 

## 星数曲线

```mermaid
xychart-beta
    title "Mytai20100/opencode-browser 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `c173d616ae74` · [字段定义](../../DATASET.md)*
