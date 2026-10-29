# sinaptik-ai/starpod

⭐ 79 · Rust · MIT · 推送 2026-04-08 · [GitHub](https://github.com/sinaptik-ai/starpod) · [官网](https://starpod.sh) · 组织维护

**Rust 编写的个人 AI agent 运行时，本地或云端部署**

用 Rust 构建的开源 AI agent 运行时：通过 starpod init 在任意目录引导一个 agent，每个 agent 自带内存（markdown + SQLite FTS5）、AES-256-GCM 加密 vault、文件沙盒与会话，全部自包含于 .starpod/ 目录。支持 Web UI、Telegram、CLI、HTTP API 与 WebSocket 流式等多通道接入，agent 可在运行时创建/编辑自己的技能文件，并具备 cron 调度能力。需 Rust 1.87+，提供安装脚本、Homebrew 与 cargo 安装方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- starpod init 一条命令引导自包含 agent（.starpod/ 目录）
- 多通道接入：Web UI、Telegram、CLI、HTTP API、WebSocket 流式
- 持久化内存（markdown + SQLite FTS5）与 AES-256-GCM 加密 vault
- agent 运行时自扩展技能与 cron 调度

## 适用场景

- 部署一个带记忆和个人 vault 的私人 AI 助手
- 通过 Telegram 或 Web UI 与同一 agent 对话
- 定时执行完整 agent 循环的 cron 任务

## 场景标签

`AI 助手` `Agent 记忆` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L15: Starpod is an open-source AI agent runtime built in Rust. Bootstrap an agent in any directory with `starpod init`, 
> L79: ├── agent-sdk/            Claude API client + agent loop

## 星数曲线

```mermaid
xychart-beta
    title "sinaptik-ai/starpod 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 78 --> 80
    line [79, 79]
```

2026-10-18 79 → 2026-10-29 79（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `a31b6d87f217` · [字段定义](../../DATASET.md)*
