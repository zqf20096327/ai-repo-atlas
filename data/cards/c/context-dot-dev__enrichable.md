# context-dot-dev/enrichable

⭐ 37 · TypeScript · MIT · 推送 2026-11-19 · [GitHub](https://github.com/context-dot-dev/enrichable) · [官网](https://www.enrichable.io) · 组织维护

**面向销售/增长团队的 AI 数据富化电子表格**

开源 AI 电子表格：用自然语言描述目标公司或人群即可生成行列表（按域名去重），再通过英文提问列对每一行做实时网络研究（定价页、CEO、技术栈、工作邮箱），每个答案附带来源与置信度。邮箱瀑布按用户顺序依次尝试 Hunter、Prospeo、Apollo、QuickEnrich、ContactOut。需自备 Context.dev 与 OpenAI API key，数据存于 Neon Postgres，本地公式在浏览器内运行。限制：每工作区 10 张表、每表 1000 行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提示词生成线索列表，行流式写入并按域名去重
- AI 研究列对每行做实时网络检索，答案保留来源与置信度
- 多供应商工作邮箱瀑布（Hunter/Prospeo/Apollo/QuickEnrich/ContactOut）
- 提供 MCP server，Claude Code/Cursor 等客户端可读写并富化表格

## 适用场景

- 从一句话描述生成销售线索清单并补全公司信息
- 为每行联系人查找并验证工作邮箱
- 对客户名单批量检查定价、融资、技术栈等公开事实
- 把表格暴露给 MCP 客户端由 agent 读写和富化

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L21: **Enrichable is an open-source AI spreadsheet for data enrichment.** Describe the companies or people you want and 
> L34: - **MCP server.** Claude Code, Cursor and other MCP clients can read, edit and enrich your sheets.
> L76: |Context.dev|Web search, scraping, company and people data|Required|


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `dab7d048977d` · [字段定义](../../DATASET.md)*
