# hydro13/tandem-browser

⭐ 625 · TypeScript · MIT · 推送 2026-10-21 · [GitHub](https://github.com/hydro13/tandem-browser) · [官网](https://tandembrowser.org/) · 个人维护

**本地优先的 Electron 浏览器：人与 AI agent 共用同一浏览器**

基于 Electron/Chromium 的本地优先桌面浏览器，将外部 AI agent 接入浏览器本体：agent 与用户共享同一套标签页、会话与 Cookie，可读取无障碍树、DOM 与实时网络日志，注入 userscript 改写页面，并在需要人工介入（验证码、风险操作）时交还控制权。通过 MCP（Claude Code/Desktop、Cursor、Windsurf 等）或 300+ 端点的 HTTP API 连接，模型无关（支持 GPT、Gemini、本地 Ollama/LM Studio），可经 Tailscale 远程连接。共暴露 257 个工具，设有 8 层安全边界防御提示注入。macOS 提供签名安装包，Windows 安装包未签名，Linux 需从源码构建且为 best-effort 支持。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 257 个工具供 agent 调用，覆盖导航、标签页、DevTools、网络检查、会话等 16 类
- 模型无关：任何支持 MCP 或 HTTP 的 agent 均可接入，含本地 Ollama/LM Studio
- 本地 MCP/HTTP 与经 Tailscale 的远程连接，多 agent 可同时共享同一浏览器
- 8 层安全边界隔离网页内容与 agent 层，含提示注入防御

## 适用场景

- 让 AI agent 在我已登录的真实浏览器里操作无 API 的 SaaS 网站
- 我与 agent 在同一浏览器中协作完成任务，遇到验证码时接手
- 通过 MCP 或 HTTP API 将现有 agent（Claude Code、Cursor 等）接入日常浏览器

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L12: Tandem is a local-first Electron browser that shifts the AI from a sidebar next
> L37: - **Bring any AI** — Tandem is model-agnostic. Any agent that speaks MCP
> L60: - **Not just another Chromium wrapper.** This is a daily-driver browser with a serious security perimeter around a 

## 星数曲线

```mermaid
xychart-beta
    title "hydro13/tandem-browser 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-24"]
    y-axis "stars" 622 --> 626
    line [623, 625, 625]
```

2026-10-18 623 → 2026-10-24 625（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `cb6209b43f96` · [字段定义](../../DATASET.md)*
