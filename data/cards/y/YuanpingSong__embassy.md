# YuanpingSong/embassy

⭐ 13 · TypeScript · MIT · 推送 2026-09-28 · [GitHub](https://github.com/YuanpingSong/embassy) · [官网](https://yuanpingsong.github.io/embassy/) · 个人维护 · 中文 README

**macOS 上让 Claude Code 会话与 Codex CLI agent 互相按名传信的本地消息代理**

Embassy 是一个运行在 macOS 上的消息代理（broker）：让在运行的 Claude Code 会话与 Codex CLI agent 之间按别名互发消息，支持单机或经 SSH 跨自有机群通信。核心含私有账本、投递协调器与三个写入适配器（Claude socket、Codex App Server 操作、SSH 交接）；通过原生接口唤醒接收方而非轮询，每条消息返回送达回执（仅证明传输，不证明已读）。Codex agent 从运行中的 Codex daemon 自动发现，Claude 会话在发送时记录。以 npm 全局包形式安装，由 launchd per-user agent 承载；要求 macOS、Node.js 22+、Claude Code 已安装，接收方需 Codex 托管安装且 App Server daemon 在运行。

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

- Claude↔Codex、同提供方之间统一命令与回执模型的消息投递
- 通过原生接口唤醒接收 agent，agent 无需轮询
- 跨自有 Mac 经 SSH 联邦，SSH 登录即信任边界
- 投递阶段持久化（queued/reserved/armed/accepted/terminal），支持 STEER 引导与 kill 开关

## 适用场景

- 在一个 Claude Code 会话中按名请求 Codex agent 做代码评审并接收回复
- 把多台自己的 Mac 上的编码 agent 组成可互发消息的联邦
- 用 TUI 查看各 endpoint 状态、队列深度与路由

## 场景标签

`多智能体` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: Embassy lets live Claude Code sessions and Codex CLI agents message one another
> L31: The core is deliberately small: one private ledger, one delivery coordinator,

## 星数曲线

```mermaid
xychart-beta
    title "YuanpingSong/embassy 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 11 --> 14
    line [12, 13, 13]
```

2026-10-18 12 → 2026-10-31 13（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `3c4d4653e2d6` · [字段定义](../../DATASET.md)*
