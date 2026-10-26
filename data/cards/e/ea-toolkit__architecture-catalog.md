# ea-toolkit/architecture-catalog

⭐ 41 · TypeScript · MIT · 推送 2026-05-01 · [GitHub](https://github.com/ea-toolkit/architecture-catalog) · [官网](https://architecture-catalog.web.app) · 组织维护

**Markdown 驱动的企业架构建模目录静态站点生成器**

面向企业架构管理的 Git-native 目录工具：用 Markdown 文件加 YAML frontmatter 建模架构元素，用单个 YAML 文件定义 schema，经构建步骤生成含仪表盘、域地图、上下文依赖图、事件流图与健康评分的静态站点。基于 Astro 5 与 React 18，词汇表无关，支持 ArchiMate、TOGAF、C4 或自定义词汇，可白标定制品牌。无数据库、无服务器，仅依赖文件、Git 与构建步骤；工具部分含校验、仪表盘生成器与 Claude skills。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Markdown + YAML frontmatter 建模，单一 registry-mapping.yaml 定义 schema
- 生成仪表盘、上下文依赖图、事件流图与健康评分的静态站点
- 词汇表无关：兼容 ArchiMate/TOGAF/C4 或自定义词汇
- 白标定制：改几行 YAML 即可换成自己的品牌

## 适用场景

- 用 Git 管理并发布企业架构目录
- 为架构评审提供可交互的依赖图与事件流视图
- 按自定义 schema 组织领域架构文档并生成导航站点

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L10: **A schema-driven, white-label architecture catalog that turns Markdown files into a beautiful, interactive static 
> L18: Model your enterprise architecture using plain Markdown files with YAML frontmatter, define your schema in a single
> L69: |Tools|Validation, dashboard generator, Claude skills|

## 星数曲线

```mermaid
xychart-beta
    title "ea-toolkit/architecture-catalog 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-26"]
    y-axis "stars" 39 --> 42
    line [40, 41, 41]
```

2026-10-18 40 → 2026-10-26 41（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `dec7c776eb91` · [字段定义](../../DATASET.md)*
