# Synthos-Logic/giurisprudenza-db

⭐ 10 · Python · MIT · 推送 2026-11-23 · [GitHub](https://github.com/Synthos-Logic/giurisprudenza-db) · [官网](https://synthoslogic.ai) · 个人维护

**意大利判例法开放数据集：宪法法院判例与最高法院摘要**

以 Markdown 一判例一卡片形式发布的意大利判例法开放数据库：收录最高法院判决办公室每周标注的刑事/民事判例（含官方摘要、要点与判决书原文 PDF 链接）、宪法法院自 1956 年以来全部判决（22,000+，来自官方开放数据服务）、预审移送索引、月度摘要集与多份开放获取期刊的元数据雷达。数据字段逐字取自官方来源，缺失即留空并隔离未完成卡片；通过 Python 脚本以周为节奏更新。卡片与数据库采用 CC BY 4.0，脚本采用 MIT。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 宪法法院 1956 年至今全部判决（22,000+），来自官方开放数据服务
- 字段逐字复制官方页面，缺失字段留 null，含不完整卡片隔离机制
- 月度摘要 PDF 自动转换为带页码标记的 Markdown 并抹除律师姓名
- 附 Python 更新脚本，支持 --dry-run 与 --backfill 参数

## 适用场景

- 为法律 AI 检索增强应用提供可溯源的意大利判例语料
- 查询特定年份与主题的宪法法院判例及官方摘要
- 跟踪开放获取法律期刊的判例信号

## 场景标签

 · 领域:法律/数据集

## 证据(README 行号)

> L1: # giurisprudenza-db
> L121: In `CONSULTA/` **tutte** le pronunce della Corte costituzionale dal 1956 a oggi (oltre 22.000), costruite dal
> L165: - Ogni campo proviene dalla pagina ufficiale della Corte ed è copiato **testualmente**;

## 星数曲线

```mermaid
xychart-beta
    title "Synthos-Logic/giurisprudenza-db 星数(近 2 点)"
    x-axis ["2026-10-30", "2026-11-24"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-30 10 → 2026-11-24 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `348b6d744870` · [字段定义](../../DATASET.md)*
