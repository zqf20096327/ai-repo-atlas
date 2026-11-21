# hypernewbie/phi

⭐ 10 · TypeScript · 推送 2026-11-20 · [GitHub](https://github.com/hypernewbie/phi) · 个人维护

**为 AI 编码助手提供浏览器统一控制台的终端复用器**

用单个 Go 二进制提供 Web UI，在浏览器中以真实 PTY（xterm.js 渲染）运行和切换多个 AI 编码代理 CLI（OpenCode、Claude Code、Antigravity、Pi Coder），并伴随只读的实时 git diff/log 面板。关键机制：读取各工具磁盘上的会话历史（SQLite/JSONL 等）实现一键恢复会话；关闭浏览器标签后 PTY 进程保留 30 分钟可重连。限制：默认不加认证，仅建议绑定 localhost/LAN；驱动哪些代理取决于用户自行安装的 CLI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 浏览器内多 AI 代理标签页，每个会话为真实 PTY（xterm.js WebGL 渲染）
- 读取各工具磁盘会话历史，一键恢复过去对话
- 实时 git diff 侧栏与 git worktree 切换
- phi-cmd 命令行客户端可从脚本和其他代理驱动 Phi

## 适用场景

- 在同一界面并行运行并监控多个 AI 编码代理
- 断开后重新接管仍在运行的代理会话
- 通过脚本或代理程序向编码代理发送提示并读取 diff

## 场景标签

 · 领域:开发者工具/AI 编码工作流

## 证据(README 行号)

> L3: **A terminal multiplexer and browser-based control center for AI coding assistants.**
> L5: Phi gives you a single web UI to run, monitor, and switch between multiple AI coding agents — OpenCode, Claude Code,
> L25: Phi is a single Go binary serving a vanilla-JS frontend (no build step, no framework).


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `0333314e94f5` · [字段定义](../../DATASET.md)*
