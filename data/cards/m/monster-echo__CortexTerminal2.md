# monster-echo/CortexTerminal2

⭐ 35 · C# · 推送 2026-10-25 · [GitHub](https://github.com/monster-echo/CortexTerminal2) · [官网](https://corterm.rwecho.top) · 个人维护 · 中文 README

**手机/浏览器远程连接服务器终端、追踪 AI Agent 的终端平台**

Corterm 是由 Gateway、Worker、Console 三部分组成的远程终端平台：在目标机器安装轻量 Worker 管理 PTY 会话，部署中央 Gateway 处理认证与会话路由，用户经浏览器或 iOS/Android/HarmonyOS 客户端接入；shell 在关闭页面后继续运行，重连时回放输出。面向在服务器上运行 Claude Code 等 AI Coding Agent 的用户，通过 hooks 将 Agent 的提示、工具调用与通知渲染为时间线供监控。另含文件传输（S3 兼容存储中转）、资源监控、多 Worker 管理与多因素认证。浏览器 Console 组件已声明停止维护。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 会话持久化：shell 在关闭页面后继续运行，重连回放输出
- Claude Code hooks 上报提示/工具调用/通知，渲染为结构化时间线监控 Agent
- Worker 支持 Linux amd64/arm64、macOS Apple Silicon、Windows x64 与 Docker
- 基于 S3 兼容存储的双向文件传输，Worker 不持有 S3 凭证

## 适用场景

- 在手机上连接服务器，继续操作 Claude Code 等终端 AI Agent 任务
- 多台远程机器的终端统一接入与管理
- 移动端查看与下载服务器工作目录中的文件产物

## 场景标签

 · 领域:远程终端/开发工具

## 证据(README 行号)

> L11: Corterm is a remote terminal platform. Install a lightweight Worker on any machine, deploy the Gateway, and access 
> L34: - **AI Agent Tracking** -- Watch Claude Code work in real time. Claude Code hooks report every prompt, tool call, a

## 星数曲线

```mermaid
xychart-beta
    title "monster-echo/CortexTerminal2 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-27 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `f87e2c54ed72` · [字段定义](../../DATASET.md)*
