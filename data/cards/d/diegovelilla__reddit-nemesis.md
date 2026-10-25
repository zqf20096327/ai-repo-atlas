# diegovelilla/reddit-nemesis

⭐ 54 · Python · Apache-2.0 · 推送 2026-01-22 · [GitHub](https://github.com/diegovelilla/reddit-nemesis) · 个人维护

**AI 驱动的 Reddit 反驳评论机器人：抓帖并逐点反对**

Reddit-Nemesis 是一个 Python 编写的 Reddit 机器人：抓取指定 subreddit 的帖子，借助 LLM（Llama 3.1 70B，经 Groq API 调用）生成逐点反驳原帖内容的伪友好评论并自动发布。配置项包括 Groq、Reddit、Serper 等 API key；不填 Reddit 账号密码时可仅运行抓取不发言。README 带有内容风险警告，提示生成文本可能不当，需使用者自行审核。作者称其为另一问答项目 reddit-omni 的反向版本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 抓取 subreddit 帖子并生成逐点反驳评论
- 通过 Groq API 调用 Llama 3.1 70B 生成文本
- 不配置 Reddit 账号时可仅运行抓取不留言

## 适用场景

- 在 subreddit 内自动发布反驳评论引发讨论
- 测试 LLM 生成对抗性评论的效果

## 场景标签

 · 领域:社交平台自动化/LLM 应用

## 证据(README 行号)

> L22: Reddit-Nemesis is an AI-powered Reddit bot that scrapes through subreddits, finds posts, and leaves pseudo-friendly
> L57: - Llama 3.1 70B - Groq.

## 星数曲线

```mermaid
xychart-beta
    title "diegovelilla/reddit-nemesis 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 53 --> 55
    line [54, 54]
```

2026-10-18 54 → 2026-10-25 54（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `39f40f192ef6` · [字段定义](../../DATASET.md)*
