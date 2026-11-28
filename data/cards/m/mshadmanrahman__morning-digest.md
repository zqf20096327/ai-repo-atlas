# mshadmanrahman/morning-digest

⭐ 10 · Python · MIT · 推送 2026-04-11 · [GitHub](https://github.com/mshadmanrahman/morning-digest) · [官网](https://github.com/mshadmanrahman/morning-digest#readme) · 个人维护

**个人晨间简报脚本：汇总日程、邮件、新闻于一条摘要**

一个 Python 脚本，每天早晨读取 Google 日历（最多两个日历）、Gmail 邮件与 Brave Search 新闻，生成一份可 90 秒读完的纯文本简报并打印到终端。通过交互式 setup 向导配置姓名、时区、日历 ID 与本地新闻关键词，配置存于 ~/.morning-digest/config.json；支持 cron 定时运行。依赖 Python 3.11+、gog CLI（Google 账号认证桥接）与免费的 Brave Search API key。无登录、无云端同步，代码短小可自行修改。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一条命令聚合日历、Gmail 与新闻为单份纯文本简报
- 交互式 setup 向导，配置保存于本地 config.json
- 支持 cron 定时与输出重定向到任意笔记工具
- 无 SaaS、无登录、无云端同步的本地运行脚本

## 适用场景

- 每天早晨一条命令获取当日日程与邮件摘要
- 用 cron 在工作日早晨自动生成简报
- 按自定义关键词追踪本地/领域新闻
- fork 后替换新闻源或增加 Slack 摘要通道

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L11: **morning-digest fixes this.** One command, one clean briefing. Everything you need to know before 9am - your sched
> L49: `gog` is a small CLI tool that connects to your Google account and lets the script pull your calendar events and Gm
> L64: The news sections (AI news, product news, local news) are powered by Brave Search. You'll need a free API key.

## 星数曲线

```mermaid
xychart-beta
    title "mshadmanrahman/morning-digest 星数(近 2 点)"
    x-axis ["2026-11-08", "2026-11-28"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-11-08 10 → 2026-11-28 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 mid · 依据 README sha `b9f5c3b1b08e` · [字段定义](../../DATASET.md)*
