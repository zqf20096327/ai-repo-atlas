# koed-labs/koed

⭐ 15 · TypeScript · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/koed-labs/koed) · [官网](https://koed.ai/) · 组织维护

**为 Codex/Claude Code/Pi 提供本地长期记忆的代理记忆层**

Koed 是一个在后台自动捕获 AI 编码会话的记忆层，将决策、失败尝试与上下文存入本机 Postgres+pgvector，供 AI 客户端通过 MCP 工具检索；带引用来源的 memory_answer 工具、Capture Policies 与本地隐私过滤模型控制留存内容，Koed Desktop 提供浏览界面。由 Apache-2.0 许可，文档另标注 Commercial feature boundary；本版本仅单设备运行，设备配对与同步默认关闭。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 后台零操作捕获 Codex/Claude Code/Pi 会话
- memory_answer MCP 工具返回带引用的证据
- 本地运行 Postgres+pgvector，无 Docker 无云账户
- Capture Policies、Capture Pause 与本地隐私过滤模型

## 适用场景

- 让 AI 编码会话延续上次项目上下文，不用重复交代
- 团队在私有服务器部署共享代理记忆
- 按策略控制哪些会话内容被记录和脱敏

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L18: Koed ends that. It captures your AI coding sessions in the background and gives
> L23: searches it. Your AI Client writes the answers, so no extra LLM sits in the
> L37: - **Recall with receipts.** The `memory_answer` MCP tool gives your AI Client


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `ce09a75d1206` · [字段定义](../../DATASET.md)*
