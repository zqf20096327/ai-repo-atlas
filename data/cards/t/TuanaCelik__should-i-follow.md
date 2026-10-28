# TuanaCelik/should-i-follow

⭐ 46 · Python · 推送 2026-03-30 · [GitHub](https://github.com/TuanaCelik/should-i-follow) · 个人维护

**输入 Bluesky 用户名，总结其发帖主题与语气的演示应用**

基于 Streamlit 的 NLP 演示应用：给定一个 Bluesky 用户 handle，调用 OpenAI gpt-4.1-nano 模型，输出该用户近期发帖的主题类型、语气与所用语言的概览。通过 Haystack 框架构建，使用 OpenAIChatGenerator 与 ChatPromptBuilder（Jinja 模板）组织提示词，作者在模板中加入示例以减少生成模型的幻觉，但仍偶发异常结果。提供 Hugging Face Spaces 在线试用，本地运行需 pip 安装依赖并启动 streamlit。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 输入 Bluesky handle 生成发帖主题/语气/语言概览
- 基于 Haystack 的 OpenAIChatGenerator 与 ChatPromptBuilder 构建
- 提供 Hugging Face Spaces 在线演示

## 适用场景

- 在关注某 Bluesky 用户前快速了解其发帖内容
- 学习 Haystack ChatPromptBuilder 与 Streamlit 集成的写法

## 场景标签

 · 领域:NLP/社交媒体分析

## 证据(README 行号)

> L17: This repo contains a streamlit application that given a Bluesky handle, tells you what type of things they've been 
> L19: It's been built with Haystack using the `OpenAIChatGenerator` and by creating a `ChatPromptBuilder`

## 星数曲线

```mermaid
xychart-beta
    title "TuanaCelik/should-i-follow 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 45 --> 47
    line [46, 46]
```

2026-10-18 46 → 2026-10-28 46（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `f3c5241dc5b0` · [字段定义](../../DATASET.md)*
