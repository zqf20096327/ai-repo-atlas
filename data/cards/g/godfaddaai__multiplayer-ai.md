# godfaddaai/multiplayer-ai

⭐ 20 · JavaScript · MIT · 推送 2026-10-04 · [GitHub](https://github.com/godfaddaai/multiplayer-ai) · [官网](https://godfaddaai.github.io/multiplayer-ai/) · 个人维护

**让 Codex 与 Claude Code 会话多人共享的终端协作层**

面向 macOS 小团队的 CLI 工具：主机继续使用原生 Codex 或 Claude Code CLI，队友通过 Tailscale 网络以具名身份加入同一终端房间，查看共享会话的持久上下文并发送带署名的远程指令（每次任务同时只允许一个远程回合）。机制上读取本地 CLI 会话存储、经 Tailscale 身份绑定与一次性邀请授权，凭据存 macOS Keychain。限制：公开 alpha，仅 macOS，需现有 tailnet 与已认证的 codex/claude CLI；standalone Codex 默认只读；不提供任意远程 shell，远程审批一律拒绝。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 跨 Codex 与 Claude Code 的统一任务/事件模型，具名远程 prompt 以 [Multiplayer teammate: X] 落盘
- Tailscale 身份绑定 + 邀请令牌（主机仅存 SHA-256 哈希）+ 默认仅共享选定会话
- macOS Keychain 存储对等凭据，Keychain 不可用时回退 mode-0600 文件
- 提供仅含元数据的支持包与 alpha 队列收据/cohort 报告命令

## 适用场景

- 队友深入几十轮的 Codex/Claude Code 对话时，直接以自己名义追加指令而非看摘要
- 两台 Mac + Tailscale 环境下的结对编程/协作调试
- 受控的客户端工作：在客户自有的 Mac 与 tailnet 上做授权试点

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L233: mpai is a coordination layer above the providers:
> L245: mpai reads the local Claude Code CLI session store and uses Claude Code's
> L258: The strongest mode connects to the managed local Codex daemon so native clients

## 星数曲线

```mermaid
xychart-beta
    title "godfaddaai/multiplayer-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `ea4c3ab81e87` · [字段定义](../../DATASET.md)*
