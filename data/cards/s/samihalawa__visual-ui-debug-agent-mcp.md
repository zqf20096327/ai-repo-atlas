# samihalawa/visual-ui-debug-agent-mcp

⭐ 83 · JavaScript · ISC · 推送 2026-10-01 · [GitHub](https://github.com/samihalawa/visual-ui-debug-agent-mcp) · [官网](https://www.npmjs.com/package/visual-ui-debug-agent-mcp) · 个人维护

**给 MCP 客户端提供浏览器 UI 检查与测试能力的 MCP 服务器**

VUDA 是一个基于 Playwright 的 Model Context Protocol (MCP) 服务器，通过标准输入输出在本地运行，为 MCP 兼容的 AI 客户端提供 29 个工具：截图（全页/视口/元素/批量）、DOM 与计算样式检查、多步 UI 工作流验证、控制台捕获、性能分析、API 端点测试、站点地图爬取与视觉对比。浏览器可在本地、Browserbase、Anchor 或任意 CDP 端点运行，本地模式无需任何 provider 账号。面向希望让 AI 客户端直接操作和调试真实网页的开发者，要求 Node.js 20+ 与 Chromium 兼容浏览器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | ISC |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 29 个 MCP 工具：截图、DOM 检查、工作流验证、控制台/性能监控、视觉对比
- 浏览器运行时可选本地、Browserbase、Anchor 或任意 CDP 端点，所有工具共用同一运行时
- 通过 npx 一条命令运行，本地模式无需 provider 账号
- 支持 Cookie 注入与 Playwright storage state 持久化登录态

## 适用场景

- 让 Claude 等 MCP 客户端打开网页、截图并定位布局问题
- 用自然语言描述用户旅程，验证登录/表单等多步流程
- 对比两个页面渲染状态并生成视觉差异
- 爬取站点地图并批量截图做 UI 巡检

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L10:  Give an MCP-compatible AI client a real browser, screenshots, DOM inspection, workflow validation, console capture
> L15: VUDA (Visual UI Debug Agent) is a Model Context Protocol server for inspecting and testing web interfaces with Play

## 星数曲线

```mermaid
xychart-beta
    title "samihalawa/visual-ui-debug-agent-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 82 --> 84
    line [83, 83]
```

2026-10-18 83 → 2026-10-25 83（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `200eda6a4e66` · [字段定义](../../DATASET.md)*
