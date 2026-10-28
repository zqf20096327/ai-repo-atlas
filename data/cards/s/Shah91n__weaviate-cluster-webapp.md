# Shah91n/weaviate-cluster-webapp

⭐ — · [GitHub]() · 个人维护

**面向开发者的 Weaviate 集群可视化管理 Streamlit 应用**

基于 Streamlit 的轻量 Web 应用，供开发者在不写查询语句的情况下管理与查看 Weaviate 集群：数据查询、集合浏览、分片与 Raft 状态、schema 健康诊断、RBAC 检查、多租户浏览、对象增删改查（含混合 BM25+向量搜索与分页浏览）、通过 Weaviate Agents API 的自然语言问答，以及云存储备份列表。支持本地/自定义/云三种连接模式，可选 OpenAI 向量化密钥注入。面向开发、测试与预发环境，社区项目，明确声明非生产用途。提供源码运行与 Docker 两种方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 集合/分片/Raft/RBAC/多租户的可视化管理与诊断
- 对象 CRUD：分页浏览上限 1,000 对象，混合 BM25+向量搜索
- 经 Weaviate Agents API 提供集合上的自然语言问答
- 自动识别 S3/GCS/Azure 备份后端并列出最近 10 次备份

## 适用场景

- 开发/测试环境快速查看和排查 Weaviate 集群状态
- 不写查询语句浏览集合数据与 schema 配置
- 检查 RBAC 权限与多租户配置

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L8: A lightweight Streamlit web app built for developers who need a quick, visual way to manage and understand their Wea
> L10: Use it to look up data, browse collections, diagnose schema health, inspect cluster state, and understand how your 

## 星数曲线

```mermaid
xychart-beta
    title "Shah91n/weaviate-cluster-webapp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 45 --> 47
    line [46, 46]
```

2026-10-18 46 → 2026-10-27 46（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `905639221eff` · [字段定义](../../DATASET.md)*
