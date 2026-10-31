# lemon07r/SanityBoard

⭐ 22 · Svelte · 推送 2026-10-24 · [GitHub](https://github.com/lemon07r/SanityBoard) · [官网](https://sanityboard.lr7.dev/) · 组织维护

**SanityHarness AI 编码 agent 评测榜的前端网站**

面向 SanityHarness 评测结果的排行榜前端：以 SvelteKit 2 + Svelte 5 构建的全静态预渲染站点，部署于 Cloudflare Pages。评测数据以 JSON 文件存于 eval-results/ 目录，构建时用 Zod schema 校验并生成类型化的 RunData 对象，路由加载函数消费这些数据生成静态页面，无运行时数据请求。提供主题切换、客户端过滤、浏览器内 ZIP 导出、Markdown 报告编译等功能。本地运行需 Bun 安装依赖并执行构建命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 评测数据以 JSON 文件存储，构建时经 Zod schema 校验生成类型化数据
- 全静态预渲染，无运行时数据请求
- 客户端过滤与浏览器内 ZIP 数据导出
- 构建时编译 Markdown 报告并语法高亮

## 适用场景

- 查看 SanityHarness 编码 agent 评测的排行榜与任务明细
- 下载评测数据做进一步分析
- 作为类似评测榜单的静态站点参考实现

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L5: A leaderboard frontend for SanityHarness AI coding agent evaluations. Static site deployed to Cloudflare Pages.
> L9: SanityBoard is a fully prerendered SvelteKit application. Evaluation data lives as JSON files in `eval-results/`, va

## 星数曲线

```mermaid
xychart-beta
    title "lemon07r/SanityBoard 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-31 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `1b7d36d9a74e` · [字段定义](../../DATASET.md)*
