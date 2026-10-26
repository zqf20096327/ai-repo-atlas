# saskinosie/weaviate-claude-skills

⭐ 39 · MIT · 推送 2025-11-04 · [GitHub](https://github.com/saskinosie/weaviate-claude-skills) · [官网](https://weaviate.io) · 个人维护

**让 Claude.ai 直连本地 Weaviate 向量库的技能集合**

一组面向 Claude.ai / Claude Desktop 的 Claude Skills（SKILL.md 格式知识模块），覆盖 5 个技能：本地 Weaviate Docker 部署、连接与健康检查、集合/Schema 管理、数据摄取（单条/批量/多模态）以及语义/混合/RAG 查询。因 Claude Desktop/Web 有网络限制，设计为连接 localhost:8080 的 Docker 实例，不支持外部 Weaviate Cloud 连接（除非添加允许域名）。获取方式为 ZIP 下载、git clone 或项目内嵌；Python 环境与依赖（weaviate-client 等）由 Claude 自动创建，也可手动 pip 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 5 个技能覆盖部署、连接、Schema 管理、数据摄取与 RAG 查询
- 针对 Claude 网络限制设计的本地 Docker Weaviate 方案（localhost:8080）
- 依赖管理可由 Claude 自动完成（创建 .venv 并安装 weaviate-client 等）
- 技能间通过 frontmatter 声明依赖，可组合成完整数据管道

## 适用场景

- 在 Claude Desktop/Web 中对话式管理本地 Weaviate 向量库
- 把 JSON/CSV 文档导入集合并做语义/RAG 检索
- 为客户交付可复用的向量库操作技能包

## 场景标签

`RAG` `语义搜索` `向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L3: A comprehensive set of Claude Skills for working with **local Weaviate vector databases**. These skills enable you t
> L20: Claude Skills are self-contained knowledge modules that Claude can load on-demand. Each skill is a folder containin
> L90: - RAG (Retrieval Augmented Generation)

## 星数曲线

```mermaid
xychart-beta
    title "saskinosie/weaviate-claude-skills 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 38 --> 40
    line [39, 39]
```

2026-10-18 39 → 2026-10-26 39（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `45fd9cb704cb` · [字段定义](../../DATASET.md)*
