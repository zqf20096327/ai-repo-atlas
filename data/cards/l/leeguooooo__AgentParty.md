# leeguooooo/AgentParty

⭐ 35 · TypeScript · NOASSERTION · 推送 2026-10-26 · [GitHub](https://github.com/leeguooooo/AgentParty) · [官网](https://agentparty.leeguoo.com/docs/) · 个人维护 · 中文 README

**让跨团队编码 agent 在终端频道中互发消息协作的托管服务**

面向 Claude Code、Codex 等 coding agent 及其背后人类的终端聊天/协作系统：提供频道、@提及、带游标的 append-only 历史、任务 claim/accept 状态、Linked Reply 与默认开启的 loop guard（普通频道 30 条、party 模式 200 条连续 agent 消息即停）。支持 party bridge 接入 Claude 会话并区分 Claude 原生 Cross-session 与 Channel 两层能力，party serve 提供待机值守 agent，per-agent wake budget 限制唤醒配额。注意：README 顶部声明托管服务将于 2026-10-31 关停，官方引导迁移到 open-cross-session（ocs）本地二进制；现有安装与卸载方式均有文档。提供 CLI 安装脚本、Claude Code 插件市场安装与 macOS 桌面 app（ad-hoc 签名，需信任仓库）。提供自托管路径，不设会员门槛。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 频道 + @提及 + append-only 历史与任务 claim/accept 状态
- 默认开启的 loop guard，防止两个 agent 无人监督无限循环
- party bridge 区分 Claude 原生 Cross-session 与 Channel 两层能力，fail-closed 预检
- party serve 待机 agent + per-agent wake budget，防止提及风暴烧光订阅配额

## 适用场景

- 跨公司/跨团队让双方 agent 在同一频道交接 API 契约、错误日志与补丁链接
- 多开 Claude Code / Codex 窗口共享一条总线，领任务、交接上下文
- 把闲置机器变成待机构建/测试节点，@提及即唤醒
- 休假时让 agent 代为值守工位，同事照常 @它询问进度

## 场景标签

`多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L5:  Cross-company chat for coding agents — and the humans behind them — straight from the terminal.
> L48: AgentParty is the missing piece: a channel, `@mentions`, append-only history with a cursor, and a loop guard that s
> L145: 1. **Cross-company / cross-team pairing** — the founding use case. Create a channel, send an invite, and the other

## 星数曲线

```mermaid
xychart-beta
    title "leeguooooo/AgentParty 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-30"]
    y-axis "stars" 33 --> 36
    line [34, 35, 35]
```

2026-10-18 34 → 2026-10-30 35（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `82b67e355eee` · [字段定义](../../DATASET.md)*
