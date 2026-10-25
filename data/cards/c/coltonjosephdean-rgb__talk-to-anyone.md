# coltonjosephdean-rgb/talk-to-anyone

⭐ 67 · Python · MIT · 推送 2026-07-07 · [GitHub](https://github.com/coltonjosephdean-rgb/talk-to-anyone) · 个人维护

**Claude Code 插件：把任意公众人物研究成教练人格并对话**

面向 Claude Code 用户的 /coach 人格插件：输入人名后自动检索其访谈、书籍、文章与 YouTube 字幕转写（经 yt-dlp 抓取，无需 API key），蒸馏为结构化人格文件（语气、信念、命名框架、语录），随后 Claude 以该人物口吻持续对话。人格本地缓存，重复加载即时完成。支持无视频人物（仅文字研究）与历史人物（基于其著作）。声明限制：仅为基于公开内容的模拟，非本人，非专业建议。可选依赖 yt-dlp，缺失时仅用网络研究构建。

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

- 从 YouTube 转写与网络研究自动构建人物人格文件
- 无需 API key 抓取真实字幕（yt-dlp，可选依赖）
- 人格本地缓存，重复加载即时完成
- 支持历史人物（仅基于其著作文集构建）

## 适用场景

- 想以某位商业或健康领域人物的口吻获得辅导式对话
- 在 Claude Code 中随时切换多位教练人格
- 研究某个公众人物的方法论并与其对话式探讨

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L3: Talk to Anyone — Claude Code plugin
> L29: /plugin marketplace add coltonjosephdean-rgb/talk-to-anyone
> L30: /plugin install talk-to-anyone@talk-to-anyone

## 星数曲线

```mermaid
xychart-beta
    title "coltonjosephdean-rgb/talk-to-anyone 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 66 --> 68
    line [67, 67]
```

2026-10-18 67 → 2026-10-25 67（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `9ca92f04097c` · [字段定义](../../DATASET.md)*
