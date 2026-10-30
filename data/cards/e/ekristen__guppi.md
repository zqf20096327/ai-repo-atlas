# ekristen/guppi

⭐ 15 · Go · MIT · 推送 2026-04-20 · [GitHub](https://github.com/ekristen/guppi) · [官网](https://guppi.sh) · 个人维护

**浏览器里监控所有 tmux 会话中 AI agent 状态的单用户工具**

Go 后端加嵌入式 React 前端组成单二进制，通过 PTY 与 tmux attach-session 在浏览器（xterm.js）中呈现完整终端视图，并用 tmux 控制模式实时发现会话/窗口/面板变化。它跟踪 tmux 内运行的 AI 编码代理（Claude Code、Codex、GitHub Copilot CLI、OpenCode），经各代理 hooks 上报状态，在总览页与侧栏以 active/waiting/errored 徽标展示，并在代理需要输入或出错时发送浏览器/桌面推送通知。面向使用 tmux 并行运行多个 AI 代理的单个开发者；明确不支持多用户、代理编排与 tmux 配置管理。提供 dist、curl 脚本与源码构建三种安装方式，默认启用 TLS。

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

- PTY + xterm.js 在浏览器还原完整终端视图，单二进制部署
- 通过 hooks 跟踪 Claude Code/Codex/Copilot CLI/OpenCode 四种代理的状态
- 代理 waiting/error 时发送 Web Push 与桌面通知（标签页关闭也可达）
- tmux 控制模式实时同步会话、窗口、面板状态

## 适用场景

- 同时在多个 tmux 会话跑多个 AI 编码代理时，一眼掌握谁在等待输入或出错
- 离开终端后在浏览器或手机上继续查看和操作 tmux 会话
- 用脚本或命令行向 guppi 发送自定义状态通知

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L11: It also tracks AI coding agents (Claude Code, Codex, Copilot, OpenCode) running inside your sessions, surfacing the
> L27: - **Agent orchestration** — guppi doesn't start, stop, or control your agents. It watches and reports. You run your

## 星数曲线

```mermaid
xychart-beta
    title "ekristen/guppi 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-29", "2026-10-30"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-30 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `43c949b60b08` · [字段定义](../../DATASET.md)*
