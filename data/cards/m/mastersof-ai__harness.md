# mastersof-ai/harness

⭐ 42 · TypeScript · MIT · 推送 2026-03-19 · [GitHub](https://github.com/mastersof-ai/harness) · [官网](https://github.com/mastersof-ai/harness#readme) · 组织维护

**以 Markdown 定义 agent 的运行时，支持终端 TUI 与 Web UI**

基于 Claude Agent SDK 的 agent 运行时：用 IDENTITY.md 文件直接作为系统提示词定义 agent，无隐藏框架指令；提供终端 TUI 与 `--serve` 多用户 Web UI 两种界面，共享同一运行时。内置 9 种工具（均为进程内 MCP 服务器）、3 个子 agent、持久化记忆层，支持 A2A 协议双向调用、YAML frontmatter 元数据、token 鉴权与 bubblewrap 沙箱。认证需 Claude Code 凭据或 Anthropic API key，npm 全局安装，需 Node.js 22。

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

- IDENTITY.md 直接作为系统提示词，无框架注入行为
- 终端 TUI 与 Web UI 双界面共享同一运行时
- 内置 memory/workspace/web/shell/a2a 等 9 种进程内 MCP 工具
- token 鉴权、速率限制、bubblewrap 沙箱与 LGPD 合规隐私

## 适用场景

- 本地终端中快速创建和调试自定义 agent
- 团队通过浏览器访问共享的 agent 服务
- 让 agent 通过 A2A 协议调用远程 agent（LangGraph、Bedrock 等）

## 场景标签

`Agent 框架` `多智能体` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L5: An agent runtime where you control the entire system prompt. Write a markdown file, get an agent -- no hidden framew
> L20: - **No separate billing.** Uses your existing Claude Code subscription or API key. Powered by the Claude Agent SDK 

## 星数曲线

```mermaid
xychart-beta
    title "mastersof-ai/harness 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-27 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `442c6045f65a` · [字段定义](../../DATASET.md)*
