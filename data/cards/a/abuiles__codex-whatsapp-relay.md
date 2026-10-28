# abuiles/codex-whatsapp-relay

⭐ 46 · JavaScript · 推送 2026-03-31 · [GitHub](https://github.com/abuiles/codex-whatsapp-relay) · 个人维护

**把 Codex 接入 WhatsApp 的插件：手机扫码聊天控制 Codex**

Codex 插件，通过一次 QR 扫描将本地 WhatsApp 账号接入 Codex：Codex 经 MCP 工具读取聊天/缓存消息/同步历史并发送回复；也可将指定 WhatsApp 直聊变为轻量 Codex 客户端。底层使用 codex app-server，手机控制映射到可 codex resume 的原生线程。支持多项目切换（/project、/in、/btw）、会话管理、权限审批、语音笔记（本地 mlx parakeet 转写，需 uvx 与 ffmpeg）、本地语音回复。限制：每个项目别名同时只允许一个在途 Codex 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- QR 一次扫描绑定 WhatsApp，Codex 经 MCP 工具读写消息
- 基于 codex app-server 的原生线程，可终端 codex resume 续接
- 一个聊天内多项目/多会话切换与权限审批命令
- 语音笔记本地转写（mlx-community/parakeet-tdt-0.6b-v3）与本地语音回复

## 适用场景

- 在手机 WhatsApp 里继续或新开 Codex 工作会话
- 同时推进多个代码项目并在审批请求到达时远程批准或拒绝
- 用语音笔记驱动 Codex 并收到语音回复

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L5: WhatsApp Relay is a Codex plugin that links a local WhatsApp account to Codex, lets Codex read and send WhatsApp mes
> L53: 2. Codex can inspect chats, read cached messages, sync history, and send replies through MCP tools.

## 星数曲线

```mermaid
xychart-beta
    title "abuiles/codex-whatsapp-relay 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 45 --> 47
    line [46, 46]
```

2026-10-18 46 → 2026-10-28 46（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `0043e1248b6b` · [字段定义](../../DATASET.md)*
