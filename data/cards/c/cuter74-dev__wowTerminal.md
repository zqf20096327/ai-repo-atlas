# cuter74-dev/wowTerminal

⭐ 14 · TypeScript · MIT · 推送 2026-10-30 · [GitHub](https://github.com/cuter74-dev/wowTerminal) · [官网](https://wowterminal.oopnwow.com/) · 个人维护

**带 AI 助手的 SSH/SFTP 终端桌面应用**

基于 Tauri 2 + Rust + React + xterm.js 的桌面终端应用，功能包括：PTY 本地终端（标签页、分屏、标签独立成窗）、SSH 主机管理（配置档案/分组/标签、密钥管理、TOFU 主机密钥校验）、双栏 SFTP 文件浏览与传输队列、tmux 集成与会话恢复。AI 部分为多后端聊天助手，兼容任意 OpenAI 兼容端点（OpenAI/Ollama/vLLM/TGI 等），可感知系统上下文并附终端输出，把回答中的命令提取为卡片一键发送到终端。从源码构建需 Rust 与 Node.js 20+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AI 助手兼容任意 OpenAI 兼容端点（OpenAI/Ollama/vLLM/TGI/自托管网关）
- SSH 主机管理：密钥管理、TOFU 主机密钥校验、密码存入系统钥匙串
- 双栏本地↔远程 SFTP 浏览、传输队列与远程文件搜索
- 会话恢复：重启后重开标签布局、SSH 重连、tmux 面板重挂载

## 适用场景

- 在同一应用里管理 SSH 主机并打开远程终端会话
- 在本地与远程之间用 SFTP 双栏传输文件
- 让 AI 助手根据当前终端输出给出命令并一键执行
- 断线后原地重连并自动回到 tmux 会话

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L19: A context-aware AI terminal — a chat assistant that reads your terminal,
> L28: - **AI assistant (multi-backend)**

## 星数曲线

```mermaid
xychart-beta
    title "cuter74-dev/wowTerminal 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `6ae28983787b` · [字段定义](../../DATASET.md)*
