# discourselab/scrapai-cli

⭐ 117 · Python · Apache-2.0 · 推送 2026-10-20 · [GitHub](https://github.com/discourselab/scrapai-cli) · [官网](https://docs.scrapai.dev) · 组织维护

**用自然语言描述需求、由 AI agent 生成可复用 Scrapy 爬虫的 CLI**

scrapai 是构建在 Scrapy 之上的自托管爬虫编排层：用户以英文描述抓取目标，AI coding agent（官方测试使用 Claude Code）分析网站并生成经 Pydantic 校验的 JSON 配置，存入 SQLite 数据库，由通用 DatabaseSpider 加载运行；运行时无 AI 参与、无按页成本。集成 CloakBrowser 做 JS 渲染与 Cloudflare 绕过（cookie 缓存、代理升级、断点续爬、增量抓取），可选 Pueue 后台队列。通过 git clone 与 ./scrapai setup 安装，适合需要批量抓取大量网站的团队与非技术用户；不支持登录墙/付费墙与硬验证码站点。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AI 在构建期生成 JSON 爬虫配置，运行期走确定性 Scrapy 流程，成本按站点而非按页计
- 生成的配置经 Pydantic 校验、SSRF 检查后存 SQLite，可导出/导入复用
- CloakBrowser 处理 JS 渲染与 Cloudflare 绕过，cookie 缓存后复用 Scrapy HTTP 引擎
- 批量队列、健康检查、断点续爬与增量抓取（跳过已抓 URL）

## 适用场景

- 用一句话让 AI 帮我给新闻/电商/论坛站点建好可复用爬虫
- 批量管理上百个站点的爬虫并定期重跑构建数据集
- 抓取 Cloudflare 保护的公开网站内容

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L7:  A CLI where you describe what you want to scrape in plain English, an AI agent builds the scraper, and Scrapy runs 
> L57: You (plain English) → AI Agent → JSON config → Database → Scrapy crawl
> L163: scrapai is designed to work with AI coding agents. The agent reads the workflow instructions, analyzes websites, a

## 星数曲线

```mermaid
xychart-beta
    title "discourselab/scrapai-cli 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-23"]
    y-axis "stars" 115 --> 118
    line [116, 117, 117]
```

2026-10-18 116 → 2026-10-23 117（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `d5f9783693e7` · [字段定义](../../DATASET.md)*
