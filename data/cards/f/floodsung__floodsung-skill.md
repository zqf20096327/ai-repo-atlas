# floodsung/floodsung-skill

⭐ 25 · Python · NOASSERTION · 推送 2026-04-21 · [GitHub](https://github.com/floodsung/floodsung-skill) · 个人维护 · 中文 README

**开源作者知乎语料训练的 Claude Code 人格分身 skill，可 fork 换成自己的语料**

一个 Claude Code skill：安装后 Claude 以 Flood Sung（XVI Robotics 创始人）的身份思考、写作、回答，可生成知乎风格文章、短想法、代答提问与技术观点。核心机制为 SKILL.md 人设 prompt 加 references 目录（风格样本、观点索引、术语词典等），底层语料为全量知乎内容 566 条约 90 万字（另含原始数据与爬虫脚本，爬取需登录 cookie）。同时定位为模板：fork 后替换语料即可生成个人分身 skill。限制：语料与爬取依赖知乎账号 cookie，许可仅声明 scripts 为 MIT。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SKILL.md 人设 prompt + 蒸馏出的风格样本/观点索引/术语词典等 references
- 566 条知乎原始语料（152 文章 + 236 回答 + 178 想法，约 90 万字）随 repo 开源
- 附知乎爬虫与分析工具，可 fork 替换为自己的语料生成个人 skill
- 支持四类输出：知乎文章、短想法、代答提问、技术观点 take

## 适用场景

- 让 Claude Code 以 Flood Sung 的风格与观点写作、回答问题
- fork 模板并用自己的语料制作个人数字分身 skill
- 爬取并分析自己的知乎全量创作内容

## 场景标签

`AI 写作` `网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L3: > **开源我自己** — An open-source Claude Code skill that lets any model speak, think, and write as **Flood Sung** (XVI Ro
> L9: 一个 **Claude Code skill**。触发后，Claude 不再是通用助手，而是以 **Flood Sung** 的身份思考、写作、回答。包含：
> L53: ## Skill 能做什么

## 星数曲线

```mermaid
xychart-beta
    title "floodsung/floodsung-skill 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-27"]
    y-axis "stars" 23 --> 26
    line [24, 25, 25]
```

2026-10-18 24 → 2026-10-27 25（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `a14daceebad0` · [字段定义](../../DATASET.md)*
