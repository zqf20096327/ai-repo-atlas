# mauricerenck/dark-visitors

⭐ 21 · PHP · MIT · 推送 2026-07-16 · [GitHub](https://github.com/mauricerenck/dark-visitors) · [官网](https://maurice-renck.de/kirby/dark-visitors) · 个人维护

**Kirby CMS 插件：通过 robots.txt 拦截 AI 爬虫**

面向 Kirby CMS 网站的插件，调用 Dark Visitors API 识别并在 robots.txt 中屏蔽 AI 助手、AI 数据抓取器、AI 搜索爬虫等指定类型的爬虫；支持覆盖默认规则添加自定义 User-Agent 与 Disallow 规则，并可向 robots.txt 附加 sitemap 声明，可选开启 Dark Visitors 的访问追踪/分析功能。使用需注册 darkvisitors.com 账号并获取 access token，经 composer 安装或手动复制到 site/plugins 目录，配置写入 config.php。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 调用 Dark Visitors API 生成 robots.txt 屏蔽规则
- 可配置屏蔽的 AI 爬虫类型（AI Assistant / AI Data Scraper / AI Search Crawler）
- 支持自定义 User-Agent 规则与 sitemap 声明
- 可选开启 Dark Visitors 追踪/分析功能

## 适用场景

- 阻止 AI 爬虫抓取我网站的内容
- 在 Kirby 站点的 robots.txt 中维护自定义访问规则
- 统计哪些 AI 爬虫访问了我的网站

## 场景标签

 · 领域:网站隐私/访问控制

## 证据(README 行号)

> L3: Dark Visitors is a plugin for Kirby that blocks unwanted AI Crawlers from your website using robots.txt. It uses the
> L30: Set which types of AI crawlers you want to block:

## 星数曲线

```mermaid
xychart-beta
    title "mauricerenck/dark-visitors 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `83aeb64ab032` · [字段定义](../../DATASET.md)*
