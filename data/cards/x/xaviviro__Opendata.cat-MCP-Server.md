# xaviviro/Opendata.cat-MCP-Server

⭐ 22 · TypeScript · 推送 2026-09-17 · [GitHub](https://github.com/xaviviro/Opendata.cat-MCP-Server) · [官网](https://opendata.cat/mcp/) · 组织维护

**连接 LLM 与加泰罗尼亚 15 个开放数据门户的 MCP 服务器**

由非营利协会 opendata.cat 维护的 MCP (Model Context Protocol) 服务器，让 Claude、ChatGPT 等 LLM 客户端检索和查询加泰罗尼亚公共开放数据：覆盖 15 个门户共 3,073 个数据集，支持 Socrata、CKAN、GTFS-RT 实时列车位置、Idescat、INE、REE 电价、CNMC 油价等多种 API 类型。提供 9 个工具（检索数据集、查询原门户真实数据、电台档案检索等）和 4 个 SKILL.md 研究指南；每周自动更新目录。不存储数据，每次查询直达官方来源。可通过 npm 安装或直接经 Streamable HTTP 端点使用，文档为加泰罗尼亚语。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 15 个门户、3,073 个数据集的统一检索与查询
- GTFS-RT 实时查询 FGC 与 Renfe Rodalies 列车位置和延误
- 以 MCP resources 和 slash-command 形式发布 4 个研究技能（SKILL.md）
- search_radioteca 检索约 48.5 万条加泰罗尼亚电台档案条目

## 适用场景

- 在 Claude 等 MCP 客户端中直接提问加泰罗尼亚水库水位、电价、油价等数据
- 调查某市的预算、债务、公共采购情况
- 查询实时近郊铁路列车延误信息
- 检索加泰罗尼亚电台历史节目与人物档案

## 场景标签

`语义搜索` `网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L11: Servidor MCP (Model Context Protocol) que connecta els models de llenguatge (Claude, ChatGPT, Gemini...) amb les **
> L174: ```

## 星数曲线

```mermaid
xychart-beta
    title "xaviviro/Opendata.cat-MCP-Server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-28 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `cbc77fa5f84c` · [字段定义](../../DATASET.md)*
