# Ashon-G/reddit-bot-cli

⭐ 21 · Python · MIT · 推送 2026-06-29 · [GitHub](https://github.com/Ashon-G/reddit-bot-cli) · 个人维护

**监控 subreddit 关键词并自动回评的命令行 Reddit 机器人**

Python 命令行工具：持续监控指定的多个 subreddit，命中配置的关键词后自动在帖子下发表预设评论。通过 reddit-bot-cli --create-config 交互式生成 config.ini，存放 Reddit API 凭据（client id/secret、账号、user agent）、监控版块、关键词与评论文本；也可手工编辑 .ini 文件。运行日志写入 logs/bot.log。README 未描述任何模型推理或机器学习功能的具体实现，仅徽章与主题标签中出现 machine-learning 字样。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 监控多个 subreddit 并按关键词匹配
- 命中后自动发布预设评论
- 交互式生成 .ini 配置文件
- 活动日志写入 logs/bot.log

## 适用场景

- 自动回复包含特定关键词的 Reddit 帖子
- 为品牌或话题持续监测相关版块动态

## 场景标签

 · 领域:社交平台自动化工具

## 证据(README 行号)

> L2: CodeScene general CodeScene Code Health Google Gemini Reddit Pytest FastAPI Flask Python NumPy

## 星数曲线

```mermaid
xychart-beta
    title "Ashon-G/reddit-bot-cli 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 low · 依据 README sha `a28db51a79a6` · [字段定义](../../DATASET.md)*
