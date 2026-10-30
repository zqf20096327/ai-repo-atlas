# TheStack-ai/mrstack

⭐ 16 · Python · MIT · 推送 2026-06-30 · [GitHub](https://github.com/TheStack-ai/mrstack) · [官网](https://pypi.org/project/mrstack/) · 组织维护

**通过 Telegram 24/7 运行 Claude Code 的本地 AI 开发助手守护进程**

在用户本机（macOS/Linux）注册为系统守护进程，将 Claude Code 接入 Telegram：用户通过消息下达编码、调试、学习文档等指令，Bot 处理文本、照片、语音并回复。内置每 3 小时分析对话生成永久记忆（SQLite/JSONL/Markdown 本地存储）、macOS 上每 5 分钟扫描系统状态的 Jarvis 主动提醒模式、定时任务（早报/晚总结/GitHub 通知）与 MCP 可选集成（Google Calendar/Notion/GitHub/Playwright）。数据本地存储，仅 Claude API 调用经由 Anthropic。需 Python 3.11+、Telegram Bot Token 与 Claude Code 订阅（推荐 Max 套餐），Windows 支持标注为准备中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- mrstack daemon 注册系统守护进程，终端关闭后 24 小时运行
- 每 3 小时分析对话生成永久记忆（人员/项目/偏好）
- Jarvis 模式：macOS 每 5 分钟扫描系统状态并主动提醒
- 模型路由（Haiku/Sonnet/Opus）与危险命令预拦截

## 适用场景

- 出门在外通过 Telegram 让 Claude Code 继续写代码、改代码
- 把链接和文档发给 Bot 让其学习，之后提问检索
- 让 Bot 定时推送早报、日程提醒和每日编程复盘

## 场景标签

`编码 Agent` `AI 助手` · 领域:编码与开发

## 证据(README 行号)

> L42: Claude Code를 **텔레그램으로 확장**한 24시간 AI 파트너입니다.
> L320: |AI 엔진|Claude Code SDK (Opus / Sonnet / Haiku)|

## 星数曲线

```mermaid
xychart-beta
    title "TheStack-ai/mrstack 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `3a32d1b6a7a9` · [字段定义](../../DATASET.md)*
