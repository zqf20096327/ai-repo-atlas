# atukunare/wiki-knowledge-agent

⭐ 19 · Python · MIT · 推送 2026-08-31 · [GitHub](https://github.com/atukunare/wiki-knowledge-agent) · 个人维护 · 中文 README

**把聊天中的链接/文本转成可检索 wiki 知识库的 agent 技能**

面向 Claude Code、Codex、Cursor、Hermes 等 AI agent 的技能包（SKILL.md + Python 脚本）：对聊天中粘贴的链接先做 HTTP 验证与广告/有用内容分类，再由 LLM 翻译摘要成目标语言，存入本地 wiki 目录作为可持续检索的知识库，时效性内容进入本地告警队列。零外部依赖，仅需 curl 与 Python 3.9+ 标准库，git clone 后复制技能文件夹即可用；配置位于 ~/.config 下的 YAML。

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

- 链接到达即验证（HTTP 状态/重定向）并区分广告与有用内容
- LLM 翻译+摘要后存为 wiki 蒸馏笔记，支持 RAG 检索与 knowledge-base-map 快速索引
- 时效性条目进入本地告警队列，可后续接 Slack/Discord/Telegram/ntfy
- 零外部依赖（curl + Python stdlib），平台无关，附各 agent 的技能目录安装说明

## 适用场景

- 让 Claude Code/Codex/Cursor 等 agent 记住聊天中粘贴的链接和文本
- 把零散资料整理成可检索、已翻译的个人 wiki 知识库
- 跟踪安全通告、到期日等时效性信息并接收提醒

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L9: > **Wiki Knowledge Agent** turns chat-pasted text and links into a **verified, translated, searchable** wiki knowled
> L80: The model follows SKILL.md: verify → classify → pre-save feedback → translate/summarize → save → maybe alert.

## 星数曲线

```mermaid
xychart-beta
    title "atukunare/wiki-knowledge-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `0db2a8f292be` · [字段定义](../../DATASET.md)*
