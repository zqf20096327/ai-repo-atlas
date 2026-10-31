# yohasebe/tmux-ccm

⭐ 16 · Python · MIT · 推送 2026-10-30 · [GitHub](https://github.com/yohasebe/tmux-ccm) · 个人维护

**管理多项目并行 Claude Code 会话的 tmux 注意力管理插件**

面向同时运行多个 Claude Code 会话的开发者的 tmux 插件：每个项目对应一个 tmux 窗口，实时检测各 Claude Code 面板状态（BUSY/IDLE/PERMIT）并聚合到窗口级；弹窗式仪表盘按紧急度排序，一键跳转至最需处理的项目。提供树状视图、git 分支与端口显示、快照恢复、跨项目消息投递（PERMIT 状态安全门控与忙时排队）、空闲会话 10 分钟自动退出释放资源、桌面通知与状态栏注入。要求 tmux 3.2+、Python 3.9+、jq、fzf 及 Claude Code v2.1.107+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 实时检测 Claude Code 面板状态（BUSY/IDLE/PERMIT）并聚合到项目窗口
- 仪表盘按紧急度排序，prefix+Tab 一键跳转最需处理的项目
- 跨项目消息投递 `ccm send`，带 PERMIT 安全门控与忙时排队
- 空闲 Claude 会话 10 分钟自动退出释放内存/CPU，切回时自动重启恢复

## 适用场景

- 我在多个项目里并行跑 Claude Code，想一眼看清哪个在等授权、哪个已完成
- 并行 agent 作业时按紧急度跳转处理，减少窗口间来回切换
- 在项目间传递提示词且避免打断正在忙的会话

## 场景标签

 · 领域:开发者工具/终端会话管理

## 证据(README 行号)

> L7: ccm is a tmux plugin for developers who run Claude Code across several projects at once. Each Claude session becomes
> L9: It's effectively an **attention manager**: every project gets a state (BUSY / IDLE / waiting for permission), the da
> L27: - **Resource Management** — Idle Claude Code sessions auto-exit after 10 minutes to free memory and CPU; auto-resta

## 星数曲线

```mermaid
xychart-beta
    title "yohasebe/tmux-ccm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `3214097378b3` · [字段定义](../../DATASET.md)*
