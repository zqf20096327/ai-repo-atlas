# tuandm/verdict-cli

⭐ 20 · JavaScript · MIT · 推送 2026-10-19 · [GitHub](https://github.com/tuandm/verdict-cli) · 个人维护

**为 AI 编码 agent 提供省 token 的浏览器验证 CLI**

基于 Playwright 的持久化无头 Chromium 命令行工具：CLI 客户端经 localhost HTTP 连接常驻 Node.js 守护进程，每次调用输出约 75 token 的 ARIA 快照，供 Claude Code、Codex CLI、Cursor 等 agent 通过 Bash 调用做浏览器操作与验证。功能含交互元素快照与 diff、CSS 检查与样式修改、响应式截图、AES-256-CBC 加密认证会话保存、handoff 手动登录、批量命令链。要求 Node.js 18+，Chromium 由 Playwright 自动安装。

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

- 每次调用约 75 token 的 ARIA 快照输出
- 常驻守护进程，后续调用约 100-200ms
- AES-256-CBC 加密的认证会话保存与 handoff/resume 手动登录流程
- 快照 diff、CSS 检查/样式修改、响应式截图、chain 批量命令

## 适用场景

- AI 编码 agent 在浏览器中验证代码改动效果
- agent 处理需登录的页面（SSO/MFA/CAPTCHA 手动登录后复用会话）
- 通过快照 diff 确认点击等操作是否改变页面状态

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3: Token-efficient browser verification for AI coding agents.
> L297: AI Agent  →  Bash  →  CLI client (bin/browse.mjs)
> L284: Verdict works with any agent that can run Bash commands. Install globally and call `verdict` directly.

## 星数曲线

```mermaid
xychart-beta
    title "tuandm/verdict-cli 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `8fb21fddde02` · [字段定义](../../DATASET.md)*
