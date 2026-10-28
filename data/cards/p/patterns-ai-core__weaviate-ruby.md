# patterns-ai-core/weaviate-ruby

⭐ 59 · Ruby · MIT · 推送 2026-10-21 · [GitHub](https://github.com/patterns-ai-core/weaviate-ruby) · [官网](https://rubydoc.info/gems/weaviate-ruby) · 个人维护

**Weaviate 向量数据库 API 的 Ruby 客户端库**

封装 Weaviate.io REST/GraphQL API 的 Ruby gem，属于 Langchain.rb 生态的一部分。覆盖 Collections 与 Objects 的增删改、Get/Aggs 查询（where/near_text/sort 参数可用 Ruby 哈希传入并转换为 GraphQL）、分类任务、备份、节点状态、别名、多租户与 RBAC 用户角色管理，另提供可用于 Kubernetes 探针的 live?/ready? 健康检查。通过 Gemfile 或 gem install 安装，供 Ruby 开发者在应用中接入 Weaviate。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖 Collections/Objects/Query/Classification/Backups 等主要 Weaviate 端点
- 查询参数可用 Ruby 哈希表示并自动转换为 GraphQL（字符串转义、符号作枚举）
- 支持多租户集合（含自动创建/激活租户）与 RBAC 用户角色
- live?/ready? 健康检查可用于 Kubernetes 存活/就绪探针

## 适用场景

- Ruby/Rails 应用中接入 Weaviate 做向量存储与检索
- 在 Langchain.rb 生态中作为向量数据库后端
- 管理 Weaviate 集合、数据对象、备份与多租户配置

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L7: Ruby wrapper for the Weaviate.io API.
> L9: Part of the Langchain.rb stack.

## 星数曲线

```mermaid
xychart-beta
    title "patterns-ai-core/weaviate-ruby 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 58 --> 60
    line [59, 59]
```

2026-10-18 59 → 2026-10-28 59（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `c30165b63085` · [字段定义](../../DATASET.md)*
