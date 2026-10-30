# namesjoe/ai_digest_finance

⭐ 18 · Python · 推送 2026-05-18 · [GitHub](https://github.com/namesjoe/ai_digest_finance) · [官网](https://sci-brief.com) · 个人维护

**用 Gemini 汇总 OpenAlex 论文并生成月度 PDF 综述**

自动化数据管线：从 OpenAlex API 按查询抓取上月经济/金融领域科学文献，存入 Postgres 表，再将文献内容发送给 Gemini Pro 模型并按预设问题提问，最终生成含总体洞见、关键发现、主题趋势、共性关联、未来方向与文献来源列表等章节的 PDF 月度报告。仓库提供 questions/articles/gemini_report/pgres_utils 四个脚本及一份示例 PDF，需自备 Gemini API key 与 Postgres 数据库；README 未给出安装或运行命令，多领域使用需自行调整表结构增加 FOS 字段。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenAlex API 抓取文献并存入 Postgres（含建表 SQL）
- 调用 Gemini Pro 处理超百万 token 上下文生成报告章节
- 自动生成结构化 PDF 月度综述（含来源文献列表）
- 问题与查询列表在 questions.py 中可配置

## 适用场景

- 按月跟踪某领域（如经济/金融）学术文献动态
- 快速了解上月论文的共同主题与趋势
- 生成可分享的 PDF 文献月报

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L16: We use OpenALex https://openalex.org free database of scientific articles as our main source of data via their API
> L57: Then we use API key for **GEMINI PRO MODEL** with its outstanding context window over 1 million tokens and transfer

## 星数曲线

```mermaid
xychart-beta
    title "namesjoe/ai_digest_finance 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `b5c201410c1a` · [字段定义](../../DATASET.md)*
