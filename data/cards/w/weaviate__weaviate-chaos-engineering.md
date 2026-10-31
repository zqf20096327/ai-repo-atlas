# weaviate/weaviate-chaos-engineering

⭐ 22 · Python · BSD-3-Clause · 推送 2026-10-30 · [GitHub](https://github.com/weaviate/weaviate-chaos-engineering) · 组织维护

**Weaviate 向量数据库的混沌工程 CI 测试管线**

针对 Weaviate 的混沌工程风格测试管线，含两条独立流水线：一是在持续注入崩溃的外部干扰下导入大规模数据集，验证每次崩溃可恢复且最终全部对象导入成功；二是导入数据集测量召回率，重启（状态从磁盘恢复）后再次测量，确保 commit log 上的异步操作不降低向量索引质量。全部容器化，通过 bash 脚本或 GitHub Actions workflow 运行，需 Bash、Docker/Docker Compose 与 jq。面向 Weaviate 核心开发者与贡献者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Chaos-Monkey 式崩溃注入导入管线，验证崩溃可恢复与数据完整性
- 重启前后召回率对比，检验向量索引质量不因异步操作退化
- 全容器化，bash 脚本与 GitHub Actions 两种运行方式

## 适用场景

- 验证自构建的 Weaviate 镜像在崩溃场景下的可恢复性
- 确认重启与 commit log 异步操作不影响检索召回率
- 为核心 Weaviate 开发做回归质量测试

## 场景标签

 · 领域:数据库/向量数据库测试基础设施

## 证据(README 行号)

> L12: This pipelines is a Chaos-Monkey-style pipeline where we aim to import a large
> L20: the CI) and meassures the recall on it. Then Weaviate is stopped and restarted

## 星数曲线

```mermaid
xychart-beta
    title "weaviate/weaviate-chaos-engineering 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-31 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `ee4d8fba7223` · [字段定义](../../DATASET.md)*
