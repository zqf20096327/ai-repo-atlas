# batuhanzorbeyzengin/rebasis

⭐ 17 · Python · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/batuhanzorbeyzengin/rebasis) · [官网](https://batuhanzorbeyzengin.github.io/rebasis/) · 个人维护

**嵌入模型升级评估与迁移工具：测量是否值得换、免重建索引桥接**

面向已用旧嵌入模型建立向量索引的开发者：当新嵌入模型发布时，先用 probe 在自己的语料和查询日志上测量升级是否值得（break-even 决策，可能建议重索引或维持现状）；值得时用正交 Procrustes 变换（六种候选中按测量选取）把新模型查询向量映射到旧索引空间，一行代码桥接、索引不动；也可 migrate 重写索引（影子副本、回滚、方向校验），并检测半迁移状态（单集合混两种嵌入空间）。提供 CLI（probe/fit/migrate/eval/doctor/status）与 JSON 输出。版本 0.1，API 与 .rbs 适配器格式在 1.0 前可能变更；迁移写入索引的历史缺陷已修复但证据仍在积累。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- probe 按用户语料与查询日志返回 bridge/reindex/维持原状 的决策
- 默认正交 Procrustes 变换（六候选中按测量选取）桥接新旧嵌入空间，不触碰索引
- migrate 支持影子副本、read-back、rollback 与方向校验，拒绝错误方向的适配器
- doctor/status 可检测索引同时持有两种嵌入空间的半迁移状态

## 适用场景

- 向量索引换嵌入模型前先测量升级是否值得
- 不重建索引直接桥接新模型的查询向量
- 安全迁移索引并在中途故障时检测与恢复

## 场景标签

 · 领域:LLM 基础设施/向量检索

## 证据(README 行号)

> L23: rebasis fits a small adapter that maps the **new** model's query vectors into
> L64: - **It decides whether the upgrade is worth doing at all.** Retention alone
> L169: A small learned transform — orthogonal Procrustes by default, chosen from six

## 星数曲线

```mermaid
xychart-beta
    title "batuhanzorbeyzengin/rebasis 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-30 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `2866715620fe` · [字段定义](../../DATASET.md)*
