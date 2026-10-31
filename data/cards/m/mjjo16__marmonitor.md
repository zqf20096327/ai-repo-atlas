# mjjo16/marmonitor

⭐ 27 · TypeScript · MIT · 推送 2026-08-25 · [GitHub](https://github.com/mjjo16/marmonitor) · 个人维护 · 中文 README

**tmux 状态栏监控器：实时追踪 Claude/Codex/Gemini 编码会话**

面向在 tmux 中并行运行多个 AI 编码 agent（Claude Code、Codex、Gemini CLI）的开发者的监控工具。以 npm 全局安装的 CLI + 后台守护进程形式运行，每 2 秒扫描本机 agent 进程与会话文件，在 tmux 状态栏显示各 agent 会话数、阶段徽章（等待许可/思考/工具执行）与编号关注条目，支持 Option+1~5 直跳会话、活动日志（工具调用+token，7 天保留）与告警系统。关键机制是进程-会话文件绑定管线（Identity Resolver→File Binding→Reconciliation），以应对 /clear 换会话、同目录多会话等场景；零侵入、只读、无网络。限制：窗格跳转依赖 tmux，WezTerm/iTerm2 原生栏暂停，Gemini 权限检测受限。

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

- tmux 状态栏实时显示 Claude/Codex/Gemini 会话数、阶段徽章与关注优先级排序
- 进程-会话文件五步绑定管线，处理 /clear、同目录多会话、延迟建文件等场景
- 活动日志记录文件编辑、bash 命令与 token 用量，保留 7 天
- 零侵入：无 API key、无 agent 插件、只读且无外发网络连接

## 适用场景

- 我在 tmux 里同时开多个 AI 编码会话，想在状态栏一眼看到哪个在等授权
- 用 Option+数字快捷键直接跳转到需要关注的会话窗格
- 查看各会话今天做了哪些工具调用、消耗了多少 token

## 场景标签

 · 领域:开发工具/终端监控

## 证据(README 行号)

> L3:  tmux status bar monitor for Claude Code, Codex & Gemini — track AI coding sessions in real time
> L100: |Agent|Detection|Session Enrichment|Phase Tracking|

## 星数曲线

```mermaid
xychart-beta
    title "mjjo16/marmonitor 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-31 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `18b8461f57ed` · [字段定义](../../DATASET.md)*
