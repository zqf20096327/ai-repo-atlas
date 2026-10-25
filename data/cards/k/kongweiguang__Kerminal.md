# kongweiguang/Kerminal

⭐ 33 · TypeScript · GPL-3.0 · 推送 2026-10-23 · [GitHub](https://github.com/kongweiguang/Kerminal) · 个人维护 · 中文 README

**带 AI Agent 集成的本地与远程终端运维桌面工作台**

基于 Tauri 2 的桌面终端与远程运维工作台，面向开发与运维人员：统一 Local/SSH/SFTP/RDP/Telnet/Serial 连接、多 Tab 分屏终端、SFTP 双面板传输与远程文本编辑、SSH 主机上的 Docker/Podman/Compose 管理、tmux、SSH 隧道与服务器监控（含 GPU/NPU 视图）。AI 部分为 Agent Launcher：可启动 Codex、Claude、PI Agent 与自定义 CLI，并通过仅监听回环地址的 Kerminal MCP 向 Agent 暴露终端、文件、容器等运行态工具；审批与审计由 MCP host 负责。GPL-3.0-or-later 授权，提供三平台安装包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 内置 Agent Launcher 支持 Codex、Claude、PI Agent 与自定义 CLI
- Kerminal MCP（loopback Streamable HTTP）暴露终端、SFTP、容器、tmux、端口转发等运行态工具
- SFTP 双面板传输：队列、断点续传、冲突策略与远程文件编辑（revision 校验）
- SSH 主机上管理 Docker/Podman/Compose，含容器内文件操作与 GPU/NPU 监控视图

## 适用场景

- 在一个工作台内管理本机与多台远程服务器的终端、文件与容器运维
- 让 Codex/Claude 等 Agent 通过 MCP 直接操作终端与基础设施执行任务
- 跨主机传输文件与编排 SSH 隧道、tmux 会话
- 多 Pane 批量向多台服务器发送命令并集中确认当前目标

## 场景标签

 · 领域:开发运维工具/终端

## 证据(README 行号)

> L17: Kerminal 是一个本地优先的桌面终端和远程运维工作台。它围绕“当前目标”组织本机与远程终端、SFTP、Docker/Podman、Compose、tmux、SSH 隧道、服务器监控和 Agent 会话，让开发、排障和交付不必
> L19: 内置 Agent Launcher 支持 Codex、Claude、PI Agent 和可持久化的自定义 CLI。每个终端 Tab 都有独立的右栏助手与历史；每个 Agent 会话都有独立工作目录，仍可通过 Kerminal MC
> L33: |MCP|本机 loopback Streamable HTTP；提供终端、SSH/SFTP、容器与容器文件、tmux、端口转发、服务器信息、历史和诊断等运行态工具。|

## 星数曲线

```mermaid
xychart-beta
    title "kongweiguang/Kerminal 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-25"]
    y-axis "stars" 31 --> 34
    line [32, 33, 33]
```

2026-10-18 32 → 2026-10-25 33（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `18cedf92ad7a` · [字段定义](../../DATASET.md)*
