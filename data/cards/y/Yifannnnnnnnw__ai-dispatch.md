# Yifannnnnnnnw/ai-dispatch

⭐ 23 · Python · MIT · 推送 2026-08-05 · [GitHub](https://github.com/Yifannnnnnnnw/ai-dispatch) · 个人维护 · 中文 README

**运行在 GitHub Actions 上的每日 AI 资讯邮件简报生成器**

面向个人用户的自动化 AI 情报日报工具：每日从多个 RSS 源聚合 AI、机器人与 Agent 领域内容，由用户选择的 LLM（默认 Gemini，可选 Anthropic）分析后生成含重点新闻、趋势分析、arXiv 论文精选、博客导读与今日信号五个板块的邮件，通过 Gmail 发送。全程运行在 GitHub Actions 上，无需服务器；浏览器内 Fork+配置 Secrets 或本地运行 setup.py 向导均可完成部署，支持中英文输出与自定义 RSS 源，以 sent_history.json 做去重。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多 RSS 源聚合 + LLM 分析生成五板块结构化日报邮件
- 全流程运行于 GitHub Actions，无需服务器与订阅费
- LLM 提供方可选 Gemini（免费默认）或 Anthropic（付费）
- 支持自定义 RSS 源、中英文输出与博客自动去重

## 适用场景

- 每天早晨在邮箱收到 AI/机器人/Agent 领域的聚合深度简报
- 用免费 Gemini 额度零成本运行自动化资讯日报
- 添加自己关注的 RSS 源定制个性化日报内容

## 场景标签

`网页抓取` `AI 写作` · 领域:效率与自动化

## 证据(README 行号)

> L5: Automatically aggregates the latest in AI, Robotics, and Agents every morning — analyzed by an LLM of your choice, d
> L42: |LLM provider|`gemini` (free) or `anthropic` (paid)|

## 星数曲线

```mermaid
xychart-beta
    title "Yifannnnnnnnw/ai-dispatch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-29 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `10bcd22fe6d3` · [字段定义](../../DATASET.md)*
