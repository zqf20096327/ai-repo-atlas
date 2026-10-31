# frane/vibesurfer

⭐ 16 · Rust · Apache-2.0 · 推送 2026-09-24 · [GitHub](https://github.com/frane/vibesurfer) · [官网](https://crates.io/crates/vibesurfer) · 个人维护

**给 LLM/agent 用的 Rust 浏览器守护进程，省 token 地读写网页**

用 Rust 编写的本地浏览器守护进程，供 LLM agent 通过 CLI 或 MCP 工具操作网页。读取返回状态 token 与树增量而非完整 DOM 以节省上下文；写入前校验 token，页面变动则失败重读。底层使用三种原生引擎（macOS WKWebView、Linux WebKitGTK、Windows WebView2），输入派发以 isTrusted=true 方式绕过反自动化检测（自述在启发式检测上的通过情况，并说明不等于通过商业反爬服务）。支持 SKILL.md 与 MCP 两种接入方式，可自动检测并注册到 Claude Code、Cursor、Codex CLI 等客户端。需注意绕过反爬涉及合规边界。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 读取返回状态 token 与树增量，Hacker News 首页约 50 token（自述数字）
- 原生输入派发使点击/键盘事件 isTrusted=true（三平台）
- SKILL.md 与 MCP 双通道接入，自动检测 Claude Code/Cursor/Codex CLI 等
- 会话 cookie 上下文内下载文件（含登录后的 PDF）

## 适用场景

- 让 agent 测试或操作 Web 应用，节省上下文预算
- agent 需要以可信事件与网页交互（富文本编辑器输入等）
- 通过 Claude Code 插件市场或 MCP 一行命令接入 agent

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L20: vibesurfer is a native browser daemon in Rust. Reads return state tokens and tree deltas instead of the full DOM. W
> L72: - **Skill**: drop `SKILL.md` into the agent's skills directory. The agent reads it as context and calls the `vs` bi
> L73: - **MCP**: register `vs mcp` as an MCP server. The agent calls vibesurfer primitives as MCP tools over JSON-RPC, no

## 星数曲线

```mermaid
xychart-beta
    title "frane/vibesurfer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `e5ac9b14424a` · [字段定义](../../DATASET.md)*
