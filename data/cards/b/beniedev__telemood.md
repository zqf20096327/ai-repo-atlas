# beniedev/telemood

⭐ 23 · Python · MIT · 推送 2026-10-12 · [GitHub](https://github.com/beniedev/telemood) · 个人维护 · 中文 README

**让模型驱动的 Telegram 机器人发出有序富回复的 Python 库**

一个零第三方运行时依赖的 Python 库（>=3.11），面向已有自建 Telegram bot 的开发者：把模型生成的回复计划解析为有序执行的文本气泡、emoji 回应、常规贴纸与一次性选择按钮，通过宿主已有的 Telegram 客户端同步或异步发送，并逐项记录执行结果。安全机制上，模型不可选择聊天、凭据或 file_id，未知输入 fail closed；提供可选的入站消息合并纯策略（无时钟、无 I/O）。v0.1 不运行第二个 bot 循环、不管理部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 模型回复计划 → 有序气泡/回应/贴纸/选择按钮的受控执行
- 逻辑贴纸目录 ID 隔离 Telegram file_id，宿主绑定可信上下文
- 同步/异步双路径，任意动作非 VERIFIED 即停止后续执行
- 纯策略的入站连续消息合并（默认 2.5s/4.5s/8.0s 阈值）

## 适用场景

- 已有 Telegram bot 想让模型输出更结构化、多形式的回复
- 需要限制模型权限、由宿主掌握令牌与路由的可控执行层
- 把用户连发的多条消息合并为一个逻辑轮次再交给模型

## 场景标签

 · 领域:聊天机器人/AI Agent 基础组件

## 证据(README 行号)

> L63: **What is Telemood?** A small Python library that turns model-generated plans into richer Telegram replies.
> L7: A model can combine text bubbles, emoji reactions, regular stickers, and tappable choices in one reply. Telemood sen

## 星数曲线

```mermaid
xychart-beta
    title "beniedev/telemood 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-27 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `a48aa8d27d39` · [字段定义](../../DATASET.md)*
