# feritzcan2/termloop

⭐ 41 · Rust · NOASSERTION · 推送 2026-10-29 · [GitHub](https://github.com/feritzcan2/termloop) · [官网](https://termloop.ai) · 个人维护

**在本地与远程统一运行多个编码 agent 的 AI 终端**

Electron + Rust 守护进程的桌面终端工作区：在同一窗口运行 Claude Code、Codex 与普通终端会话，守护进程持有 PTY 使会话在关闭窗口后仍存活。提供 Ask To 向其他 agent 求审查、Handoff 转交上下文、Session Fork、带验收标准的 Task 与可选 Git worktree、diff 审查等协调功能；支持通过 SSH/Tailscale 连接最多 8 台远程计算机，agent 在服务器上运行并使用用户既有订阅登录，产品不代理模型流量。另提供移动 Companion 与 Steward 助手。macOS/Windows/Linux 提供安装包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `dual` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Ask To/Handoff 实现 agent 间上下文传递与互相审查
- Rust 守护进程持有 PTY，关闭窗口后会话存活并可重连
- SSH/Tailscale 接入最多 8 台远程计算机，agent 用既有订阅运行
- Task 携带验收标准与可选 Git worktree，diff 审查可发送给运行中的 agent

## 适用场景

- 同时运行多个编码 agent 并让它们互相审查代码
- 在远程 Linux 服务器上跑 agent、笔记本上查看与输入
- 用 Task 与 worktree 组织需要分支隔离的改动

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L28: - **Bring your own agents.** TermLoop launches the Claude Code and Codex CLIs with your existing subscriptions and 
> L151: Claude Code and OpenAI Codex are the first-class agent launch paths, alongside ordinary terminal and dev-run Sessi

## 星数曲线

```mermaid
xychart-beta
    title "feritzcan2/termloop 星数(近 2 点)"
    x-axis ["2026-10-23", "2026-10-30"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-23 41 → 2026-10-30 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `e40262f110b5` · [字段定义](../../DATASET.md)*
