# zhixuli0406/DuDuClaw

⭐ 50 · Rust · Apache-2.0 · 推送 2026-10-24 · [GitHub](https://github.com/zhixuli0406/DuDuClaw) · [官网](https://duduclaw.dudustudio.monster/) · 组织维护 · 中文 README

**把 AI 编程 CLI 变成接入 11 个聊天平台的常驻 AI 员工网关**

Rust 单二进制自托管网关，把 Claude Code、Codex 等 12 种 AI CLI 运行时或任意 OpenAI 兼容 API 接入 Telegram/LINE/Discord 等 11 个消息渠道，由 MCP(JSON-RPC 2.0) 桥接；内置独立评审（judge）审核结果、SQLite 时序记忆与分层 wiki、247 个 MCP 工具、策略内核与 OS 沙箱、Web 仪表盘与本地推理 crate。配置与记忆留在本机。安装提供桌面应用（Tauri，签名构建）、npm 预编译二进制、源码编译与 Yocto 整机镜像（pre-GA）；npm 路径需 Node.js 20+，不自带 LLM，需自带 API key 或本地模型。核心 Apache 2.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 12 种 AI CLI 运行时可切换，上下文跨后端保留
- 11 个消息渠道，按 agent 分配独立 bot token
- 247 个 MCP 工具（stdio 与 HTTP/SSE），含记忆/任务板/Odoo ERP/computer use
- 独立 judge 审核工作成果，费用逐条记录，记忆存本地

## 适用场景

- 让团队在 LINE/Discord/Telegram 上直接向 AI 编程 agent 派活并跟进任务
- 多 agent 多渠道部署，需要账号轮换、护栏与审计的场景
- 作为独立 MCP 记忆服务器供其他客户端调用

## 场景标签

`编码 Agent` `多智能体` `聊天机器人` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L9: All you need is one Rust binary. Channel routing, conversation memory, multi-account rotation, behavioral guardrails
> L47: The AI runtime is the brain, DuDuClaw is the plumbing, and MCP (JSON-RPC 2.0) is the bridge. Swap the brain, keep t
> L50: AI Runtime (brain) — Claude Code / Codex / Antigravity / Grok / … (11 CLIs) / OpenAI-compat

## 星数曲线

```mermaid
xychart-beta
    title "zhixuli0406/DuDuClaw 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-25"]
    y-axis "stars" 48 --> 51
    line [49, 50, 50]
```

2026-10-18 49 → 2026-10-25 50（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `fc2380a98325` · [字段定义](../../DATASET.md)*
