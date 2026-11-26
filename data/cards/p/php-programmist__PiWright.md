# php-programmist/PiWright

⭐ 9 · TypeScript · MIT · 推送 2026-11-25 · [GitHub](https://github.com/php-programmist/PiWright) · 个人维护 · 中文 README

**pi coding agent 的开源 Windows 桌面 GUI，整合聊天/看板/Git/编辑器**

基于 Electron + React 的原生 Windows 桌面应用，为 pi coding agent 提供类 IDE 工作区：RPC 流式聊天、agent 驱动的看板（agent 自主领任务、移动卡片并评论汇报）、PHPStorm 风格 git 分支图、Monaco 编辑器与 node-pty 终端。支持原生与 WSL 双 pi 后端、SSH 远程后端、MCP 服务器管理、Telegram 通知以及手机 PIN 认证的远程 Web UI。依赖 Windows 10/11、Node.js ≥22.19、Git 与 pi CLI；单个维护者，MIT 许可。

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

- agent 驱动看板：agent 领取任务、移动卡片并通过评论汇报
- 会话 fork/rewind：回滚到任意回答并从快照恢复工作目录
- 原生 Windows 与 WSL 双 pi 后端，另有 SSH 远程后端
- 手机远程 Web UI（WebSocket 桥 + PIN 认证）与 Telegram 通知

## 适用场景

- 在单一窗口内与编码 agent 协作完成开发任务
- 用看板让 agent 自主推进多任务工作流
- 通过手机远程查看和操控本地 agent 会话

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L7: **PiWright** is an open-source desktop GUI for the pi coding agent — a native Windows app (Electron + React) that tu
> L80: ### Models, MCP and skills


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `5396d48ab800` · [字段定义](../../DATASET.md)*
