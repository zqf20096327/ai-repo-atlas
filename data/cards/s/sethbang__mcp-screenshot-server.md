# sethbang/mcp-screenshot-server

⭐ 35 · TypeScript · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/sethbang/mcp-screenshot-server) · 个人维护

**为 AI 助手提供网页与系统截图能力的 MCP 服务器**

基于 Model Context Protocol 的截图服务器，向 Claude Desktop、Claude Code、Cursor 等 MCP 客户端暴露两个工具：take_screenshot 用 Puppeteer 无头 Chromium 抓取网页（支持视口、全页、CSS 选择器定位），take_system_screenshot 调用 macOS/Linux/Windows 原生工具截取全屏、窗口或区域。内置 SSRF 防护、路径穿越校验、命令注入防护与并发限制。系统截图功能依赖各平台原生工具（如 Linux 需 maim/scrot 之一），网页截图无需额外安装；提供 npx --doctor 自检命令。

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

- Puppeteer 网页截图与三平台原生系统截图两种 MCP 工具
- SSRF/DNS rebinding/命令注入/路径穿越多层安全防护
- npx --doctor 探测缺失系统工具并输出对应发行版安装命令
- 三层测试体系（Unit/Integration/E2E），Linux E2E 经 Docker 运行

## 适用场景

- 让 Claude/Cursor 等 MCP 客户端按对话指令截取网页或屏幕
- 开发调试时让 AI 助手查看本地服务页面（需开启 ALLOW_LOCAL）
- 为 Agent 工作流补充可视化取证能力

## 场景标签

 · 领域:AI 工具/桌面自动化

## 证据(README 行号)

> L7: An MCP (Model Context Protocol) server that provides AI assistants with screenshot capabilities — both web page capt
> L111: The server exposes two MCP tools:

## 星数曲线

```mermaid
xychart-beta
    title "sethbang/mcp-screenshot-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-30 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `dfd496a7254c` · [字段定义](../../DATASET.md)*
