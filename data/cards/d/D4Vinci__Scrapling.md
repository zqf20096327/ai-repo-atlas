# D4Vinci/Scrapling

⭐ 88,433 · Python · BSD-3-Clause · 推送 2026-10-18 · [GitHub](https://github.com/D4Vinci/Scrapling) · [官网](https://scrapling.readthedocs.io/en/latest/) · 个人维护 · 中文 README

**自适应网页抓取框架：从单次请求到全站爬取**

Python 网页抓取框架，提供三类能力：Spider 爬虫框架（并发爬取、多会话、断点续爬、AutoThrottle 自适应限速、robots.txt 遵循、内置 JSON/JSONL/CSV/XML 导出）；抓取器体系（Fetcher 支持 TLS 指纹伪装，DynamicFetcher 基于 Playwright，StealthyFetcher 处理 Cloudflare Turnstile 等反爬）；自适应解析（页面结构变更后通过相似度算法重新定位元素）。提供 CLI、MCP 接口、Docker 镜像与 AI Agent Skill。面向爬虫开发者与常规数据采集用户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 0.7 天,年发版 24,41 位贡献者
- 涨星:近 1 天 **+276**(自 20261016 起算)
- 安装:pypi 包 `scrapling` 月下载 919,855
- 平台:— · 协议:MCP

## 能力要点

- 解析器学习页面变更，自动重新定位元素（adaptive=True）
- StealthyFetcher 开箱处理 Cloudflare Turnstile，DynamicFetcher 基于 Playwright
- Spider 框架支持并发、断点续爬、AutoThrottle 与流式输出
- 提供 MCP 服务、CLI 与 AI Agent Skill 入口

## 适用场景

- 采集结构会频繁改版网站的数据且选择器不失效
- 绕过 Cloudflare 等反爬机制抓取动态页面
- 大规模并发爬取并支持中断后恢复
- 通过 MCP 让 AI agent 调用抓取能力

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L55: Scrapling is an adaptive Web Scraping framework that handles everything from a single request to a full-scale crawl
> L57: Its parser learns from website changes and automatically relocates your elements when pages update. Its fetchers by
> L183: ### AI Features

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `70e901421465` · [字段定义](../../DATASET.md)*
