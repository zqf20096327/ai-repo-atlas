# isala404/Tera

⭐ 97 · Rust · AGPL-3.0 · 推送 2026-10-03 · [GitHub](https://github.com/isala404/Tera) · 个人维护

**把 WhatsApp 变成个人 AI Agent 入口的 Rust 守护进程**

Tera 是一个 Rust 守护进程：通过 WhatsApp Rust 连接 WhatsApp Web（无需 Cloud API 或 Meta 开发者账号），将收到的每条消息作为一轮任务交给本机 Codex（常驻 codex app-server），Codex 拥有 shell、文件系统与网络，可执行磁盘清理、PR 总结等操作并通过 send_message MCP 工具回复。消息落在 SQLite 事件库，记忆为自再生的 markdown 文件，内置调度器。需要 codex CLI 登录及 git/python3/sqlite3/jq/ffmpeg 等依赖，以 cargo 编译构建。重要限制：所有 Codex 线程以 danger-full-access 且永不审批运行，主人号码检查是唯一安全边界。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | `idea` | |

## 能力要点

- WhatsApp 消息直接作为 Codex 任务在本机工作区执行（shell/文件系统/网络）
- SQLite 事件库 + JSONL 投影，Codex 用 jq/sqlite3 查询历史
- 内置调度器与 Phoenix 回滚保护的自更新机制
- 本地 Aloud Q8 语音识别/合成，可收发 WhatsApp 语音消息

## 适用场景

- 通过手机 WhatsApp 远程指挥本机电脑做清理、总结等工作
- 让常驻个人 Agent 按日程自行排队执行任务
- 用 WhatsApp 收发本地转录与语音回复

## 场景标签

`AI 助手` `语音识别` · 领域:对话与助手

## 证据(README 行号)

> L3: Tera is a Rust daemon that pairs to a WhatsApp account. Every message you send becomes a turn run by Codex against a
> L9: It connects to WhatsApp Web through WhatsApp Rust, so no Cloud API and no Meta developer account, and spawns one per

## 星数曲线

```mermaid
xychart-beta
    title "isala404/Tera 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-29"]
    y-axis "stars" 95 --> 98
    line [96, 97, 97]
```

2026-10-18 96 → 2026-10-29 97（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `3ab1e2e962ae` · [字段定义](../../DATASET.md)*
