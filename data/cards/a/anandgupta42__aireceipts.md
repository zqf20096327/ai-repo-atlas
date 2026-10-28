# anandgupta42/aireceipts

⭐ 31 · TypeScript · Apache-2.0 · 推送 2026-09-24 · [GitHub](https://github.com/anandgupta42/aireceipts) · [官网](https://anandgupta42.github.io/aireceipts/) · 个人维护

**本地读取 AI 编码代理会话记录并生成成本收据的 CLI**

面向使用 AI 编码代理的开发者的成本观测工具：本地解析 Claude Code、Codex、Gemini CLI、OpenCode、Cursor 的会话 transcript，按 Standard-API 价目重建可观测的成本下限（≥ 记法），提供状态栏实时计数、会话结束的分项收据、PR 评论附收据、周报与对比等命令。全程本地确定性运行，无需账号与 API key，transcript 不上传；共享收据仅含数字与截断的会话标题。Cursor 因日志无逐轮用量仅支持会话总额模式。以 npm CLI 提供，支持 --json/--csv/--svg/--png 输出。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 支持 5 种 AI 编码代理，含逐轮模型/工具/缓存分层计价（Cursor 为降级总额模式）
- 实时状态栏（Claude Code statusline，tmux/starship/PowerShell）与 5 小时配额倒计时
- PR 评论附加收据与 CI 检查、pre-push hook 自动化
- 确定性收据、金样本测试与引证价目行（厂商 URL/观测日期）

## 适用场景

- 查看 Claude Code/Codex 等代理会话花了多少 token 与 API 成本下限
- 在 PR 上附上构建该 PR 各会话的成本收据
- 状态栏实时监控上下文窗口占用与 5 小时配额消耗

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L17: not the token ledger. aireceipts reconstructs an observable Standard-API list-price
> L18: floor: live in your status bar, itemized when the session ends, attached to the PR.
> L84: |Agent|Depth|

## 星数曲线

```mermaid
xychart-beta
    title "anandgupta42/aireceipts 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-28 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `56d7fd0d8739` · [字段定义](../../DATASET.md)*
