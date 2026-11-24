# scrapesmith/scrape-skill

⭐ — · [GitHub]() · 个人维护

**Claude Code 技能：一句话描述即从网站抓取数据生成 CSV**

面向不会网页抓取的用户，通过 Claude Code 技能以 URL 加一句描述获取 CSV。流程固定为分析（在真实 Chrome 窗口寻找隐藏 JSON 接口、页面内嵌数据、API 拦截或 DOM 四条路径）、确认（展示 5 行样例与截图标注，用户确认后继续）、采集（限速采集并保存 recipe 以便复用）。遇到登录、robots.txt 限制或反爬时停下告知用户并由用户决定，不做验证码破解、隐身补丁或代理轮换。可脱离 Claude 用 Node 直接运行已保存的 recipe。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- URL + 一句话描述输出 CSV/xlsx，含价格、相对时间、追踪参数清理
- 四条数据路径（http/embedded/intercept/dom）与 5 行样例加截图确认机制
- recipe 保存与站点改版后的自修复（用户确认后更新并保留备份）
- 遇 robots.txt、登录、反爬时停止并告知，不做隐身规避

## 适用场景

- 从电商分类页抓取商品名称、价格与评分
- 从新闻或博客列表页提取标题、作者、时间与正文
- 把职位列表页整理成表格文件
- 复用已保存 recipe 定期重新采集同一站点数据

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L5: Give it a URL and one sentence, get a CSV. No selectors, no code, no scraping vocabulary.
> L16: Claude plays the scraping expert so you don't have to. The order is always the same:

## 星数曲线

```mermaid
xychart-beta
    title "scrapesmith/scrape-skill 星数(近 3 点)"
    x-axis ["2026-10-24", "2026-10-25", "2026-11-24"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-10-24 3 → 2026-11-24 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 mid · 依据 README sha `c97a402c80fa` · [字段定义](../../DATASET.md)*
