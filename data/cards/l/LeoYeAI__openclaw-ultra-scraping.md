# LeoYeAI/openclaw-ultra-scraping

⭐ 23 · Python · MIT · 推送 2026-06-21 · [GitHub](https://github.com/LeoYeAI/openclaw-ultra-scraping) · [官网](https://myclaw.ai) · 组织维护 · 中文 README

**OpenClaw agent 的自适应网页抓取技能包（已归档）**

面向 OpenClaw agent 的网页抓取技能：基于 Scrapling 提供 3 级抓取器（HTTP/动态浏览器/隐身浏览器），内置 Cloudflare Turnstile 绕过、自适应元素追踪（站点改版后仍可定位元素）、并发爬虫与代理轮换，输出 JSON/CSV/Markdown 等格式。安装方式为 clawhub install 或克隆到 OpenClaw skills 目录后运行 setup.sh；需 OpenClaw 实例、Python 3.10+ 与约 2GB 磁盘。注意：仓库已归档，开发迁移至 LeoYeAI/ultra-scraper。

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

- 3 级抓取器：HTTP → 动态浏览器 → 隐身浏览器
- Cloudflare Turnstile 等 anti-bot 绕过（--solve-cloudflare）
- 自适应元素追踪，站点改版后元素仍可定位
- 并发爬虫框架，支持暂停/恢复与代理轮换

## 适用场景

- 让 OpenClaw agent 抓取受 Cloudflare 保护的页面数据
- 并发爬取整站并导出 JSON/CSV/Markdown
- 站点改版后无需重写选择器继续提取数据

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L13: > Built by MyClaw.ai — the AI personal assistant platform that gives every user a full server with complete code co
> L23: An OpenClaw agent skill that gives your AI assistant powerful web scraping superpowers — with built-in anti-bot byp

## 星数曲线

```mermaid
xychart-beta
    title "LeoYeAI/openclaw-ultra-scraping 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-28 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `3b82020ede84` · [字段定义](../../DATASET.md)*
