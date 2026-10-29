# brayden-s-haws/pm_am_newsletter

⭐ 29 · Python · MIT · 推送 2025-11-27 · [GitHub](https://github.com/brayden-s-haws/pm_am_newsletter) · [官网](https://pmnews.today/) · 个人维护

**用 GPT 自动生成产品管理日报新闻邮件的 Python 脚本集**

个人自动化新闻邮件项目：从 Hacker News、Reddit、Product Hunt、邮件订阅等多个来源抓取内容，经 robots.txt 检查后由 GPT 完成 URL 去重与域名权威筛选、主题相关性过滤、文章摘要与邮件导语的链式生成，最终通过 SendGrid 发送给订阅者。包含 Flask 邮件发送端与各来源爬虫脚本，修改提示词与来源可覆盖其他领域。需 OpenAI、SendGrid、Gmail、Reddit API 等账号。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多步 GPT API 链：去重→相关性过滤→摘要→导语生成
- 多来源抓取（Hacker News 类站点、Reddit、Product Hunt、Gmail 收件箱）并遵守 robots.txt
- 用 GPT 的域名权威知识替代付费域名权威工具
- SendGrid 联系人拉取与定时/手动触发的邮件发送（Flask 端点）

## 适用场景

- 每天自动收到产品管理领域的新闻摘要邮件
- 改写提示词和来源，搭建其他主题的自动化新闻邮件
- 学习多步 LLM API 链式调用与爬虫组合的参考实现

## 场景标签

`网页抓取` `AI 写作` · 领域:效率与自动化

## 证据(README 行号)

> L38: - **GPT Filtering**: The text of the de-duplicated URLs is sent to the GPT API and it determines if a story is/isn'
> L39: - **GPT Summaries**: For all the relevant stories the text is again sent to GPT and it produces a summary of the ar

## 星数曲线

```mermaid
xychart-beta
    title "brayden-s-haws/pm_am_newsletter 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-29 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `77cf02406f10` · [字段定义](../../DATASET.md)*
