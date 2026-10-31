# tzongen5168/telegram-to-obsidian

⭐ 14 · Shell · MIT · 推送 2026-03-28 · [GitHub](https://github.com/tzongen5168/telegram-to-obsidian) · 个人维护 · 中文 README

**通过 Telegram 把内容经 AI 整理后存入 Obsidian 的个人知识库工具**

面向个人知识管理用户的 Telegram bot 工作流：将文章、链接、笔记等发送给 bot 并附口令，AI 自动生成摘要、标签与分类，以结构化 markdown 按 PARA 结构写入本地 Obsidian vault，并支持通过对话检索已存笔记。基于 OpenClaw agent 框架与 OpenRouter（默认 Gemini Flash 免费额度，可换 Claude Sonnet 等付费模型或 14B 以上本地模型）运行，通过 Docker 部署在自己的 Mac/Linux 机器，数据留在本地。限制：小模型（7B）无法可靠执行工具调用；免费模型分类与摘要稳定性有限。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AI 自动生成摘要、标签并按 PARA 结构分类写入 Obsidian
- 支持文章、URL、YouTube、推文、书摘、会议纪要等多类内容
- 通过对话检索 vault 中已保存的笔记
- Docker 本地部署，模型可经 OpenRouter 切换（免费/付费/本地 14B+）

## 适用场景

- 手机上看到好文章随时发给 bot 存入 Obsidian
- 自动整理零散的灵感、书摘和会议记录并分类
- 事后用自然语言向 bot 查询已保存的笔记

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L12:   → AI processes it (summarize, tag, categorize)
> L43: - **AI-powered**: Auto-generates summary, tags, and category — not just raw copy-paste
> L55: │  Telegram    │────>│  OpenClaw    │────>│  OpenRouter  │────>│  Obsidian    │

## 星数曲线

```mermaid
xychart-beta
    title "tzongen5168/telegram-to-obsidian 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `f00871c22471` · [字段定义](../../DATASET.md)*
