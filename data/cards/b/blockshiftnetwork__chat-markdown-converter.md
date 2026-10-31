# blockshiftnetwork/chat-markdown-converter

⭐ 13 · PHP · MIT · 推送 2026-07-20 · [GitHub](https://github.com/blockshiftnetwork/chat-markdown-converter) · 组织维护

**将 LLM 生成的 Markdown 转为五大聊天平台格式的 PHP 库**

PHP 库（Composer 包），通过中间表示（IR）架构把 ChatGPT、Claude 等模型输出的 Markdown 转换为 Telegram HTML、WhatsApp 文本、Discord/Slack markdown 及 Instagram Unicode 格式。先解析为 IR 再由各平台渲染器输出，处理代码块、表格、任务列表、链接等；含智能消息分块（按平台长度上限拆分）、零外部依赖、206 个通过的测试，支持自定义渲染器与 Laravel 集成。限制：表格在不支持的平台转为列表；Instagram 渲染对屏幕阅读器不友好（README 有无障碍说明）。

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

- IR 架构：Markdown→Parser→IR→Renderer，便于扩展新平台
- 覆盖 Telegram/WhatsApp/Discord/Slack/Instagram 五个平台的格式规则
- 智能消息分块，按各平台最大长度在安全断点拆分
- 零外部依赖，206 个测试通过，支持自定义渲染器

## 适用场景

- 把 LLM API 回复格式化后发送到用户所在的聊天平台
- 在 Laravel 通知/队列任务中投递 AI 生成的 Markdown 内容
- 一份 Markdown 内容同时分发到多个聊天平台

## 场景标签

 · 领域:开发库/LLM 输出格式化

## 证据(README 行号)

> L9: Convert AI-generated Markdown to WhatsApp, Telegram, Discord, Slack and Instagram formats using an Intermediate Repr
> L11: This PHP library transforms ChatGPT, Claude, GPT-5, and other AI model outputs into platform-specific markup. It ha
> L270: Markdown → Parser → IR → Renderer → Platform-Specific Format

## 星数曲线

```mermaid
xychart-beta
    title "blockshiftnetwork/chat-markdown-converter 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `7cc4779fc44e` · [字段定义](../../DATASET.md)*
