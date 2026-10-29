# thevibeworks/claude-reads-hn

⭐ 17 · HTML · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/thevibeworks/claude-reads-hn) · [官网](https://thevibeworks.github.io/claude-reads-hn) · 个人维护

**Claude 定时读 Hacker News 生成辣评摘要并推送的自动化仓库**

基于 GitHub Actions cron 的自动化仓库：Claude 每天四次拉取 HN 前 100 条，去重后取 20 条候选，抓取评论与文章预览，读取 llms.txt 记忆索引避免重复，自行挑选 5 条撰写摘要 JSON，经技能脚本转为 org 文件并重建站点，提交推送后经 Bark/Telegram/Discord 通知。面向想复刻该流程的开发者：fork 仓库、配置 secrets、启用 Actions 即可运行。依赖 Claude Code OAuth token 与 GitHub App 私钥，通知渠道为可选。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- GitHub Actions cron 每日 4 次自动运行，抓取 HN 前 100 条并去重筛选 5 条
- llms.txt 记忆索引记录历史摘要，避免重复选题
- 摘要以 Git 提交存档并由 GitHub Pages 生成静态站点
- Bark/Telegram/Discord 多渠道通知，缺 secrets 时静默跳过

## 适用场景

- 我想让 AI 自动读 Hacker News 并生成带观点的摘要推送给我
- 我想利用 Claude Code 的 5 小时配额窗口保持定时活跃
- 我想留下一份 AI 对 2025 年科技新闻观点的存档

## 场景标签

`网页抓取` `AI 写作` · 领域:效率与自动化

## 证据(README 行号)

> L17: Claude wakes up 4x daily (01:00, 06:00, 11:00, 16:00 UTC; America/Los_Angeles: 17:00, 22:00, 03:00, 08:00 PST; in P
> L66: |`CLAUDE_CODE_OAUTH_TOKEN`|Claude Code OAuth token|Everything. Claude can't run.|

## 星数曲线

```mermaid
xychart-beta
    title "thevibeworks/claude-reads-hn 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-29"]
    y-axis "stars" 15 --> 18
    line [16, 17, 17]
```

2026-10-18 16 → 2026-10-29 17（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `4a4f9e75e38a` · [字段定义](../../DATASET.md)*
