# evgeniycheban/spring-data-reindexer

⭐ 24 · Java · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/evgeniycheban/spring-data-reindexer) · 个人维护

**面向 Reindexer 数据库的 Spring Data 访问模块**

为 Reindexer（NoSQL/内存数据库）提供 Spring Data 集成层：仓库接口、对象映射、查询方法派生、@Query SQL 查询（可选 JSQLParser 类型安全绑定）、Query By Example、投影、命名空间引用（@NamespaceReference，支持懒加载代理与 SpEL lookup）、基于 @Transactional 的单命名空间事务管理（支持 REQUIRED/REQUIRES_NEW 传播，不支持 NESTED），以及 AOT 支持。通过 Maven 依赖引入，支持 Spring Boot Starter 与纯 Spring 配置两种方式，默认连接 cproto://localhost:6534。查询支持 KNN 向量检索、RANGE 与 JPQL 风格语法。限制：索引创建后不可修改；lazy=true 时 joinType 被忽略；final 类无法被 CGLIB 代理。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 仓库接口、查询派生、@Query SQL/JPQL 查询与 Query By Example
- 支持 KNN 向量检索与 RANGE 的类型安全查询绑定（可选 JSQLParser）
- @NamespaceReference 跨命名空间引用：懒加载代理、SpEL lookup 与排序
- @Transactional 事务管理（REQUIRED/REQUIRES_NEW、只读事务）与 AOT 支持

## 适用场景

- 在 Spring 应用中以仓库模式访问 Reindexer 数据库
- 通过 SQL/JPQL 或派生查询方法执行含 KNN 向量检索的查询
- 在 Spring Boot 项目中通过 Starter 快速接入 Reindexer

## 场景标签

 · 领域:数据库访问/Java 生态

## 证据(README 行号)

> L4: Spring Data module for the Reindexer database. Provides repositories, object mapping, query derivation,
> L165: @Query("SELECT *, vectors(), rank() FROM item_float_vectors WHERE knn(float_vector_index, :vector, :knnSearchParam

## 星数曲线

```mermaid
xychart-beta
    title "evgeniycheban/spring-data-reindexer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-29 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `861add7fea0c` · [字段定义](../../DATASET.md)*
