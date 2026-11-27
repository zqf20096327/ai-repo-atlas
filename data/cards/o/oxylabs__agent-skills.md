# oxylabs/agent-skills

⭐ 869 · JavaScript · MIT · 推送 2026-11-26 · [GitHub](https://github.com/oxylabs/agent-skills) · 组织维护

**为 AI agent 提供接入 Oxylabs 代理与数据抓取服务的技能集**

Oxylabs 官方发布的 agent 技能集合，包含 5 个技能：Proxies、Web Unblocker、Web Scraper API、Agent Browser、Video Data，以结构化指令形式让 AI agent 调用 Oxylabs 各产品。提供 Claude Code 插件市场安装与通用的 npx 安装方式，凭据通过 .env 环境变量配置。使用需 Oxylabs 账号，README 含推广码并引导至文档。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 5 个技能覆盖代理、解锁、抓取 API、远程浏览器、视频数据
- 支持 Claude Code 插件市场一键安装全部技能
- 通过 CDP 支持 Playwright/Puppeteer 远程浏览器
- 产品路由表按任务需求指引选择技能

## 适用场景

- 让 agent 抓取受保护页面并解析为结构化 JSON
- 为自动化任务配置带地理定位的代理流量
- 提取 YouTube 元数据、字幕与视频下载

## 场景标签

`浏览器自动化` `网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L10: Official agent skills for Oxylabs products. Each skill provides structured instructions that AI agents can use to i
> L36: ### Claude Code (plugin marketplace)

## 星数曲线

```mermaid
xychart-beta
    title "oxylabs/agent-skills 星数(近 11 点)"
    x-axis ["2026-10-25", "2026-10-28", "2026-10-31", "2026-11-06", "2026-11-10", "2026-11-15", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-25", "2026-11-27"]
    y-axis "stars" 867 --> 879
    line [876, 877, 878, 876, 877, 878, 873, 870, 869, 868, 869]
```

2026-10-25 876 → 2026-11-27 869（-7）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `245f392278db` · [字段定义](../../DATASET.md)*
