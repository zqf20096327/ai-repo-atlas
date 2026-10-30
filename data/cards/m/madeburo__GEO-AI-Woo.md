# madeburo/GEO-AI-Woo

⭐ 30 · PHP · GPL-2.0 · 推送 2026-03-20 · [GitHub](https://github.com/madeburo/GEO-AI-Woo) · [官网](https://www.geoai.run) · 组织维护 · 中文 README

**WordPress/WooCommerce 的 AI 搜索优化插件：生成 llms.txt 与爬虫规则**

面向 WordPress 站点的 GEO（生成式引擎优化）插件：在站点根目录自动生成 /llms.txt 与 /llms-full.txt 静态文件（文件系统不可写时回退 rewrite 规则），为 16 种 AI 爬虫（GPTBot、ClaudeBot、PerplexityBot 等）输出 robots.txt 指令；提供 AI Meta Box 为文章/页面/商品添加 AI 描述与关键词，可调用 Claude 或 OpenAI API 一键生成描述（限流与密钥加密存储）；WooCommerce 商品自动纳入 llms.txt 并输出 Schema.org 标记。另有内容净化管道、AI 爬虫追踪面板、REST API 与 WP-CLI 命令。要求 PHP 7.4+、WordPress 6.2+，WooCommerce 可选。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自动生成 /llms.txt 与 /llms-full.txt，支持按语言分文件
- 为 GPTBot/ClaudeBot/PerplexityBot 等 16 种 AI 爬虫输出允许/禁止规则
- AI Meta Box 可经 Claude 或 OpenAI API 批量生成描述（单批至多 50 条）
- WooCommerce 商品含价格/库存/评分自动入 llms.txt 与 Schema.org 标记

## 适用场景

- 让我的 WordPress 站点内容被 ChatGPT、Perplexity 等 AI 搜索收录
- 给 WooCommerce 商品生成面向 LLM 的结构化描述
- 按爬虫粒度控制允许或禁止哪些 AI 机器人抓取

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L7: Generate llms.txt, AI crawler rules and metadata to make your site visible to AI search engines.
> L66: - **Generate with AI** — One-click description generation via Claude or OpenAI
> L78: - Generate AI descriptions via **Claude (Anthropic)** or **OpenAI** APIs

## 星数曲线

```mermaid
xychart-beta
    title "madeburo/GEO-AI-Woo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-30 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `a7474e24d946` · [字段定义](../../DATASET.md)*
