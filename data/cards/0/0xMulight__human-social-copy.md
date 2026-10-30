# 0xMulight/human-social-copy

⭐ 23 · MIT · 推送 2026-08-03 · [GitHub](https://github.com/0xMulight/human-social-copy) · 个人维护 · 中文 README

**让 AI Agent 写出真人风格中文社交文案的规则库**

一套中文社交媒体文案写作规则库，供 Hermes、Claude Code、Codex、Gemini 等任意 AI Agent 加载使用。规则分三层：通用表达规则（去AI味、14个禁用词、禁用句式、中文排版规范）、内容场景规则（金融写作、图文排版、选题、合作brief）与个人语气系统（内置0xMulight语气画像，也可通过采集Prompt为其他人建立画像）。以 Git 仓库形式提供，Agent 按类型读取 SKILL.md/CLAUDE.md/AGENTS.md 等入口文件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三层规则：通用表达、内容场景（金融/图文/选题/brief）、个人语气画像
- 14个禁用词与禁用句式清单，去AI味
- 支持 Hermes/Claude Code/Codex/Gemini 及任意 Agent 的适配入口文件
- 提供 voice-capture-prompt 为其他作者采集个人语气画像

## 适用场景

- 让 AI 写出的推文、图文更像真人分享而非AI八股
- 为美股、宏观、财报、crypto 内容套用专门的金融写作规则
- 为自己的社交账号建立个人语气画像并让 Agent 沿用

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L14: 一套中文社交媒体文案规则库。你可以把它交给Hermes、Claude Code、Codex、Gemini或任何AI Agent，让AI写出的内容更像真人分享。
> L20: 1. 通用表达规则：去AI味、去套话、保留具体信息。

## 星数曲线

```mermaid
xychart-beta
    title "0xMulight/human-social-copy 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-30 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `fc5e55bbb779` · [字段定义](../../DATASET.md)*
