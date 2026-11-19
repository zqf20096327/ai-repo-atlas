# samestrin/llm-newsletter-generator

⭐ 15 · Python · MIT · 推送 2026-11-17 · [GitHub](https://github.com/samestrin/llm-newsletter-generator) · 个人维护

**用 LLM 从 RSS/Atom 源生成带事实核查的 Newsletter**

Python 包：读取 RSS/Atom 订阅源（也可配网页和 Hacker News），用嵌入模型按主题分组排序报道，快速模型为每条报道提取引用原文的声明，逐条与原文核对，不被支持的声明保留并标记为 flagged；推理模型仅基于已支持声明编辑成刊（头条、主题、导语），可选 yourvoice.dev 改写为作者文风。产出 Markdown、HTML 邮件、运行报告与人工审阅页，任一失败或 flag 则退出码为 1。通过环境变量接入任意 OpenAI 兼容端点，另有 HTTP API 与 Docker 部署方式。限制：跨订阅源分组为后续工作，archive 命令仅有 demo 模式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 声明级事实核查：不被原文支持的声明标记为 flagged，绝不静默丢弃或通过
- 嵌入模型按主题对报道分组与排序，重复报道合并并保留全部来源
- 输出 Markdown/HTML 邮件 + 运行报告（失败源、flagged 声明、每次模型调用的 token 与成本）
- 人工审阅页：编辑即清除批准；任何失败或 flag 导致退出码 1

## 适用场景

- 我希望自动从 RSS 源起草 Newsletter 草稿，再人工审改后发布
- 为 AI 周刊类栏目生成带来源引用、可核查声明的邮件
- 以作者本人文风改写导语与评论（需 yourvoice.dev key）

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L7: **llm-newsletter-generator** is a Python package that generates text-only newsletters from RSS feeds using LLMs. See
> L13: 1. The fast model writes claims for each story, each one quoting the passage it came from.
> L15: 3. The reasoning model edits the issue (lead story, themes, intro, why each story matters) and may cite only suppor

## 星数曲线

```mermaid
xychart-beta
    title "samestrin/llm-newsletter-generator 星数(近 2 点)"
    x-axis ["2026-11-02", "2026-11-19"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-11-02 15 → 2026-11-19 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 mid · 依据 README sha `f52500a3af7b` · [字段定义](../../DATASET.md)*
