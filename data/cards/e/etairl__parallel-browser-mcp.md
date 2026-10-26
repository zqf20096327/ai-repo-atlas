# etairl/parallel-browser-mcp

⭐ 43 · TypeScript · Apache-2.0 · 推送 2026-09-10 · [GitHub](https://github.com/etairl/parallel-browser-mcp) · 个人维护

**供 AI agent 并行多会话浏览器自动化的 MCP 服务器**

一个 MCP 服务器，暴露数字会话模型让单一客户端同时创建并控制多个浏览器会话。通过统一的 provider 抽象层接入本地 Playwright Chromium、Browserbase、Anchor Browser 与 Cloudflare Browser Run 四种提供商，Browserbase 与 Anchor 连接后归一化为 Playwright 页面操作以保持工具接口一致。提供 4 个会话管理工具与 20 余个 browser_* 工具，配置经环境变量或 JSON 传入而非逐次调用。本地 Playwright 无需凭据，云提供商需各自 API key；可选启用 CloakBrowser 反检测。面向构建 agent 的开发者，可接入 Claude Code、Codex、Copilot、Cursor、Gemini、VS Code 等 MCP 客户端。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一客户端同时控制多个编号浏览器会话，所有 browser_* 工具接受 sessionId
- provider 抽象覆盖 Playwright/Browserbase/Anchor/Cloudflare Browser Run，云会话归一化为 Playwright 操作
- 约 20 个浏览器工具（导航/点击/截图/拖拽/文件上传等）加 4 个会话管理工具
- playwright provider 可选启用 CloakBrowser 隐身 Chromium

## 适用场景

- 让 AI agent 在多个浏览器会话中并行执行网页操作
- 在本地 Chromium 与云浏览器提供商之间切换而无需改动 agent 代码
- 为需要绕过机器人检测的会话启用隐身浏览器

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L6: `parallel-browser-mcp` is an MCP server for parallel browser automation. It exposes a numeric session model over MCP
> L19: - Provider abstraction shared across Browserbase, Anchor Browser, Cloudflare Browser Run, and local Playwright

## 星数曲线

```mermaid
xychart-beta
    title "etairl/parallel-browser-mcp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-26"]
    y-axis "stars" 41 --> 44
    line [42, 43, 43]
```

2026-10-18 42 → 2026-10-26 43（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `252e2107bb16` · [字段定义](../../DATASET.md)*
