# Jackychen-12/AI-Search

⭐ 117 · TypeScript · MIT · 推送 2026-10-23 · [GitHub](https://github.com/Jackychen-12/AI-Search) · [官网](https://aisearches.cc/) · 个人维护 · 中文 README

**零服务器零数据库的 AI 行业资讯聚合站，每日自动抓取 40+ 源**

基于 Next.js 的静态 AI 资讯聚合站：GitHub Actions 每日并行抓取 40+ 公开来源（模型实验室博客、arXiv、科技媒体、中文媒体、GitHub Trending 等），智能去重分类后静态部署到 GitHub Pages，访客无需登录或 API Key。提供 7 种浏览视角、全文搜索、浏览器本地个性化、GitHub AI 趋势追踪（8 赛道、不估算 Star 数）与免 Key 的 JSON API + SKILL.md 供 Agent 接入。AI 功能（每条资讯一句话点评、周报总结）依赖可选的 DEEPSEEK_API_KEY，无该 Key 其余功能可用；改 FEEDS 数组可改造成其他领域资讯站。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 40+ 来源每日并行抓取、去重分类，GitHub Actions 自动重建部署
- GitHub AI 趋势页：8 赛道、今日/本周/本月 Star 增速（不做估算）
- 免 Key 静态 JSON API + SKILL.md，Agent 可自然语言获取数据
- 个性化（关注/屏蔽/收藏/已读）全存浏览器 localStorage

## 适用场景

- 每天跟踪 AI 行业资讯与开源项目 Star 动态
- Fork 一份零成本部署成自己领域的资讯站
- 让 Agent 通过开放 API 查询每日 AI 资讯

## 场景标签

`网页抓取` `精选清单` · 领域:效率与自动化

## 证据(README 行号)

> L19: 一个**零服务器、零数据库**的 AI 行业资讯聚合站。GitHub Actions 每天自动从 40+ 公开来源抓取最新资讯，AI 生成一句话点评，静态部署到 GitHub Pages——访客不需要登录、不需要 API Key、
> L35: |🔌|**开放 API**|静态 JSON 端点 + SKILL.md，Agent 可用自然语言获取数据|

## 星数曲线

```mermaid
xychart-beta
    title "Jackychen-12/AI-Search 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-24"]
    y-axis "stars" 115 --> 118
    line [116, 117, 117]
```

2026-10-18 116 → 2026-10-24 117（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `dd3d5e940e2a` · [字段定义](../../DATASET.md)*
