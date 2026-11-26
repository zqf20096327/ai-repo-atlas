# marcello-pichini/ai-science-tracker

⭐ 3 · HTML · CC-BY-4.0 · 推送 2026-11-25 · [GitHub](https://github.com/marcello-pichini/ai-science-tracker) · [官网](https://aisciencetracker.org/) · 个人维护

**AI 驱动的科学发现策展目录，关联模型族与原始来源**

收录 2020 年以来由 AI 赋能的科学成果的英文目录，每条记录含原始来源、日期、证据限制说明与编辑相关性评分；另用 Epoch AI 数据维护模型目录，按名称将模型族与发现关联，并明示该匹配不能确定具体模型版本。含独立的 AI 漏洞追踪页、方法论页与数据校验测试。提供静态站点（GitHub Pages）、开放数据下载（JSON/CSV）、只读静态 API、多语言版本，以及供 Claude Code 等 agent 使用的 SKILL.md 技能与 llms.txt。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `viral` | CC-BY-4.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 发现目录与 Epoch AI 模型目录按模型族名称关联
- 开放数据：JSON/CSV 下载、JSON Schema、只读静态 API
- AI 漏洞追踪作为独立板块，不计入科学发现数
- 提供 SKILL.md 技能与插件，agent 可本地过滤后查询目录

## 适用场景

- 查询 2020 年以来 AI 参与的科学发现及其原始来源
- 按领域/机构/年份过滤并导出目录条目为 JSON 或 CSV
- 让 AI 助手直接回答 AI 科学领域的新进展
- 追踪 AI 发现的安全漏洞案例及修复背景

## 场景标签

`精选清单` · 领域:学习与行业

## 证据(README 行号)

> L5: An English-language catalog of scientific results enabled by AI since 2020, with original sources, dates, evidence c
> L95: The catalog is open data. Downloads: `data/discoveries.json`, `data/discoveries.csv`, `data/vulnerabilities.json`, 

## 星数曲线

```mermaid
xychart-beta
    title "marcello-pichini/ai-science-tracker 星数(近 2 点)"
    x-axis ["2026-11-25", "2026-11-26"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-25 3 → 2026-11-26 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `06930b62510b` · [字段定义](../../DATASET.md)*
