# smixs/agent-second-brain

⭐ 410 · Python · MIT · 推送 2026-08-05 · [GitHub](https://github.com/smixs/agent-second-brain) · [官网](https://t.me/aimastersme) · 个人维护

**常驻 Telegram 语音助手：把语音/消息整理进 Obsidian 知识库**

面向个人用户的第二大脑系统：通过 Telegram 发送语音、文字、照片与文档，运行在自有 VPS 上的 bot 驱动一个长驻的交互式 Claude Code 会话（tmux），将内容分类为带类型和 wiki 链接的 markdown 卡片写入用户自己的 Obsidian vault。内置 autograph 记忆引擎，实现 Ebbinghaus 遗忘曲线、五层级衰减与 MOC 索引。语音经 Deepgram 转录，文本经 Claude 订阅处理，vault 数据留在本机。以 bootstrap 脚本一键安装到 Ubuntu VPS，配置 systemd 服务常驻运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 语音/文字/文件经 Telegram 捕获并自动写入 Obsidian vault
- autograph 记忆引擎：类型化卡片、Ebbinghaus 五层衰减、MOC 索引、健康评分
- 单一长驻交互式 Claude Code 会话运行于订阅额度，CI 禁止 headless 调用
- watchdog 自愈与每日 🟢/🔴 健康报告，代理可从自然语言自建 cron 任务

## 适用场景

- 走路时随手发语音，晚上自动整理成知识卡片
- 随时向 bot 询问过去记录的内容并获得带链接引用的回答
- 让代理定时提醒、整理收件箱并生成每日报告

## 场景标签

`AI 助手` `知识库管理` · 领域:对话与助手

## 证据(README 行号)

> L6: Voice note in Telegram → typed, linked knowledge in your Obsidian vault.
> L104: Telegram ──▶ bot (aiogram) ──▶ persistent Claude Code session (tmux pane)
> L76:  🎙 Total capture Voice (Deepgram, seconds), text, photos, documents, videos, forwarded posts, whole albums — the ag

## 星数曲线

```mermaid
xychart-beta
    title "smixs/agent-second-brain 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-24"]
    y-axis "stars" 404 --> 411
    line [405, 409, 410]
```

2026-10-18 405 → 2026-10-24 410（+5）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `db391ac97444` · [字段定义](../../DATASET.md)*
