# cross-entropy-ai/deck

⭐ 15 · Rust · 推送 2026-09-13 · [GitHub](https://github.com/cross-entropy-ai/deck) · 组织维护

**在终端内管理 tmux 会话与 AI agent 会话的侧边栏工具**

用 Rust/ratatui 编写的 tmux 增强工具：在终端中以侧边栏列出 tmux 会话，支持点击切换、拖拽排序、右键重命名/关闭。面向在 tmux 中运行编码 agent 的开发者，提供跨会话 agent 摘要（可选 Claude Code 或 Codex CLI 生成）、容器会话通道（docker/podman/Apple container）、SSH 远程主机管理与 ssh-agent 转发、iPad 远程控制（Deck Buddy）。运行前置条件是本机安装 tmux；不负责安装配置 tmux 或接入 agent 本身。通过 brew、curl 脚本或 GitHub Releases 预编译二进制安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 侧边栏列出并操作 tmux 会话，主窗格跟随焦点会话
- Agents 标签可用 Claude Code 或 Codex 生成跨会话摘要
- 支持 docker/podman/container 容器通道与 SSH 远程主机（复用单连接、默认转发 ssh-agent）
- Deck Buddy iPad 应用可远程控制并读取侧边栏状态（macOS）

## 适用场景

- 同时跑多个 AI 编码 agent 时快速浏览与切换会话
- 在本地与远程主机/容器中统一管理 tmux 会话
- 用 iPad 作为 Mac 上 deck 的键盘触控板并遥控会话切换

## 场景标签

 · 领域:开发者工具/终端

## 证据(README 行号)

> L18: `deck` is a tmux enhancement tool — the sidebar lists your sessions and agents.
> L58: The Agents tab can generate a cross-session summary with either Claude Code or Codex; choose the CLI under **Settin

## 星数曲线

```mermaid
xychart-beta
    title "cross-entropy-ai/deck 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `203d105e1352` · [字段定义](../../DATASET.md)*
