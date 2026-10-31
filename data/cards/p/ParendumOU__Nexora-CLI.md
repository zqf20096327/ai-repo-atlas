# ParendumOU/Nexora-CLI

⭐ 14 · Go · MIT · 推送 2026-09-01 · [GitHub](https://github.com/ParendumOU/Nexora-CLI) · [官网](https://nexora.parendum.com) · 组织维护

**Nexora AI-agent 平台的终端客户端（Go/Bubble Tea TUI）**

面向 Nexora / NexoraCloud 的终端客户端：以单个静态 Go 二进制提供流式聊天、agents CRUD、providers、知识库、看板、issues、日程与 marketplace 等与 Web 前端对等的全量功能，通过 REST 与 WebSocket 连接任意实例。Agent 的 shell/文件工具在 CLI 所在主机本地执行（带确认提示，--yolo 可自动批准），令牌存于 config.toml 并自动刷新。由 Parendum OÜ 以 MIT 许可发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单个静态二进制，零运行时依赖，覆盖 Web UI 全部功能
- 本地工具执行带同意提示，支持 --yolo 自动批准
- 通过 REST + WebSocket 连接任意 Nexora 实例，可多实例切换
- 一键安装脚本（Linux/macOS/Windows）与 nexora update 自更新

## 适用场景

- 在终端中与 Nexora 平台的 agent 对话并观看任务流
- 无需 Node/Python/Docker 环境远程管理 agents、知识库与看板
- 团队成员通过邀请令牌快速加入组织并配对终端

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L5: **Terminal client for Nexora** — chat with your
> L20:  Nexora — AI-agent orchestration platform (click to watch the full demo)
> L25: > Status: **full frontend parity** — auth, streaming chat, agents CRUD, providers, knowledge

## 星数曲线

```mermaid
xychart-beta
    title "ParendumOU/Nexora-CLI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `49925189e673` · [字段定义](../../DATASET.md)*
